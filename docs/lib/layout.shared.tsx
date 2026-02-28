import type { BaseLayoutProps } from "fumadocs-ui/layouts/shared";
import Image from "next/image";

// fill this with your actual GitHub info, for example:
export const gitConfig = {
  user: "lingc2001",
  repo: "leetcode-solutions",
  branch: "main",
};

export function baseOptions(): BaseLayoutProps {
  const basePath = process.env.NEXT_PUBLIC_BASE_PATH ?? "";

  return {
    nav: {
      title: (
        <div className="flex items-center gap-2 font-semibold">
          <Image
            src={`${basePath}/logo-light.png`}
            alt="Logo"
            width={24}
            height={24}
            className="dark:hidden"
            unoptimized={true}
          />
          <Image
            src={`${basePath}/logo-dark.png`}
            alt="Logo"
            width={24}
            height={24}
            className="hidden dark:block"
            unoptimized={true}
          />
          LeetCode Solutions
        </div>
      ),
    },
    links: [
      {
        text: "Problems & Solutions",
        url: "/docs",
        on: "nav",
      },
    ],
    githubUrl: `https://github.com/${gitConfig.user}/${gitConfig.repo}`,
  };
}
