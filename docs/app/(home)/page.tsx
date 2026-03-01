import Link from "next/link";

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
          Learn Algorithms<br></br>and Data Structures
        </h1>

        {/* Description */}
        <p className="text-base sm:text-lg text-gray-500 dark:text-gray-400 max-w-2xl mx-auto">
          A curated collection of LeetCode problem and solutions<br></br>
          with detailed explanations, optimal approaches and<br></br>
          time/space complexity analysis.
        </p>

        {/* CTA Buttons */}
        <div className="flex flex-col sm:flex-row gap-4 justify-center pt-4">
          <Link
            href="/docs"
            className="px-6 py-2 rounded-lg bg-blue-600 text-white font-medium hover:bg-blue-700 transition-colors duration-200 shadow-lg hover:shadow-xl inline-flex items-center justify-center gap-2"
          >
            Explore Solutions
            <span>→</span>
          </Link>
          <a
            href="https://github.com/LingC2001/leetcode-solutions"
            target="_blank"
            rel="noopener noreferrer"
            className="px-6 py-2 rounded-lg border border-blue-600/30 text-blue-600 font-medium hover:bg-blue-600/10 transition-colors duration-200 inline-flex items-center justify-center"
          >
            Browse GitHub
          </a>
        </div>
      </div>
    </div>
  );
}
