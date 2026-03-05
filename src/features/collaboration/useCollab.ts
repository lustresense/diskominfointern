import { useState } from "react";
import * as collabApi from "@/api/collab";

export function useCollab(token?: string | null) {
  const [requests, setRequests] = useState<any[]>([]);

  async function refresh(status?: string) {
    const data: any = await collabApi.getCollabRequests(status, token);
    setRequests(data?.requests || []);
    return data;
  }

  return {
    requests,
    refresh,
    createCollab: collabApi.createCollab,
    approveCollab: (requestId: string, approved: boolean) => collabApi.approveCollab(requestId, approved, token),
  };
}
