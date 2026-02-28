import { useEffect, useRef, useState } from "react";
import { ChevronDown } from "lucide-react";
import { Button } from "@/app/components/ui/button";

interface HeroSectionProps {
  onExplore: () => void;
}

function clamp(value: number, min: number, max: number) {
  return Math.max(min, Math.min(max, value));
}

export function HeroSection({ onExplore }: HeroSectionProps) {
  const sectionRef = useRef<HTMLElement | null>(null);
  const [progress, setProgress] = useState(0);

  useEffect(() => {
    let raf = 0;
    const onScroll = () => {
      cancelAnimationFrame(raf);
      raf = requestAnimationFrame(() => {
        const section = sectionRef.current;
        if (!section) {
          return;
        }
        const rect = section.getBoundingClientRect();
        const viewport = window.innerHeight;
        const total = Math.max(section.offsetHeight - viewport, 1);
        const raw = -rect.top / total;
        setProgress(clamp(raw, 0, 1));
      });
    };

    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    window.addEventListener("resize", onScroll);
    return () => {
      window.removeEventListener("scroll", onScroll);
      window.removeEventListener("resize", onScroll);
      cancelAnimationFrame(raf);
    };
  }, []);

  const inset = progress * 6.5;
  const radius = progress * 34;
  const shadow = progress * 0.2;

  return (
    <section ref={sectionRef} className="relative h-[165vh]">
      <div className="sticky top-0 h-screen overflow-hidden">
        <div
          className="h-full w-full transition-[clip-path,box-shadow] duration-100"
          style={{
            clipPath: `inset(${inset}% ${inset}% ${inset}% ${inset}% round ${radius}px)`,
            boxShadow: `0 28px 55px rgba(7, 27, 19, ${shadow})`,
            background:
              "radial-gradient(circle at 15% 20%, rgba(255,193,7,0.16) 0 20%, transparent 21%), radial-gradient(circle at 82% 14%, rgba(255,193,7,0.12) 0 16%, transparent 17%), linear-gradient(136deg, #0a4d34 0%, #0d6341 55%, #0b5539 100%)",
          }}
        >
          <div
            className="h-full w-full"
            style={{
              backgroundImage:
                "linear-gradient(90deg, rgba(4,35,23,0.22) 1px, transparent 1px), linear-gradient(rgba(4,35,23,0.22) 1px, transparent 1px)",
              backgroundSize: "56px 56px",
            }}
          >
            <div className="mx-auto flex h-full w-full max-w-6xl items-center px-6 md:px-10">
              <div className="max-w-4xl text-white">
                <h1 className="text-5xl font-semibold leading-[1.06] tracking-tight text-white md:text-7xl">
                  Mewujudkan Kampung yang Seimbang dan Mandiri
                </h1>
                <p className="mt-6 max-w-3xl text-lg leading-relaxed text-white/92 md:text-2xl">
                  Program kampung berbasis partisipasi warga dengan empat pilar utama: Lingkungan, Ekonomi, Sosial Budaya,
                  dan Kemasyarakatan.
                </p>
                <div className="mt-8 flex flex-wrap gap-2 text-sm">
                  <span className="rounded-full border border-white/30 bg-white/12 px-4 py-1.5">153 Kelurahan</span>
                  <span className="rounded-full border border-white/30 bg-white/12 px-4 py-1.5">1.360 RW</span>
                  <span className="rounded-full border border-white/30 bg-white/12 px-4 py-1.5">Kampung-Centric</span>
                </div>
                <Button
                  type="button"
                  onClick={onExplore}
                  className="mt-9 h-12 rounded-full bg-[#FFC107] px-8 text-base font-semibold text-[#1a1a1a] transition hover:bg-[#ffd347]"
                >
                  Jelajahi Program
                </Button>
              </div>
            </div>
          </div>
        </div>

        <div
          className="pointer-events-none absolute bottom-8 left-1/2 -translate-x-1/2 text-center text-white transition-opacity duration-300"
          style={{ opacity: progress > 0.78 ? 0 : 1 }}
        >
          <p className="text-xs font-medium tracking-[0.14em] uppercase text-white/82">Scroll</p>
          <ChevronDown className="mx-auto mt-1 h-5 w-5 animate-bounce text-white/86" />
        </div>
      </div>
    </section>
  );
}
