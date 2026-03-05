import type { ReactNode } from "react";

interface SidebarProps {
  children: ReactNode;
}

export function Sidebar({ children }: SidebarProps) {
  return <aside className="w-full rounded-2xl border border-slate-200 bg-white p-4 lg:w-72">{children}</aside>;
}
