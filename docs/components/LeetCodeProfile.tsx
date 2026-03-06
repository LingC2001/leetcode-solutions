"use client";

const PROFILE_URL = "https://leetcode.com/u/lingc2001/";
const AVATAR_URL =
  "https://assets.leetcode.com/users/avatars/avatar_1677916784.png";
const KNIGHT_BADGE_URL =
  "https://leetcode.com/static/images/badges/knight.png";

export function LeetCodeProfile() {
  return (
    <a
      href={PROFILE_URL}
      target="_blank"
      rel="noopener noreferrer"
      className="flex items-center gap-4 rounded-xl border border-fd-border bg-fd-card p-4 pr-5 shadow-sm hover:border-fd-primary/40 hover:shadow-md transition-all group"
    >
      <img
        src={AVATAR_URL}
        alt="lingc2001"
        width={40}
        height={40}
        className="rounded-full ring-2 ring-fd-border group-hover:ring-fd-primary/40 transition-all"
      />
      <div className="flex flex-col min-w-0">
        <span className="font-semibold text-fd-foreground text-sm leading-tight">
          lingc2001
        </span>
        <span className="text-xs text-fd-muted-foreground">
          View LeetCode profile →
        </span>
      </div>
      <div className="flex items-center gap-1.5 ml-2 pl-3 border-l border-fd-border">
        <img
          src={KNIGHT_BADGE_URL}
          alt="Knight"
          width={20}
          height={20}
          className="shrink-0"
        />
        <div className="flex flex-col">
          <span className="text-xs font-semibold text-fd-foreground leading-tight">
            1,860
          </span>
          <span className="text-[10px] text-fd-muted-foreground leading-tight">
            Knight
          </span>
        </div>
      </div>
    </a>
  );
}
