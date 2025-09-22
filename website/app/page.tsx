import { ProfileSection } from "@/components/profile-section";
import { ProjectsSection } from "@/components/projects-section";
import { SiteFooter } from "@/components/site-footer";
import { BlogSection } from "@/components/blog-section";

export default function ProfilePage() {
  return (
    <main className="min-h-screen bg-[var(--main-background)]">
      <ProfileSection />
      <ProjectsSection />
      <BlogSection />
      <SiteFooter />
    </main>
  );
}
