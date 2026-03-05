import type { Event } from "@/types/event";
import { Card, CardContent, CardHeader, CardTitle } from "@/app/components/ui/card";
import { StatusBadge } from "@/components/shared/StatusBadge";

export function EventCard({ event }: { event: Event }) {
  return (
    <Card>
      <CardHeader className="pb-2">
        <CardTitle className="text-base">{event.title}</CardTitle>
      </CardHeader>
      <CardContent className="space-y-2 text-sm text-slate-600">
        <p>{event.description}</p>
        <div className="flex items-center justify-between">
          <span>{event.kelurahan || event.kecamatan || "-"}</span>
          <StatusBadge status={event.status} />
        </div>
      </CardContent>
    </Card>
  );
}
