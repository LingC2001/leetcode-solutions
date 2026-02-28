import type { BaseLayoutProps } from 'fumadocs-ui/layouts/shared';

// fill this with your actual GitHub info, for example:
export const gitConfig = {
  user: 'lingc2001',
  repo: 'leetcode-solutions',
  branch: 'main',
};

export function baseOptions(): BaseLayoutProps {
  return {
    nav: {
      title: (
        <div className="flex items-center gap-2 font-semibold">
          <img
            src="/logo-light.png"
            alt="Logo"
            className="h-6 w-6 dark:hidden"
          />
          <img
            src="/logo-dark.png"
            alt="Logo"
            className="h-6 w-6 hidden dark:block"
          />
          LeetCode Solutions
        </div>
      ),
    },
    links: [
      {
        text: 'Problems & Solutions',
        url: '/docs',
        on: 'nav',
      },
    ],
    githubUrl: `https://github.com/${gitConfig.user}/${gitConfig.repo}`,
  };
}
