import Image from "next/image";

export function SiteFooter() {
  return (
    <footer className="bg-[var(--footer-background)] py-12 px-4 border-t border-border">
      <div className="container mx-auto max-w-3xl">
        <div className="flex flex-col md:flex-row justify-between items-center gap-6">
          <div className="flex items-center gap-2 text-center md:text-left">
            <Image
              alt="dracoboost's Blog"
              className="h-10 w-auto"
              height={94}
              src="/images/logos/dracoboost-blog-logo.png"
              width={504}
            />
            <p className="text-muted-foreground">© 2025 dracoboost.</p>
          </div>

          <div className="flex gap-4">
            <a
              className="text-muted-foreground hover:text-primary transition-colors"
              href="https://x.com/dracoboost"
              rel="noopener noreferrer"
              target="_blank"
            >
              <Image
                alt="X"
                className="w-6 h-6"
                height={20}
                src="/images/icons/x.svg"
                width={20}
              />
              <span className="sr-only">X</span>
            </a>

            <a
              className="text-muted-foreground hover:text-primary transition-colors"
              href="https://github.com/dracoboost"
              rel="noopener noreferrer"
              target="_blank"
            >
              <Image
                alt="GitHub"
                className="w-6 h-6"
                height={20}
                src="/images/icons/github.svg"
                width={20}
              />
              <span className="sr-only">GitHub</span>
            </a>
          </div>
        </div>
      </div>
    </footer>
  );
}
