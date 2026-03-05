import { Badge } from "@/components/ui/Badge";

export function StatusBadge({ status }: { status: string }) {
  const variant = status === "verified" || status === "published" ? "default" : "outline";
  return <Badge variant={variant as any}>{status}</Badge>;
}
