import { Inter } from "next/font/google";
import { Provider } from "@/components/provider";
import "./global.css";

const basePath = process.env.NEXT_PUBLIC_BASE_PATH ?? "";

const inter = Inter({
  subsets: ["latin"],
});

export const metadata = {
  icons: {
    icon: `${basePath}/favicon.ico`,
  },
};

export default function Layout({ children }: LayoutProps<"/">) {
  return (
    <html lang="en" className={inter.className} suppressHydrationWarning>
      <body className="flex flex-col min-h-screen">
        <Provider>{children}</Provider>
      </body>
    </html>
  );
}
