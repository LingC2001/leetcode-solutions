import { source } from "@/lib/source";
import {
  ProblemsTableClient,
  type Problem,
} from "./ProblemsTableClient";

function formatCategory(slug: string): string {
  return slug
    .split("-")
    .map((word) =>
      word === "and"
        ? "&"
        : word.charAt(0).toUpperCase() + word.slice(1),
    )
    .join(" ");
}

export function ProblemsTable() {
  const pages = source.getPages();

  const problems: Problem[] = pages
    .filter((page) => page.slugs.length > 1)
    .map((page) => {
      const title = page.data.title;
      const numberMatch = title.match(/^(\d+)\./);
      const number = numberMatch ? Number.parseInt(numberMatch[1], 10) : 0;
      const displayTitle = title.replace(/^\d+\.\s*/, "");
      const categorySlug = page.slugs[0];

      return {
        number,
        title,
        displayTitle,
        difficulty: page.data.difficulty ?? "",
        category: formatCategory(categorySlug),
        categorySlug,
        url: page.url,
      };
    })
    .sort((a, b) => a.number - b.number);

  return <ProblemsTableClient problems={problems} />;
}
