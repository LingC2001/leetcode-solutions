"use client";

import { useEffect, useState } from "react";

interface ActivityHeatmapProps {
  /** Array of ISO date strings (YYYY-MM-DD) when problems were solved */
  solveDates: string[];
}

/* ── Helpers ─────────────────────────────────────────────────── */

/** Return YYYY-MM-DD string in local time */
function toDateStr(d: Date): string {
  const y = d.getFullYear();
  const m = String(d.getMonth() + 1).padStart(2, "0");
  const day = String(d.getDate()).padStart(2, "0");
  return `${y}-${m}-${day}`;
}

/** Short month name */
const MONTHS = [
  "Jan",
  "Feb",
  "Mar",
  "Apr",
  "May",
  "Jun",
  "Jul",
  "Aug",
  "Sep",
  "Oct",
  "Nov",
  "Dec",
];

const DAY_LABELS = ["", "Mon", "", "Wed", "", "Fri", ""];

/** Map a count to a green intensity level 0–4 */
function getLevel(count: number): number {
  if (count === 0) return 0;
  if (count === 1) return 1;
  if (count <= 2) return 2;
  if (count <= 4) return 3;
  return 4;
}

const LEVEL_COLORS = [
  "var(--heatmap-empty, #161b22)", // level 0
  "var(--heatmap-l1, #0e4429)", // level 1
  "var(--heatmap-l2, #006d32)", // level 2
  "var(--heatmap-l3, #26a641)", // level 3
  "var(--heatmap-l4, #39d353)", // level 4
];

/* ── Component ───────────────────────────────────────────────── */

interface HeatmapData {
  weeks: { date: string; count: number; dayOfWeek: number }[][];
  monthLabels: { label: string; weekIndex: number }[];
  countMap: Record<string, number>;
  totalActiveDays: number;
  maxStreak: number;
  totalSolves: number;
}

function computeHeatmapData(solveDates: string[]): HeatmapData {
  // Build count map from dates
  const countMap: Record<string, number> = {};
  for (const d of solveDates) {
    countMap[d] = (countMap[d] || 0) + 1;
  }

  // Compute date range: past 52 weeks + current partial week
  const today = new Date();
  today.setHours(0, 0, 0, 0);

  // Start from the Sunday 52 weeks ago
  const startDate = new Date(today);
  startDate.setDate(startDate.getDate() - 363 - startDate.getDay());

  // Build weeks (columns) of 7 days each
  const weeks: { date: string; count: number; dayOfWeek: number }[][] = [];
  const monthLabels: { label: string; weekIndex: number }[] = [];
  let prevMonth = -1;

  const cursor = new Date(startDate);
  let currentWeek: { date: string; count: number; dayOfWeek: number }[] = [];

  while (cursor <= today) {
    const dateStr = toDateStr(cursor);
    const dayOfWeek = cursor.getDay(); // 0=Sun

    // Track month labels (show on first occurrence in a new week)
    if (dayOfWeek === 0 && cursor.getMonth() !== prevMonth) {
      prevMonth = cursor.getMonth();
      monthLabels.push({
        label: MONTHS[cursor.getMonth()],
        weekIndex: weeks.length,
      });
    }

    currentWeek.push({
      date: dateStr,
      count: countMap[dateStr] || 0,
      dayOfWeek,
    });

    if (dayOfWeek === 6 || cursor.getTime() === today.getTime()) {
      weeks.push(currentWeek);
      currentWeek = [];
    }

    cursor.setDate(cursor.getDate() + 1);
  }

  // Push remaining partial week
  if (currentWeek.length > 0) {
    weeks.push(currentWeek);
  }

  // Compute stats
  let totalActiveDays = 0;
  let maxStreak = 0;
  let currentStreak = 0;

  // Walk through all days in range for streak calc
  const walker = new Date(startDate);
  while (walker <= today) {
    const ds = toDateStr(walker);
    if (countMap[ds]) {
      totalActiveDays++;
      currentStreak++;
      if (currentStreak > maxStreak) maxStreak = currentStreak;
    } else {
      currentStreak = 0;
    }
    walker.setDate(walker.getDate() + 1);
  }

  return {
    weeks,
    monthLabels,
    countMap,
    totalActiveDays,
    maxStreak,
    totalSolves: solveDates.length,
  };
}

