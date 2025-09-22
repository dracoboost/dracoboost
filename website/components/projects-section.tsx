import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Github } from "lucide-react";
import Image from "next/image";

export function ProjectsSection() {
  const projects = [
    {
      title: "HoHatch",
      description:
        "A desktop tool for converting and managing JPG/DDS images to streamline modding for Shadowverse: Worlds Beyond with Special K.",
      technologies: ["Image Converter", "Shadowverse", "Modding Tool"],
      githubUrl: "https://github.com/dracoboost/hohatch",
      liveUrl: "https://hohatch.draco.moe",
      image: "/images/hohatch/hohatch-og-1200x600.png",
    },
  ];

  return (
    <section className="py-20 px-4 bg-[var(--main-background)]">
      <div className="container mx-auto max-w-6xl">
        <h2 className="text-3xl font-bold text-center mb-12 text-balance">
          Featured Projects
        </h2>

        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
          {projects.map((project, index) => (
            <Card
              key={index}
              className="flex flex-col h-full bg-[var(--main-background)] hover:shadow-lg transition-shadow"
            >
              <a
                href={project.liveUrl}
                rel="noopener noreferrer"
                target="_blank"
              >
                <CardHeader>
                  {project.image && (
                    <Image
                      alt={project.title}
                      className="mb-4 rounded-lg"
                      height={600}
                      src={project.image}
                      width={1200}
                    />
                  )}
                  <CardTitle className="text-xl">{project.title}</CardTitle>
                </CardHeader>
              </a>
              <CardDescription className="px-6 pb-6 text-pretty">
                {project.description}
              </CardDescription>

              <CardContent className="flex-1 flex flex-col">
                <div className="flex flex-wrap gap-2 mb-6">
                  {project.technologies.map((tech) => (
                    <Badge key={tech} className="text-xs" variant="secondary">
                      {tech}
                    </Badge>
                  ))}
                </div>

                <div className="flex gap-3 mt-auto">
                  <Button asChild size="sm" variant="outline">
                    <a
                      className="flex items-center gap-2"
                      href={project.githubUrl}
                    >
                      <Github className="w-4 h-4" />
                      Code
                    </a>
                  </Button>
                </div>
              </CardContent>
            </Card>
          ))}
        </div>
      </div>
    </section>
  );
}
