import type { ReactNode } from "react";

interface PageWrapperProps {
  children: ReactNode;
  className?: string;
}

export function PageWrapper({ children, className = "" }: PageWrapperProps) {
  return <main className={`mx-auto w-full max-w-7xl px-4 ${className}`}>{children}</main>;
}