export function ActivityHeatmap({ solveDates }: ActivityHeatmapProps) {
  // Defer date-dependent computation to client-only to avoid hydration mismatch
  // (server builds at one time, client hydrates at a potentially different time)
  const [data, setData] = useState<HeatmapData | null>(null);

  useEffect(() => {
    setData(computeHeatmapData(solveDates));
  }, [solveDates]);

  if (!data) {
    // SSR / initial render placeholder — matches approximate card height
    return (
      <div className="rounded-xl border border-fd-border bg-fd-card p-6 shadow-sm">
        <div className="h-[180px]" />
      </div>
    );
  }

  const { weeks, monthLabels, totalActiveDays, maxStreak, totalSolves } = data;

  const cellSize = 13;
  const cellGap = 3;
  const cellStep = cellSize + cellGap;
  const dayLabelWidth = 32;
  const topPadding = 20; // space for month labels
  const svgWidth = dayLabelWidth + weeks.length * cellStep + 2;
  const svgHeight = topPadding + 7 * cellStep + 2;

  return (
    <div className="rounded-xl border border-fd-border bg-fd-card p-6 shadow-sm">
      {/* Header with stats */}
      <div className="flex flex-wrap items-center justify-between gap-4 mb-4">
        <h2 className="text-lg font-semibold text-fd-foreground">
          {totalSolves} problems solved in the past year
        </h2>
        <div className="flex items-center gap-6 text-sm text-fd-muted-foreground">
          <span>
            Active days:{" "}
            <span className="font-semibold text-fd-foreground">
              {totalActiveDays}
            </span>
          </span>
          <span>
            Max streak:{" "}
            <span className="font-semibold text-fd-foreground">
              {maxStreak}
            </span>
          </span>
        </div>
      </div>

      {/* Heatmap grid */}
      <div className="w-full">
        <svg
          viewBox={`0 0 ${svgWidth} ${svgHeight}`}
          className="block w-full h-auto"
          role="img"
          aria-label="Activity heatmap showing problem solving activity over the past year"
        >
          {/* Month labels */}
          {monthLabels.map(({ label, weekIndex }) => (
            <text
              key={`${label}-${weekIndex}`}
              x={dayLabelWidth + weekIndex * cellStep}
              y={12}
              className="fill-fd-muted-foreground"
              fontSize={11}
              fontFamily="inherit"
            >
              {label}
            </text>
          ))}

          {/* Day labels (Mon, Wed, Fri) */}
          {DAY_LABELS.map(
            (label, i) =>
              label && (
                <text
                  key={label}
                  x={0}
                  y={topPadding + i * cellStep + cellSize - 2}
                  className="fill-fd-muted-foreground"
                  fontSize={10}
                  fontFamily="inherit"
                >
                  {label}
                </text>
              ),
          )}

          {/* Grid cells */}
          {weeks.map((week, weekIdx) =>
            week.map((day) => (
              <rect
                key={day.date}
                x={dayLabelWidth + weekIdx * cellStep}
                y={topPadding + day.dayOfWeek * cellStep}
                width={cellSize}
                height={cellSize}
                rx={2}
                ry={2}
                fill={LEVEL_COLORS[getLevel(day.count)]}
                className="transition-opacity hover:opacity-80"
              >
                <title>
                  {day.count > 0
                    ? `${day.count} problem${day.count > 1 ? "s" : ""} on ${day.date}`
                    : `No activity on ${day.date}`}
                </title>
              </rect>
            )),
          )}
        </svg>
      </div>

      {/* Legend */}
      <div className="flex items-center justify-end gap-1.5 mt-3 text-xs text-fd-muted-foreground">
        <span>Less</span>
        {LEVEL_COLORS.map((color) => (
          <div
            key={color}
            className="rounded-sm"
            style={{ width: 12, height: 12, backgroundColor: color }}
          />
        ))}
        <span>More</span>
      </div>
    </div>
  );
}
