import Link from 'next/link';

export default function HomePage() {
  return (
    <div className="flex flex-col justify-center items-center flex-1 px-4 py-20">
      {/* Hero Section */}
      <div className="w-full max-w-3xl text-center space-y-6">
        {/* Badge */}
        <div className="inline-flex items-center rounded-full px-4 py-1.5 bg-gradient-to-r from-blue-500/10 to-purple-500/10 border border-blue-500/20">
          <span className="text-sm font-medium bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
            ✨ Comprehensive LeetCode Solutions
          </span>
        </div>

        {/* Main Heading */}
        <h1 className="text-5xl sm:text-6xl font-bold text-foreground leading-tight">
          Master Coding Interviews
        </h1>

        {/* Description */}
        <p className="text-lg sm:text-xl text-muted-foreground max-w-2xl mx-auto">
          A curated collection of LeetCode problem solutions with detailed explanations, optimal approaches, and time/space complexity analysis.
        </p>

        {/* CTA Buttons */}
        <div className="flex flex-col sm:flex-row gap-4 justify-center pt-4">
          <Link
            href="/docs"
            className="px-8 py-3 rounded-lg bg-blue-600 text-white font-medium hover:bg-blue-700 transition-colors duration-200 shadow-lg hover:shadow-xl inline-flex items-center gap-2"
          >
            Explore Solutions
            <span>→</span>
          </Link>
          <a
            href="https://github.com/LingC2001/leetcode-solutions"
            target="_blank"
            rel="noopener noreferrer"
            className="px-8 py-3 rounded-lg border border-foreground/20 text-foreground font-medium hover:bg-foreground/5 transition-colors duration-200"
          >
            Browse GitHub
          </a>
        </div>

        {/* Stats */}
        <div className="pt-8 grid grid-cols-3 gap-8 border-t border-foreground/10">
          <div>
            <div className="text-3xl font-bold text-foreground">200+</div>
            <p className="text-sm text-muted-foreground mt-1">Problems Solved</p>
          </div>
          <div>
            <div className="text-3xl font-bold text-foreground">3</div>
            <p className="text-sm text-muted-foreground mt-1">Difficulty Levels</p>
          </div>
          <div>
            <div className="text-3xl font-bold text-foreground">1k+</div>
            <p className="text-sm text-muted-foreground mt-1">Code Examples</p>
          </div>
        </div>
      </div>
    </div>
  );
}
