import { cn } from "@/lib/cn";

const difficultyConfig = {
  easy: {
    label: "Easy",
    className: "bg-green-500/15 text-green-700 dark:text-green-400",
  },
  medium: {
    label: "Medium",
    className: "bg-yellow-500/15 text-yellow-700 dark:text-yellow-400",
  },
  hard: {
    label: "Hard",
    className: "bg-red-500/15 text-red-700 dark:text-red-400",
  },
} as const;

type Difficulty = keyof typeof difficultyConfig;

function isDifficulty(value: string): value is Difficulty {
  return value in difficultyConfig;
}

interface TagsProps {
  difficulty?: string;
  tags?: string[];
}

export function Tags({ difficulty, tags }: TagsProps) {
  if (!difficulty && (!tags || tags.length === 0)) return null;

  return (
    <div className="flex flex-wrap gap-2 not-prose">
      {difficulty && isDifficulty(difficulty) && (
        <span
          className={cn(
            "inline-flex items-center rounded-md px-2.5 py-0.5 text-xs font-semibold",
            difficultyConfig[difficulty].className,
          )}
        >
          {difficultyConfig[difficulty].label}
        </span>
      )}
      {tags?.map((tag) => (
        <span
          key={tag}
          className="inline-flex items-center rounded-md bg-fd-primary/10 px-2.5 py-0.5 text-xs font-medium text-fd-primary"
        >
          {tag}
        </span>
      ))}
    </div>
  );
}
