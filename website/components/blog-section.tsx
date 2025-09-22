import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { getSortedPostsData } from "../lib/markdown";
import Link from "next/link";
import Image from "next/image";

export function BlogSection() {
  const allPostsData = getSortedPostsData();

  return (
    <section className="py-20 px-4 bg-[var(--main-background)]">
      <div className="container mx-auto max-w-4xl">
        <h2 className="text-3xl font-bold text-center mb-12 text-balance">
          Latest Blog Posts
        </h2>
        <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
          {allPostsData.map(({ slug, date, title, thumbnail }) => (
            <Card
              key={slug}
              className="bg-[var(--main-background)] hover:shadow-lg transition-shadow"
            >
              <CardHeader>
                {thumbnail && (
                  <Link href={`/blog/${slug}`}>
                    <Image
                      alt={title}
                      className="mb-4 rounded-lg"
                      height={600}
                      src={thumbnail}
                      width={1200}
                    />
                  </Link>
                )}
                <CardTitle>
                  <Link href={`/blog/${slug}`}>{title}</Link>
                </CardTitle>
              </CardHeader>
              <CardContent>
                <p className="text-muted-foreground text-sm">{date}</p>
              </CardContent>
            </Card>
          ))}
        </div>
      </div>
    </section>
  );
}
