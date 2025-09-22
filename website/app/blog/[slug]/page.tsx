import { notFound } from "next/navigation";
import { parseMarkdown } from "@/lib/markdown";
import fs from "fs";
import path from "path";
import { SiteFooter } from "@/components/site-footer";
import Image from "next/image";
import { MarkdownRenderer } from "@/components/markdown-renderer";

interface BlogPostPageProps {
  params: { slug: string };
}

export default async function BlogPostPage({ params }: BlogPostPageProps) {
  const { slug } = params;
  const filePath = path.join(process.cwd(), "content", `${slug}.md`);

  if (!fs.existsSync(filePath)) {
    notFound();
  }

  const { content, data } = await parseMarkdown(filePath);

  return (
    <>
      {data.thumbnail && (
        <div className="container mx-auto max-w-5xl px-4">
          <Image
            alt={data.title}
            className="mb-8 rounded-lg"
            height={600}
            src={data.thumbnail}
            width={1200}
          />
        </div>
      )}
      <article className="container mx-auto max-w-4xl py-12 px-4">
        <h1 className="text-4xl font-bold mb-4">{data.title}</h1>
        <p className="text-muted-foreground mb-8">{data.date}</p>
        <MarkdownRenderer content={content} />
      </article>
      <SiteFooter />
    </>
  );
}

export async function generateStaticParams() {
  const postsDirectory = path.join(process.cwd(), "content");
  const filenames = fs.readdirSync(postsDirectory);

  return filenames.map((filename) => ({
    slug: filename.replace(/\.md$/, ""),
  }));
}
