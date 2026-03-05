import { useEffect, useState } from "react";
import * as reportsApi from "@/api/reports";

export function useReports(token?: string | null) {
  const [reports, setReports] = useState<any[]>([]);

  async function refresh(params: { status?: string; userId?: string } = {}) {
    const data: any = await reportsApi.getReports(params, token);
    setReports(data?.reports || []);
    return data;
  }

  useEffect(() => {
    void refresh();
  }, []);

  return {
    reports,
    refresh,
    createReport: (payload: unknown) => reportsApi.createReport(payload, token),
    verifyReport: (reportId: string, approved: boolean) => reportsApi.verifyReport(reportId, approved, token),
  };
}
