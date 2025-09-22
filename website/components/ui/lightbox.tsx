"use client";

import { useState } from "react";
import { Dialog, DialogContent } from "@/components/ui/dialog";
import Image from "next/image";

interface LightboxProps {
  src: string;
  alt: string;
}

export function Lightbox({ src, alt }: LightboxProps) {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <>
      <Image
        alt={alt}
        className="cursor-pointer rounded-lg"
        height={600}
        src={src}
        width={1200}
        onClick={() => setIsOpen(true)}
      />
      <Dialog open={isOpen} onOpenChange={setIsOpen}>
        <DialogContent className="max-w-4xl p-0 border-0">
          <Image
            alt={alt}
            className="w-full h-auto rounded-lg"
            height={800}
            src={src}
            width={1600}
          />
        </DialogContent>
      </Dialog>
    </>
  );
}
