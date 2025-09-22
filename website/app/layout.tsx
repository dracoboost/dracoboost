import type { Metadata } from "next";
import { GeistSans } from "geist/font/sans";
import { GeistMono } from "geist/font/mono";
import { Analytics } from "@vercel/analytics/next";
import { ThemeProvider } from "next-themes";
import { SiteHeader } from "@/components/site-header";
import "./globals.css";

export const metadata: Metadata = {
  metadataBase: new URL("https://draco.moe"),
  title: "dracoboost's Blog",
  description: "Created with Next.js",
  generator: "Next.js",
  openGraph: {
    images: ["/images/og/dracoboost-og-1200x630.png"],
  },
  twitter: {
    images: ["/images/og/dracoboost-og-1200x600.png"],
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html suppressHydrationWarning lang="en">
      <body className={`font-sans ${GeistSans.variable} ${GeistMono.variable}`}>
        <ThemeProvider
          disableTransitionOnChange
          enableSystem
          attribute="class"
          defaultTheme="system"
        >
          <SiteHeader />
          {children}
        </ThemeProvider>
        <Analytics />
      </body>
    </html>
  );
}
