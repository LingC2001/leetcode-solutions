import { getDashboardData } from "@/lib/dashboard-data";
import { DashboardClient } from "@/components/DashboardClient";

export const metadata = {
  title: "Dashboard – LeetCode Solutions",
  description: "Visual overview of solved LeetCode problems by difficulty, category, and tags.",
};

export default function DashboardPage() {
  const data = getDashboardData();

  return (
    <main className="px-4 py-10">
      <DashboardClient data={data} />
    </main>
  );
}
