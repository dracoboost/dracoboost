import Image from "next/image";

export function ProfileSection() {
  return (
    <section className="relative border-b border-border">
      <div className="absolute inset-0 bg-[url('/images/headers/maliss.png')] bg-cover bg-center brightness-75" />
      <div className="relative container mx-auto max-w-4xl text-center py-20 px-4">
        <div className="mb-8">
          <Image
            alt="dracoboost"
            className="mx-auto rounded-full border-4 border-primary/20 shadow-lg"
            height={200}
            src="/images/avatars/dracoboost.png"
            width={200}
          />
        </div>

        <h1 className="text-5xl font-bold text-foreground mb-4 text-balance">
          dracoboost
        </h1>

        <div className="flex gap-4 justify-center">
          <a
            href="https://x.com/dracoboost"
            rel="noopener noreferrer"
            target="_blank"
          >
            <Image
              alt="X"
              height={20}
              src="https://img.shields.io/badge/@dracoboost-222222?logo=x"
              width={100}
            />
            <span className="sr-only">X</span>
          </a>
          <a
            href="https://github.com/dracoboost"
            rel="noopener noreferrer"
            target="_blank"
          >
            <Image
              alt="GitHub"
              height={20}
              src="https://img.shields.io/badge/@dracoboost-262c36?logo=github"
              width={100}
            />
            <span className="sr-only">GitHub</span>
          </a>
        </div>
      </div>
    </section>
  );
}
