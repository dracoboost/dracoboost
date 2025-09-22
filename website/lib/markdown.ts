import { readFileSync, readdirSync } from "fs";
import { join } from "path";
import matter from "gray-matter";

export interface PostData {
  slug: string;
  title: string;
  date: string;
  thumbnail?: string;
  [key: string]: any; // Allow for other front matter properties
}

export async function parseMarkdown(filePath: string) {
  const fileContents = readFileSync(filePath, "utf8");

  // Use gray-matter to parse the post metadata section
  const matterResult = matter(fileContents);

  // Return the raw content and data
  return {
    content: matterResult.content,
    data: matterResult.data as Omit<PostData, "slug">,
  };
}

export function getSortedPostsData(): PostData[] {
  const postsDirectory = join(process.cwd(), "content");
  const fileNames = readdirSync(postsDirectory, { withFileTypes: true })
    .filter((dirent) => dirent.isFile() && dirent.name.endsWith(".md"))
    .map((dirent) => dirent.name);

  const allPostsData = fileNames.map((fileName) => {
    // Remove ".md" from file name to get id
    const slug = fileName.replace(/\.md$/, "");

    // Read markdown file as string
    const fullPath = join(postsDirectory, fileName);
    const fileContents = readFileSync(fullPath, "utf8");

    // Use gray-matter to parse the post metadata section
    const matterResult = matter(fileContents);

    const { title, date, thumbnail } = matterResult.data as {
      title: string;
      date: string;
      thumbnail?: string;
    };

    // Combine the data with the id
    return {
      slug,
      title,
      date,
      thumbnail,
    };
  });

  // Sort posts by date
  return allPostsData.sort((a, b) => {
    if (a.date < b.date) {
      return 1;
    } else {
      return -1;
    }
  });
}
