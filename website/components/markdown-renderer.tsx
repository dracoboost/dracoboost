"use client";

import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { Lightbox } from "@/components/ui/lightbox";

interface MarkdownRendererProps {
  content: string;
}

export function MarkdownRenderer({ content }: MarkdownRendererProps) {
  return (
    <div className="prose dark:prose-invert max-w-none">
      <ReactMarkdown
        components={{
          img: ({ src, alt }) => {
            if (!src) return null;
            return <Lightbox alt={alt || ""} src={src} />;
          },
        }}
        remarkPlugins={[remarkGfm]}
      >
        {content}
      </ReactMarkdown>
    </div>
  );
}
