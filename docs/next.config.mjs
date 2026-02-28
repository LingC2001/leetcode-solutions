import { createMDX } from 'fumadocs-mdx/next';

const withMDX = createMDX();
const isProd = process.env.NODE_ENV === 'production';
const basePath = isProd ? '/leetcode-solutions' : '';

/** @type {import('next').NextConfig} */
const config = {
  output: 'export',
  reactStrictMode: true,

  basePath: basePath,
  assetPrefix: basePath + '/',

  serverExternalPackages: ['@takumi-rs/image-response'],
};

export default withMDX(config);