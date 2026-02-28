import { useEffect, useState } from "react";
import { AnimatePresence, motion } from "framer-motion";
import { Menu, ArrowRight, LogIn } from "lucide-react";
import type { LandingNavigatePage } from "@/app/components/landing/types";

interface CenteredLogoNavProps {
  onNavigate: (page: LandingNavigatePage) => void;
  onHomeClick: () => void;
}

const containerSpring = {
  type: "spring",
  stiffness: 400,
  damping: 30,
  mass: 1,
} as const;

const menuVariants = {
  hidden: { opacity: 0, transition: { when: "afterChildren" } },
  visible: {
    opacity: 1,
    transition: {
      delayChildren: 0.14,
      staggerChildren: 0.05,
    },
  },
} as const;

const itemVariants = {
  hidden: { opacity: 0, y: 10 },
  visible: { opacity: 1, y: 0 },
} as const;

export function CenteredLogoNav({ onNavigate, onHomeClick }: CenteredLogoNavProps) {
  const [open, setOpen] = useState(false);
  const [isMobile, setIsMobile] = useState(false);

  useEffect(() => {
    const handleResize = () => setIsMobile(window.innerWidth < 768);
    handleResize();
    window.addEventListener("resize", handleResize);
    return () => window.removeEventListener("resize", handleResize);
  }, []);

  const openNav = () => setOpen(true);
  const closeNav = () => setOpen(false);
  const go = (page: LandingNavigatePage) => {
    closeNav();
    onNavigate(page);
  };

  return (
    <>
      <AnimatePresence>
        {open && (
          <motion.button
            type="button"
            key="nav-overlay"
            onClick={closeNav}
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            transition={{ duration: 0.22 }}
            className="fixed inset-0 z-40 bg-black/22 backdrop-blur-[6px]"
            aria-label="Tutup menu"
          />
        )}
      </AnimatePresence>

      <header className="fixed left-0 right-0 top-4 z-50 px-4">
        <div className="mx-auto flex max-w-6xl justify-center">
          <motion.div
            layout
            transition={containerSpring}
            animate={{ borderRadius: open ? 22 : 999 }}
            className={[
              "border border-[#0f5f3f]/25 bg-white/92 shadow-[0_10px_24px_rgba(8,33,23,0.14)] backdrop-blur",
              open ? "w-[min(960px,calc(100vw-2rem))] px-4 py-4 md:px-5 md:py-4" : "w-[296px] px-3 py-2",
            ].join(" ")}
          >
            {!open ? (
              <div className="flex items-center justify-between gap-2">
                <button
                  type="button"
                  onClick={onHomeClick}
                  className="flex h-9 w-9 items-center justify-center rounded-full bg-[#0f5f3f] text-xs font-semibold text-[#FFC107]"
                  aria-label="Kembali ke atas"
                >
                  SR
                </button>
                <button
                  type="button"
                  onClick={onHomeClick}
                  className="text-sm font-semibold tracking-[0.12em] text-[#0f5f3f]"
                  aria-label="SIMRP"
                >
                  SIMRP
                </button>
                <button
                  type="button"
                  onClick={openNav}
                  className="grid h-9 w-9 place-items-center rounded-full border border-[#d4ddd7] text-[#173127] transition hover:bg-[#eef4f0]"
                  aria-label="Buka menu"
                >
                  <Menu className="h-4 w-4" />
                </button>
              </div>
            ) : (
              <motion.div layout className="space-y-4">
                <div className="flex items-center justify-between">
                  <button
                    type="button"
                    onClick={onHomeClick}
                    className="flex items-center gap-2 text-[#0f5f3f]"
                    aria-label="Kembali ke landing"
                  >
                    <span className="grid h-8 w-8 place-items-center rounded-full bg-[#0f5f3f] text-xs font-semibold text-[#FFC107]">SR</span>
                    <span className="text-sm font-semibold tracking-[0.12em]">SIMRP</span>
                  </button>
                  <button
                    type="button"
                    onClick={closeNav}
                    className="rounded-full border border-[#d5ded8] px-3 py-1 text-xs font-semibold text-[#1f3329] transition hover:bg-[#edf4ef]"
                  >
                    Tutup
                  </button>
                </div>

                <motion.div variants={menuVariants} initial="hidden" animate="visible" exit="hidden">
                  <motion.nav
                    variants={menuVariants}
                    className={isMobile ? "grid gap-2" : "flex flex-wrap items-center gap-3"}
                  >
                    <motion.button
                      variants={itemVariants}
                      type="button"
                      onClick={() => go("login")}
                      className="rounded-xl border border-[#d7e1db] bg-white px-4 py-2 text-sm font-medium text-[#1b2f25] transition hover:bg-[#f0f6f2]"
                    >
                      Masuk
                    </motion.button>
                    <motion.button
                      variants={itemVariants}
                      type="button"
                      onClick={() => go("about")}
                      className="rounded-xl border border-[#d7e1db] bg-white px-4 py-2 text-sm font-medium text-[#1b2f25] transition hover:bg-[#f0f6f2]"
                    >
                      About
                    </motion.button>
                    <motion.button
                      variants={itemVariants}
                      type="button"
                      onClick={() => go("faq")}
                      className="rounded-xl border border-[#d7e1db] bg-white px-4 py-2 text-sm font-medium text-[#1b2f25] transition hover:bg-[#f0f6f2]"
                    >
                      FAQ
                    </motion.button>
                  </motion.nav>

                  <motion.div
                    variants={menuVariants}
                    className={isMobile ? "mt-3 grid grid-cols-1 gap-2" : "mt-3 flex flex-wrap items-center gap-2"}
                  >
                    <motion.button
                      variants={itemVariants}
                      type="button"
                      onClick={() => go("collaboration")}
                      className="inline-flex items-center justify-center gap-2 rounded-xl bg-[#FFC107] px-4 py-2 text-sm font-semibold text-[#182117] transition hover:bg-[#ffd347]"
                    >
                      Jadi Mitra
                      <ArrowRight className="h-4 w-4" />
                    </motion.button>
                    <motion.button
                      variants={itemVariants}
                      type="button"
                      onClick={() => go("login")}
                      className="inline-flex items-center justify-center gap-2 rounded-xl border border-[#d7e1db] bg-white px-4 py-2 text-sm font-medium text-[#1b2f25] transition hover:bg-[#f0f6f2]"
                    >
                      Jadi Relawan
                      <LogIn className="h-4 w-4" />
                    </motion.button>
                  </motion.div>
                </motion.div>
              </motion.div>
            )}
          </motion.div>
        </div>
      </header>
    </>
  );
}
