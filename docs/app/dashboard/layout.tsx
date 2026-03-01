import { HomeLayout } from "fumadocs-ui/layouts/home";
import { baseOptions } from "@/lib/layout.shared";

export default function DashboardLayout({ children }: LayoutProps<"/dashboard">) {
  return <HomeLayout {...baseOptions()}>{children}</HomeLayout>;
}
