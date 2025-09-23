import { promises as fs } from "fs";
import path from "path";

export const dynamic = "force-static";

async function getBlogSlugs() {
  const contentDir = path.join(process.cwd(), "content");
  try {
    const files = await fs.readdir(contentDir);
    const blogSlugs = await Promise.all(
      files
        .filter((file) => file.endsWith(".md"))
        .map(async (file) => {
          const filePath = path.join(contentDir, file);
          const fileContent = await fs.readFile(filePath, "utf8");
          if (fileContent.startsWith("---") && /date:/.test(fileContent)) {
            return file.replace(/\.md$/, "");
          }
          return null;
        }),
    );
    return blogSlugs.filter((slug): slug is string => slug !== null);
  } catch (error) {
    console.error(`Could not read content directory: ${contentDir}`, error);
    return [];
  }
}

export async function GET() {
  const baseUrl = "https://draco.moe";
  const lastmod = new Date().toISOString().split("T")[0];
  const slugs = await getBlogSlugs();

  const urls = [
    {
      loc: baseUrl,
      lastmod,
    },
    ...slugs.map((slug) => ({
      loc: `${baseUrl}/blog/${slug}`,
      lastmod,
    })),
  ];

  const sitemap = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  ${urls
    .map(
      (url) => `
  <url>
    <loc>${url.loc}</loc>
    <lastmod>${url.lastmod}</lastmod>
  </url>`,
    )
    .join("\n")}
</urlset>
  `;

  return new Response(sitemap.trim(), {
    headers: {
      "Content-Type": "application/xml",
    },
  });
}
