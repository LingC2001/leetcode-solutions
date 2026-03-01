"use client";

import { Search } from "lucide-react";
import Link from "next/link";
import { useMemo, useState } from "react";

export interface Problem {
  number: number;
  title: string;
  displayTitle: string;
  difficulty: string;
  category: string;
  categorySlug: string;
  url: string;
}

const difficultyConfig = {
  easy: {
    label: "Easy",
    active:
      "bg-green-500/20 text-green-700 dark:text-green-400 ring-1 ring-green-500/30",
    badge: "bg-green-500/15 text-green-700 dark:text-green-400",
  },
  medium: {
    label: "Medium",
    active:
      "bg-yellow-500/20 text-yellow-700 dark:text-yellow-400 ring-1 ring-yellow-500/30",
    badge: "bg-yellow-500/15 text-yellow-700 dark:text-yellow-400",
  },
  hard: {
    label: "Hard",
    active:
      "bg-red-500/20 text-red-700 dark:text-red-400 ring-1 ring-red-500/30",
    badge: "bg-red-500/15 text-red-700 dark:text-red-400",
  },
} as const;

type Difficulty = keyof typeof difficultyConfig;

export function ProblemsTableClient({
  problems,
}: {
  problems: Problem[];
}) {
  const [search, setSearch] = useState("");
  const [difficulty, setDifficulty] = useState<string>("all");
  const [category, setCategory] = useState<string>("all");

  const categories = useMemo(() => {
    const cats = new Map<string, string>();
    for (const p of problems) {
      cats.set(p.categorySlug, p.category);
    }
    return [...cats.entries()].sort((a, b) => a[1].localeCompare(b[1]));
  }, [problems]);

  const filtered = useMemo(() => {
    return problems.filter((p) => {
      if (difficulty !== "all" && p.difficulty !== difficulty) return false;
      if (category !== "all" && p.categorySlug !== category) return false;
      if (search) {
        const q = search.toLowerCase();
        return (
          p.displayTitle.toLowerCase().includes(q) ||
          p.number.toString().includes(q)
        );
      }
      return true;
    });
  }, [problems, search, difficulty, category]);

  return (
    <div className="not-prose space-y-4">
      {/* Search */}
      <div className="relative">
        <Search className="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-fd-muted-foreground pointer-events-none" />
        <input
          type="text"
          placeholder="Search problems..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          className="w-full rounded-lg border border-fd-border bg-fd-card pl-10 pr-4 py-2 text-sm text-fd-foreground placeholder:text-fd-muted-foreground focus:outline-none focus:ring-2 focus:ring-fd-ring transition-shadow"
        />
      </div>

      {/* Filters */}
      <div className="flex flex-wrap items-center gap-3">
        <div className="flex items-center gap-1.5 rounded-lg bg-fd-muted/50 p-1">
          <button
            type="button"
            onClick={() => setDifficulty("all")}
            className={`rounded-md px-3 py-1 text-xs font-medium transition-all ${
              difficulty === "all"
                ? "bg-fd-background text-fd-foreground shadow-sm"
                : "text-fd-muted-foreground hover:text-fd-foreground"
            }`}
          >
            All
          </button>
          {(["easy", "medium", "hard"] as Difficulty[]).map((d) => (
            <button
              type="button"
              key={d}
              onClick={() =>
                setDifficulty(difficulty === d ? "all" : d)
              }
              className={`rounded-md px-3 py-1 text-xs font-medium transition-all ${
                difficulty === d
                  ? difficultyConfig[d].active
                  : "text-fd-muted-foreground hover:text-fd-foreground"
              }`}
            >
              {difficultyConfig[d].label}
            </button>
          ))}
        </div>

        <select
          value={category}
          onChange={(e) => setCategory(e.target.value)}
          className="rounded-lg border border-fd-border bg-fd-card px-3 py-1.5 text-xs text-fd-foreground focus:outline-none focus:ring-2 focus:ring-fd-ring transition-shadow"
        >
          <option value="all">All Categories</option>
          {categories.map(([slug, label]) => (
            <option key={slug} value={slug}>
              {label}
            </option>
          ))}
        </select>

        <span className="ml-auto text-xs text-fd-muted-foreground tabular-nums">
          {filtered.length} of {problems.length} problems
        </span>
      </div>

      {/* Table */}
      <div className="overflow-x-auto rounded-lg border border-fd-border">
        <table className="w-full text-sm">
          <thead>
            <tr className="border-b border-fd-border bg-fd-muted/40">
              <th className="whitespace-nowrap px-4 py-2.5 text-left text-xs font-medium text-fd-muted-foreground w-14">
                #
              </th>
              <th className="px-4 py-2.5 text-left text-xs font-medium text-fd-muted-foreground">
                Problem
              </th>
              <th className="whitespace-nowrap px-4 py-2.5 text-left text-xs font-medium text-fd-muted-foreground w-24">
                Difficulty
              </th>
              <th className="whitespace-nowrap px-4 py-2.5 text-left text-xs font-medium text-fd-muted-foreground hidden sm:table-cell">
                Category
              </th>
            </tr>
          </thead>
          <tbody className="divide-y divide-fd-border">
            {filtered.map((p) => (
              <tr
                key={p.number}
                className="transition-colors hover:bg-fd-muted/30"
              >
                <td className="px-4 py-2.5 text-fd-muted-foreground tabular-nums text-xs">
                  {p.number}
                </td>
                <td className="px-4 py-2.5">
                  <Link
                    href={p.url}
                    className="font-medium text-fd-foreground hover:text-fd-primary transition-colors"
                  >
                    {p.displayTitle}
                  </Link>
                </td>
                <td className="px-4 py-2.5">
                  {p.difficulty in difficultyConfig && (
                    <span
                      className={`inline-flex items-center rounded-md px-2 py-0.5 text-xs font-semibold ${
                        difficultyConfig[p.difficulty as Difficulty].badge
                      }`}
                    >
                      {difficultyConfig[p.difficulty as Difficulty].label}
                    </span>
                  )}
                </td>
                <td className="px-4 py-2.5 text-xs text-fd-muted-foreground hidden sm:table-cell">
                  {p.category}
                </td>
              </tr>
            ))}
            {filtered.length === 0 && (
              <tr>
                <td
                  colSpan={4}
                  className="px-4 py-12 text-center text-fd-muted-foreground"
                >
                  No problems found matching your filters.
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}
