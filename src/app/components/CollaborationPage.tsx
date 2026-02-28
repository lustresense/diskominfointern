import { useState } from "react";
import { ArrowLeft, CheckCircle2 } from "lucide-react";
import { apiBaseUrl } from "/utils/supabase/info";
import { Button } from "@/app/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/app/components/ui/card";
import { Input } from "@/app/components/ui/input";
import { Label } from "@/app/components/ui/label";
import { Textarea } from "@/app/components/ui/textarea";
import { toast } from "sonner";

interface CollaborationPageProps {
  onNavigate: (page: "landing" | "login") => void;
}

const supportOptions = [
  { value: "dana", label: "Dana" },
  { value: "konsumsi", label: "Konsumsi" },
  { value: "peralatan", label: "Peralatan" },
  { value: "media_partner", label: "Media partner" },
  { value: "lainnya", label: "Lainnya" },
];

export function CollaborationPage({ onNavigate }: CollaborationPageProps) {
  const [submitting, setSubmitting] = useState(false);
  const [submitted, setSubmitted] = useState(false);
  const [form, setForm] = useState({
    organizationName: "",
    picName: "",
    email: "",
    supportType: "dana",
    supportDescription: "",
  });

  const submit = async (e: React.FormEvent) => {
    e.preventDefault();
    setSubmitting(true);
    try {
      const response = await fetch(`${apiBaseUrl}/collaboration-requests`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(form),
      });
      const data = await response.json();
      if (!response.ok || !data.success) {
        throw new Error(data.error || "Gagal kirim kolaborasi");
      }
      setSubmitted(true);
      toast.success("Permintaan kolaborasi terkirim");
    } catch (error: any) {
      toast.error(error.message || "Terjadi kesalahan");
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <div className="min-h-screen bg-[#f6f8f5] px-4 py-6 text-[#17231d]">
      <div className="mx-auto max-w-3xl">
        <button
          type="button"
          onClick={() => onNavigate("landing")}
          className="mb-5 inline-flex items-center gap-2 text-sm font-medium text-[#335046] hover:text-[#0f5f3f]"
        >
          <ArrowLeft className="h-4 w-4" />
          Kembali ke Landing
        </button>

        <Card className="rounded-2xl border-[#d8e2db] bg-white shadow-sm">
          <CardHeader>
            <CardTitle className="text-2xl font-semibold text-[#132019]">Ajukan Kolaborasi</CardTitle>
            <CardDescription className="text-[#506057]">
              Submit akan masuk sebagai <strong>collaboration_request</strong>, lalu diproses oleh Moderator Tier 2
              (Kelurahan/Kecamatan).
            </CardDescription>
          </CardHeader>
          <CardContent>
            {submitted ? (
              <div className="rounded-xl border border-[#cde5d5] bg-[#f2faf4] p-5">
                <div className="flex items-start gap-3">
                  <CheckCircle2 className="mt-0.5 h-5 w-5 text-[#0f8a53]" />
                  <div>
                    <p className="font-semibold text-[#164d33]">Permintaan kolaborasi sudah masuk.</p>
                    <p className="mt-1 text-sm text-[#355746]">
                      Tim kelurahan akan meninjau permintaan dan menghubungi PIC melalui email.
                    </p>
                  </div>
                </div>
                <div className="mt-4 flex flex-wrap gap-2">
                  <Button
                    type="button"
                    onClick={() => onNavigate("login")}
                    className="rounded-full bg-[#0f5f3f] text-white hover:bg-[#0d5035]"
                  >
                    Masuk ke Sistem
                  </Button>
                  <Button type="button" variant="outline" onClick={() => onNavigate("landing")} className="rounded-full">
                    Kembali Landing
                  </Button>
                </div>
              </div>
            ) : (
              <form onSubmit={submit} className="space-y-4">
                <div className="space-y-2">
                  <Label htmlFor="organizationName">Nama organisasi</Label>
                  <Input
                    id="organizationName"
                    value={form.organizationName}
                    onChange={(e) => setForm((prev) => ({ ...prev, organizationName: e.target.value }))}
                    placeholder="Contoh: Komunitas Peduli Surabaya"
                    required
                  />
                </div>
                <div className="space-y-2">
                  <Label htmlFor="picName">Nama PIC</Label>
                  <Input
                    id="picName"
                    value={form.picName}
                    onChange={(e) => setForm((prev) => ({ ...prev, picName: e.target.value }))}
                    placeholder="Nama penanggung jawab"
                    required
                  />
                </div>
                <div className="space-y-2">
                  <Label htmlFor="email">Email</Label>
                  <Input
                    id="email"
                    type="email"
                    value={form.email}
                    onChange={(e) => setForm((prev) => ({ ...prev, email: e.target.value }))}
                    placeholder="pic@organisasi.id"
                    required
                  />
                </div>
                <div className="space-y-2">
                  <Label htmlFor="supportType">Jenis dukungan</Label>
                  <select
                    id="supportType"
                    value={form.supportType}
                    onChange={(e) => setForm((prev) => ({ ...prev, supportType: e.target.value }))}
                    className="h-10 w-full rounded-md border border-input bg-transparent px-3 py-2 text-sm shadow-xs"
                    required
                  >
                    {supportOptions.map((option) => (
                      <option key={option.value} value={option.value}>
                        {option.label}
                      </option>
                    ))}
                  </select>
                </div>
                <div className="space-y-2">
                  <Label htmlFor="supportDescription">Deskripsi singkat dukungan</Label>
                  <Textarea
                    id="supportDescription"
                    value={form.supportDescription}
                    onChange={(e) => setForm((prev) => ({ ...prev, supportDescription: e.target.value }))}
                    placeholder="Jelaskan bentuk kontribusi yang bisa diberikan"
                    rows={5}
                    required
                  />
                </div>
                <Button
                  type="submit"
                  disabled={submitting}
                  className="w-full rounded-full bg-[#FFC107] text-[#1f1f1f] hover:bg-[#ffd34d]"
                >
                  {submitting ? "Mengirim..." : "Submit"}
                </Button>
              </form>
            )}
          </CardContent>
        </Card>
      </div>
    </div>
  );
}
