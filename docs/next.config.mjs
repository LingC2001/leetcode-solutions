import { createMDX } from "fumadocs-mdx/next";

const withMDX = createMDX();
const basePath = process.env.GITHUB_PAGES ? "/leetcode-solutions" : "";

/** @type {import('next').NextConfig} */
const config = {
  output: "export",
  reactStrictMode: true,

  basePath: basePath,
  assetPrefix: `${basePath}/`,

  env: {
    NEXT_PUBLIC_BASE_PATH: basePath,
  },

  serverExternalPackages: ["@takumi-rs/image-response"],
};

export default withMDX(config);
