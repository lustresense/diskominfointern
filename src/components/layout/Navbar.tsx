import type { ReactNode } from "react";

interface NavbarProps {
  left?: ReactNode;
  center?: ReactNode;
  right?: ReactNode;
}

export function Navbar({ left, center, right }: NavbarProps) {
  return (
    <header className="sticky top-0 z-30 border-b border-slate-200 bg-white/95 backdrop-blur">
      <div className="mx-auto flex h-14 w-full max-w-7xl items-center justify-between px-4">
        <div>{left}</div>
        <div>{center}</div>
        <div>{right}</div>
      </div>
    </header>
  );
}
