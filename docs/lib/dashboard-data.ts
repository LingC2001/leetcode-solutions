import { source } from "@/lib/source";

export interface DashboardData {
  totalProblems: number;
  difficultyBreakdown: { name: string; value: number; color: string }[];
  categoryBreakdown: {
    category: string;
    slug: string;
    firstProblemUrl: string;
    easy: number;
    medium: number;
    hard: number;
    total: number;
  }[];
  tagFrequency: { tag: string; count: number }[];
  categoriesCovered: number;
  totalCategories: number;
}

const DIFFICULTY_COLORS: Record<string, string> = {
  easy: "#22c55e",
  medium: "#f59e0b",
  hard: "#ef4444",
};

function formatCategory(slug: string): string {
  return slug
    .split("-")
    .map((word) =>
      word === "and" ? "&" : word.charAt(0).toUpperCase() + word.slice(1),
    )
    .join(" ");
}

const ALL_CATEGORIES = [
  "arrays-and-hashing",
  "string",
  "sorting",
  "two-pointers",
  "binary-search",
  "sliding-window",
  "stack",
  "linked-list",
  "tree",
  "heap",
  "backtracking",
  "graph",
  "greedy",
  "dynamic-programming",
  "interval",
  "other",
];

export function getDashboardData(): DashboardData {
  const pages = source.getPages().filter((page: { slugs: string[] }) => page.slugs.length > 1);

  // Difficulty breakdown
  const diffMap: Record<string, number> = { easy: 0, medium: 0, hard: 0 };
  // Category → difficulty → count
  const catMap: Record<string, { easy: number; medium: number; hard: number }> =
    {};
  // Category → first problem URL (by problem number)
  const catFirstUrl: Record<string, { num: number; url: string }> = {};
  // Tag frequency
  const tagMap: Record<string, number> = {};

  for (const page of pages) {
    const diff = (page.data.difficulty ?? "").toLowerCase();
    if (diff in diffMap) {
      diffMap[diff]++;
    }

    const categorySlug = page.slugs[0];
    if (!catMap[categorySlug]) {
      catMap[categorySlug] = { easy: 0, medium: 0, hard: 0 };
    }
    if (diff === "easy" || diff === "medium" || diff === "hard") {
      catMap[categorySlug][diff as "easy" | "medium" | "hard"]++;
    }

    // Track first (lowest-numbered) problem URL per category
    const titleMatch = page.data.title.match(/^(\d+)/);
    const problemNum = titleMatch ? Number(titleMatch[1]) : Number.MAX_SAFE_INTEGER;
    const pageUrl = page.url;
    if (!catFirstUrl[categorySlug] || problemNum < catFirstUrl[categorySlug].num) {
      catFirstUrl[categorySlug] = { num: problemNum, url: pageUrl };
    }

    const tags = (page.data as { tags?: string[] }).tags ?? [];
    for (const tag of tags) {
      const normalizedTag = tag.toLowerCase().trim();
      tagMap[normalizedTag] = (tagMap[normalizedTag] || 0) + 1;
    }
  }

  const difficultyBreakdown = [
    { name: "Easy", value: diffMap.easy, color: DIFFICULTY_COLORS.easy },
    { name: "Medium", value: diffMap.medium, color: DIFFICULTY_COLORS.medium },
    { name: "Hard", value: diffMap.hard, color: DIFFICULTY_COLORS.hard },
  ];

  const categoryBreakdown = Object.entries(catMap)
    .map(([slug, counts]) => ({
      category: formatCategory(slug),
      slug,
      firstProblemUrl: catFirstUrl[slug]?.url ?? `/docs/${slug}`,
      ...counts,
      total: counts.easy + counts.medium + counts.hard,
    }))
    .sort((a, b) => b.total - a.total);

  const tagFrequency = Object.entries(tagMap)
    .map(([tag, count]) => ({ tag, count }))
    .sort((a, b) => b.count - a.count);

  const categoriesWithProblems = new Set(Object.keys(catMap));
  const categoriesCovered = categoriesWithProblems.size;

  return {
    totalProblems: pages.length,
    difficultyBreakdown,
    categoryBreakdown,
    tagFrequency,
    categoriesCovered,
    totalCategories: ALL_CATEGORIES.length,
  };
}
