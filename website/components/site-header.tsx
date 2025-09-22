import Link from "next/link";
import Image from "next/image";

export function SiteHeader() {
  return (
    <header className="bg-[var(--header-background)] py-4 px-4 border-b border-border">
      <div className="container mx-auto max-w-4xl">
        <Link href="/">
          <Image
            alt="dracoboost's Blog"
            className="h-10 w-auto"
            height={94}
            src="/images/logos/dracoboost-blog-logo.png"
            width={504}
          />
        </Link>
      </div>
    </header>
  );
}
