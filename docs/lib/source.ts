import { docs } from "fumadocs-mdx:collections/server";
import { type InferPageType, loader } from "fumadocs-core/source";
import type { Folder, Node } from "fumadocs-core/page-tree";

/**
 * Extract the leading number from a page tree node's URL.
 * e.g. "/docs/arrays-and-hashing/1-two-sum" → 1
 *      "/docs/medium/128-longest-consecutive-sequence" → 128
 */
function extractProblemNumber(node: Node): number {
  if (node.type === "page" && typeof node.url === "string") {
    const lastSegment = node.url.split("/").pop() ?? "";
    const match = lastSegment.match(/^(\d+)/);
    if (match) return Number(match[1]);
  }
  return Number.MAX_SAFE_INTEGER;
}

function sortFolderNumerically(folder: Folder): Folder {
  folder.children.sort((a, b) => extractProblemNumber(a) - extractProblemNumber(b));
  return folder;
}

// See https://fumadocs.dev/docs/headless/source-api for more info
export const source = loader({
  baseUrl: "/docs",
  source: docs.toFumadocsSource(),
  plugins: [],
  pageTree: {
    transformers: [{
      folder(node, _folderPath, metaPath) {
        // Only auto-sort folders without explicit meta.json ordering
        if (metaPath) return node;
        return sortFolderNumerically(node);
      },
    }],
  },
});

export function getPageImage(page: InferPageType<typeof source>) {
  const segments = [...page.slugs, "image.webp"];

  return {
    segments,
    url: `/og/docs/${segments.join("/")}`,
  };
}

export async function getLLMText(page: InferPageType<typeof source>) {
  const processed = await page.data.getText("processed");

  return `# ${page.data.title}

${processed}`;
}
