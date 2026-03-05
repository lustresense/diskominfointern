import { useEffect, useState } from "react";
import * as eventsApi from "@/api/events";

export function useEvents(token?: string | null) {
  const [events, setEvents] = useState<any[]>([]);
  const [loading, setLoading] = useState(false);

  async function refresh(status?: string) {
    setLoading(true);
    try {
      const data: any = await eventsApi.getEvents(status, token);
      setEvents(data?.events || []);
      return data;
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    void refresh();
  }, []);

  return {
    events,
    loading,
    refresh,
    createEvent: (payload: unknown) => eventsApi.createEvent(payload, token),
    approveEvent: (eventId: string, approved: boolean) => eventsApi.approveEvent(eventId, approved, token),
    joinEvent: (eventId: string) => eventsApi.joinEvent(eventId, token),
    completeEvent: (eventId: string, outputSummary: string) => eventsApi.completeEvent(eventId, outputSummary, token),
  };
}
