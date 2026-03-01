"use client";

import {
  PieChart,
  Pie,
  Cell,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";
import { useRouter } from "next/navigation";
import type { DashboardData } from "@/lib/dashboard-data";

/* ── Difficulty Donut ───────────────────────────────────────── */

function DifficultyDonut({
  data,
  total,
}: {
  data: DashboardData["difficultyBreakdown"];
  total: number;
}) {
  return (
    <div className="rounded-xl border border-fd-border bg-fd-card p-6 shadow-sm">
      <h2 className="text-lg font-semibold text-fd-foreground mb-4">
        Difficulty Distribution
      </h2>
      <div className="flex items-center justify-center gap-8">
        <ResponsiveContainer width={200} height={200}>
          <PieChart>
            <Pie
              data={data}
              cx="50%"
              cy="50%"
              innerRadius={55}
              outerRadius={85}
              paddingAngle={3}
              dataKey="value"
              stroke="none"
            >
              {data.map((entry) => (
                <Cell key={entry.name} fill={entry.color} />
              ))}
            </Pie>
          </PieChart>
        </ResponsiveContainer>
        <div className="flex flex-col gap-3">
          {data.map((entry) => (
            <div key={entry.name} className="flex items-center gap-3">
              <div
                className="w-3 h-3 rounded-full"
                style={{ backgroundColor: entry.color }}
              />
              <span className="text-sm text-fd-muted-foreground w-16">
                {entry.name}
              </span>
              <span className="text-sm font-semibold text-fd-foreground">
                {entry.value}
              </span>
              <span className="text-xs text-fd-muted-foreground">
                ({total > 0 ? Math.round((entry.value / total) * 100) : 0}%)
              </span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

/* ── Category Bar Chart ─────────────────────────────────────── */

function CategoryBarChart({
  data,
}: {
  data: DashboardData["categoryBreakdown"];
}) {
  const router = useRouter();

  // Build a lookup from display name → first problem URL for click handling
  const urlMap = Object.fromEntries(data.map((d) => [d.category, d.firstProblemUrl]));

  // Custom Y-axis tick that renders as a clickable link
  const CategoryTick = (props: { x: number; y: number; payload: { value: string } }) => {
    const { x, y, payload } = props;
    const url = urlMap[payload.value];
    return (
      <g
        transform={`translate(${x},${y})`}
        onClick={() => router.push(url)}
        style={{ cursor: "pointer" }}
      >
        <text
          x={-6}
          y={0}
          dy={4}
          textAnchor="end"
          fontSize={12}
          fill="var(--color-fd-primary)"
          className="hover:underline"
        >
          {payload.value}
        </text>
      </g>
    );
  };

  return (
    <div className="rounded-xl border border-fd-border bg-fd-card p-6 shadow-sm">
      <h2 className="text-lg font-semibold text-fd-foreground mb-4">
        Problems by Category
      </h2>
      <ResponsiveContainer width="100%" height={Math.max(300, data.length * 40)}>
        <BarChart
          data={data}
          layout="vertical"
          margin={{ top: 0, right: 20, left: 0, bottom: 0 }}
        >
          <CartesianGrid strokeDasharray="3 3" opacity={0.15} horizontal={false} />
          <XAxis type="number" allowDecimals={false} tick={{ fontSize: 12 }} />
          <YAxis
            dataKey="category"
            type="category"
            width={140}
            tick={CategoryTick as any}
          />
          <Tooltip
            contentStyle={{
              backgroundColor: "var(--color-fd-card)",
              border: "1px solid var(--color-fd-border)",
              borderRadius: "8px",
              fontSize: "13px",
            }}
          />
          <Legend wrapperStyle={{ fontSize: "13px" }} />
          <Bar
            dataKey="easy"
            name="Easy"
            stackId="a"
            fill="#22c55e"
            radius={[0, 0, 0, 0]}
            style={{ cursor: "pointer" }}
            onClick={(_: unknown, index: number) => router.push(data[index].firstProblemUrl)}
          />
          <Bar
            dataKey="medium"
            name="Medium"
            stackId="a"
            fill="#f59e0b"
            style={{ cursor: "pointer" }}
            onClick={(_: unknown, index: number) => router.push(data[index].firstProblemUrl)}
          />
          <Bar
            dataKey="hard"
            name="Hard"
            stackId="a"
            fill="#ef4444"
            radius={[0, 4, 4, 0]}
            style={{ cursor: "pointer" }}
            onClick={(_: unknown, index: number) => router.push(data[index].firstProblemUrl)}
          />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}

/* ── Tag Frequency Heatmap ──────────────────────────────────── */

function TagHeatmap({ data }: { data: DashboardData["tagFrequency"] }) {
  const maxCount = Math.max(...data.map((d) => d.count), 1);

  function getOpacity(count: number) {
    return 0.2 + (count / maxCount) * 0.8;
  }

  function getTextColor(count: number) {
    return count / maxCount > 0.5 ? "white" : undefined;
  }

  return (
    <div className="rounded-xl border border-fd-border bg-fd-card p-6 shadow-sm">
      <h2 className="text-lg font-semibold text-fd-foreground mb-4">
        Tag Frequency
      </h2>
      <div className="flex flex-wrap gap-2">
        {data.map(({ tag, count }) => (
          <div
            key={tag}
            className="px-3 py-1.5 rounded-lg text-sm font-medium transition-colors"
            style={{
              backgroundColor: `rgba(59, 130, 246, ${getOpacity(count)})`,
              color: getTextColor(count),
            }}
          >
            {tag}
            <span className="ml-1.5 opacity-80">{count}</span>
          </div>
        ))}
      </div>
    </div>
  );
}

/* ── Hero Stat Card ─────────────────────────────────────────── */

function StatCard({
  label,
  value,
  sublabel,
  color,
}: {
  label: string;
  value: number | string;
  sublabel?: string;
  color?: string;
}) {
  return (
    <div className="rounded-xl border border-fd-border bg-fd-card p-6 shadow-sm flex flex-col items-center justify-center text-center gap-1">
      <span className="text-xs uppercase tracking-wider text-fd-muted-foreground font-medium">
        {label}
      </span>
      <span
        className="text-4xl font-bold"
        style={{ color: color ?? "var(--color-fd-foreground)" }}
      >
        {value}
      </span>
      {sublabel && (
        <span className="text-sm text-fd-muted-foreground">{sublabel}</span>
      )}
    </div>
  );
}

/* ── Main Export ─────────────────────────────────────────────── */

export function DashboardClient({ data }: { data: DashboardData }) {
  const {
    totalProblems,
    difficultyBreakdown,
    categoryBreakdown,
    tagFrequency,
  } = data;

  const easy = difficultyBreakdown.find((d) => d.name === "Easy")?.value ?? 0;
  const medium = difficultyBreakdown.find((d) => d.name === "Medium")?.value ?? 0;
  const hard = difficultyBreakdown.find((d) => d.name === "Hard")?.value ?? 0;

  return (
    <div className="max-w-5xl mx-auto space-y-8">
      {/* Hero heading */}
      <div>
        <h1 className="text-3xl font-bold text-fd-foreground">Dashboard</h1>
        <p className="text-fd-muted-foreground mt-1">
          Overview of solved LeetCode problems
        </p>
      </div>

      {/* Stat Cards */}
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
        <StatCard
          label="Total Solved"
          value={totalProblems}
          sublabel="problems"
        />
        <StatCard label="Easy" value={easy} color="#22c55e" />
        <StatCard label="Medium" value={medium} color="#f59e0b" />
        <StatCard label="Hard" value={hard} color="#ef4444" />
      </div>

      {/* Charts row */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <DifficultyDonut data={difficultyBreakdown} total={totalProblems} />
        <TagHeatmap data={tagFrequency} />
      </div>

      {/* Full-width bar chart */}
      <CategoryBarChart data={categoryBreakdown} />
    </div>
  );
}
