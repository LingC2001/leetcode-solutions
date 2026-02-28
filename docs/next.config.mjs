import { createMDX } from 'fumadocs-mdx/next';

const withMDX = createMDX();
const basePath = process.env.GITHUB_PAGES ? '/leetcode-docs' : '';

/** @type {import('next').NextConfig} */
const config = {
  serverExternalPackages: ['@takumi-rs/image-response'],
  
  output: 'export',
  reactStrictMode: true,
  basePath: basePath,
};

export default withMDX(config);
