import { useEffect, useMemo, useState } from "react";
import { ArrowLeft, ArrowRight, CheckCircle2, Handshake, Home, Search, Sparkles } from "lucide-react";

import { geographicData } from "@/data/geographicData";
import { apiPublicGet, apiPublicPost } from "@/lib/api";
import { Button } from "@/app/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/app/components/ui/card";
import { Input } from "@/app/components/ui/input";
import { Label } from "@/app/components/ui/label";
import { Textarea } from "@/app/components/ui/textarea";
import { toast } from "sonner";

interface CollaborationPageProps {
  onNavigate: (page: "landing" | "login") => void;
}

interface CollaborationForm {
  organizationName: string;
  picName: string;
  email: string;
  supportType: "dana" | "konsumsi" | "peralatan" | "media_partner" | "lainnya";
  contributionScope: "kota" | "kecamatan" | "kelurahan";
  kecamatanId: string;
  kecamatanName: string;
  kelurahanId: string;
  kelurahanName: string;
  supportDescription: string;
}

interface GeoKelurahan {
  id: number;
  name: string;
  kodepos: string[];
}

interface GeoKecamatan {
  id: number;
  name: string;
  kelurahan: GeoKelurahan[];
}

interface LocalKelurahan {
  code: string;
  name: string;
}

interface LocalKecamatan {
  code: string;
  name: string;
  kelurahan: LocalKelurahan[];
}

interface KelurahanSuggestion {
  name: string;
  kecamatanName: string;
}

type FocusedGeoField = "kecamatan" | "kelurahan" | null;

const normalize = (value: string) => value.trim().toLowerCase().replace(/\s+/g, " ");

const supportOptions: Array<{ value: CollaborationForm["supportType"]; label: string }> = [
  { value: "dana", label: "Sponsorship & Pendanaan" },
  { value: "konsumsi", label: "Konsumsi" },
  { value: "peralatan", label: "Peralatan" },
  { value: "media_partner", label: "Media Partner" },
  { value: "lainnya", label: "Lainnya" },
];

const initialForm: CollaborationForm = {
  organizationName: "",
  picName: "",
  email: "",
  supportType: "dana",
  contributionScope: "kota",
  kecamatanId: "",
  kecamatanName: "",
  kelurahanId: "",
  kelurahanName: "",
  supportDescription: "",
};

export function CollaborationPage({ onNavigate }: CollaborationPageProps) {
  const [submitting, setSubmitting] = useState(false);
  const [form, setForm] = useState<CollaborationForm>(initialForm);
  const [geoOptions, setGeoOptions] = useState<GeoKecamatan[]>([]);
  const [focusedGeoField, setFocusedGeoField] = useState<FocusedGeoField>(null);
  const [receipt, setReceipt] = useState<{ requestId: string; submittedAt: string } | null>(null);

  const localGeoOptions = useMemo<LocalKecamatan[]>(
    () =>
      geographicData.kecamatan
        .map((kecamatan) => ({
          code: kecamatan.kode,
          name: kecamatan.nama,
          kelurahan: kecamatan.kelurahan.map((kelurahan) => ({
            code: kelurahan.kode,
            name: kelurahan.nama,
          })),
        }))
        .sort((a, b) => a.name.localeCompare(b.name, "id")),
    [],
  );

  const formattedDate = useMemo(() => {
    const source = receipt?.submittedAt ? new Date(receipt.submittedAt) : new Date();
    return source.toLocaleDateString("id-ID", { day: "numeric", month: "long", year: "numeric" });
  }, [receipt?.submittedAt]);

  const updateField = <K extends keyof CollaborationForm>(key: K, value: CollaborationForm[K]) => {
    setForm((prev) => ({ ...prev, [key]: value }));
  };

  const resolveApiIds = (kecamatanName: string, kelurahanName?: string) => {
    const apiKecamatan = geoOptions.find((item) => normalize(item.name) === normalize(kecamatanName));
    if (!apiKecamatan) {
      return { kecamatanId: "", kelurahanId: "" };
    }
    if (!kelurahanName) {
      return { kecamatanId: String(apiKecamatan.id), kelurahanId: "" };
    }
    const apiKelurahan = apiKecamatan.kelurahan.find((item) => normalize(item.name) === normalize(kelurahanName));
    return {
      kecamatanId: String(apiKecamatan.id),
      kelurahanId: apiKelurahan ? String(apiKelurahan.id) : "",
    };
  };

  const pickKecamatan = (rawName: string) => {
    const exact = localGeoOptions.find((item) => normalize(item.name) === normalize(rawName));
    const name = exact ? exact.name : rawName;
    const ids = resolveApiIds(name);
    setForm((prev) => ({
      ...prev,
      kecamatanName: name,
      kecamatanId: ids.kecamatanId,
      kelurahanName: "",
      kelurahanId: "",
    }));
  };

  const pickKelurahan = (suggestion: KelurahanSuggestion) => {
    const ids = resolveApiIds(suggestion.kecamatanName, suggestion.name);
    setForm((prev) => ({
      ...prev,
      kecamatanName: suggestion.kecamatanName,
      kecamatanId: ids.kecamatanId,
      kelurahanName: suggestion.name,
      kelurahanId: ids.kelurahanId,
    }));
  };

  const closeGeoSuggestions = () => {
    setTimeout(() => {
      const activeId = (document.activeElement as HTMLElement | null)?.id;
      if (activeId !== "collab-kecamatan" && activeId !== "collab-kelurahan") {
        setFocusedGeoField(null);
      }
    }, 120);
  };

  useEffect(() => {
    const loadGeo = async () => {
      try {
        const data = await apiPublicGet<{ kecamatan: GeoKecamatan[] }>("/geo/options");
        setGeoOptions(Array.isArray(data?.kecamatan) ? data.kecamatan : []);
      } catch {
        // Tetap gunakan geographicData.ts sebagai sumber pencarian nama.
      }
    };
    loadGeo();
  }, []);

  useEffect(() => {
    if (form.contributionScope === "kota") {
      setForm((prev) => ({
        ...prev,
        kecamatanId: "",
        kecamatanName: "",
        kelurahanId: "",
        kelurahanName: "",
      }));
      return;
    }
    if (form.contributionScope === "kecamatan") {
      setForm((prev) => ({ ...prev, kelurahanId: "", kelurahanName: "" }));
    }
  }, [form.contributionScope]);

  const selectedLocalKecamatan = useMemo(
    () => localGeoOptions.find((item) => normalize(item.name) === normalize(form.kecamatanName)) || null,
    [form.kecamatanName, localGeoOptions],
  );

  const kecamatanSuggestions = useMemo(() => {
    const query = normalize(form.kecamatanName);
    const rows = query
      ? localGeoOptions.filter((item) => normalize(item.name).includes(query))
      : localGeoOptions;
    return rows.slice(0, 50);
  }, [form.kecamatanName, localGeoOptions]);

  const kelurahanSuggestions = useMemo(() => {
    const query = normalize(form.kelurahanName);
    const rows: KelurahanSuggestion[] = [];

    if (selectedLocalKecamatan) {
      for (const kelurahan of selectedLocalKecamatan.kelurahan) {
        if (query && !normalize(kelurahan.name).includes(query)) {
          continue;
        }
        rows.push({ name: kelurahan.name, kecamatanName: selectedLocalKecamatan.name });
      }
      return rows.slice(0, 80);
    }

    const kecQuery = normalize(form.kecamatanName);
    for (const kecamatan of localGeoOptions) {
      if (kecQuery && !normalize(kecamatan.name).includes(kecQuery)) {
        continue;
      }
      for (const kelurahan of kecamatan.kelurahan) {
        if (query && !normalize(kelurahan.name).includes(query)) {
          continue;
        }
        rows.push({ name: kelurahan.name, kecamatanName: kecamatan.name });
      }
    }
    return rows.slice(0, 80);
  }, [form.kecamatanName, form.kelurahanName, localGeoOptions, selectedLocalKecamatan]);

  const submit = async (event: React.FormEvent) => {
    event.preventDefault();

    let matchedKecamatan: LocalKecamatan | null = null;
    if (form.contributionScope !== "kota") {
      matchedKecamatan =
        localGeoOptions.find((item) => normalize(item.name) === normalize(form.kecamatanName)) || null;
      if (!matchedKecamatan) {
        toast.error("Kecamatan tidak valid. Gunakan tombol Cari atau pilih dari daftar.");
        return;
      }
    }

    if (form.contributionScope === "kelurahan") {
      const matchedKelurahan = matchedKecamatan?.kelurahan.find(
        (item) => normalize(item.name) === normalize(form.kelurahanName),
      );
      if (!matchedKelurahan) {
        toast.error("Kelurahan tidak valid untuk kecamatan yang dipilih.");
        return;
      }
    }

    setSubmitting(true);
    try {
      const payload = {
        organizationName: form.organizationName,
        picName: form.picName,
        email: form.email,
        supportType: form.supportType,
        contributionScope: form.contributionScope,
        kecamatanId: form.kecamatanId ? Number(form.kecamatanId) : null,
        kelurahanId: form.kelurahanId ? Number(form.kelurahanId) : null,
        kecamatanName: form.kecamatanName.trim() || null,
        kelurahanName: form.kelurahanName.trim() || null,
        supportDescription: form.supportDescription,
      };
      const data = await apiPublicPost<any>("/collaboration-requests", payload);
      if (!data?.success) {
        throw new Error("Pengajuan kolaborasi gagal diproses");
      }
      const requestId = data?.request?.id || `REQ-${Date.now().toString().slice(-8)}`;
      setReceipt({ requestId, submittedAt: new Date().toISOString() });
      toast.success("Pengajuan kolaborasi berhasil dikirim");
    } catch (error: any) {
      toast.error(error.message || "Terjadi kesalahan saat mengirim pengajuan");
    } finally {
      setSubmitting(false);
    }
  };

  if (receipt) {
    return (
      <div className="relative min-h-screen overflow-hidden bg-[#f8faf9] px-4 py-8 text-slate-800">
        <div className="pointer-events-none absolute inset-0 bg-[radial-gradient(circle_at_15%_20%,rgba(21,87,56,0.08),transparent_42%),radial-gradient(circle_at_85%_85%,rgba(255,199,0,0.16),transparent_46%)]" />
        <main className="relative z-10 mx-auto flex min-h-[80vh] max-w-md items-center justify-center">
          <Card className="w-full overflow-hidden rounded-3xl border border-slate-100 bg-white shadow-[0_24px_48px_rgba(0,0,0,0.09)]">
            <CardContent className="p-8 text-center">
              <div className="mx-auto grid h-24 w-24 place-items-center rounded-full bg-emerald-50">
                <div className="grid h-16 w-16 place-items-center rounded-full bg-emerald-500 text-white shadow-lg shadow-emerald-200">
                  <CheckCircle2 className="h-8 w-8" />
                </div>
              </div>
              <h1 className="mt-6 text-2xl font-bold tracking-tight text-slate-900">Pengajuan Berhasil</h1>
              <p className="mt-3 text-sm leading-relaxed text-slate-500">
                Terima kasih. Tim kami akan meninjau pengajuan kolaborasi Anda dan menghubungi PIC melalui email.
              </p>

              <div className="mt-6 rounded-xl border border-slate-200 bg-slate-50 px-4 py-3 text-left text-xs text-slate-500">
                <div className="flex items-center justify-between gap-3">
                  <span className="font-medium text-slate-600">ID Request</span>
                  <span className="rounded-md border border-slate-200 bg-white px-2 py-1 font-mono text-slate-700">{receipt.requestId}</span>
                </div>
                <div className="mt-2 flex items-center justify-between gap-3">
                  <span className="font-medium text-slate-600">Tanggal</span>
                  <span>{formattedDate}</span>
                </div>
              </div>

              <div className="mt-6 grid gap-2">
                <Button
                  type="button"
                  onClick={() => onNavigate("landing")}
                  className="h-11 rounded-xl bg-slate-900 text-white hover:bg-slate-800"
                >
                  <Home className="mr-2 h-4 w-4" />
                  Kembali ke Beranda
                </Button>
                <Button
                  type="button"
                  variant="outline"
                  onClick={() => {
                    setReceipt(null);
                    setForm(initialForm);
                  }}
                  className="h-11 rounded-xl border-[#d7e1db]"
                >
                  Buat Pengajuan Baru
                </Button>
              </div>
            </CardContent>
          </Card>
        </main>
      </div>
    );
  }

  return (
    <div className="relative min-h-screen overflow-hidden bg-[#f8faf9] px-4 py-6 text-slate-800 lg:px-8">
      <div className="pointer-events-none absolute inset-0 bg-[radial-gradient(circle_at_18%_18%,rgba(21,87,56,0.1),transparent_42%),radial-gradient(circle_at_88%_82%,rgba(255,199,0,0.18),transparent_50%)]" />
      <div className="pointer-events-none absolute inset-0 opacity-[0.06] [background-image:radial-gradient(#155738_0.6px,transparent_0.6px)] [background-size:24px_24px]" />

      <div className="relative z-10 mx-auto max-w-7xl">
        <button
          type="button"
          onClick={() => onNavigate("landing")}
          className="mb-6 inline-flex items-center gap-2 rounded-full border border-slate-200 bg-white px-3 py-2 text-sm font-medium text-slate-600 shadow-sm transition hover:border-[#155738]/30 hover:text-[#155738]"
        >
          <ArrowLeft className="h-4 w-4" />
          Kembali ke Beranda
        </button>

        <div className="grid items-center gap-8 lg:grid-cols-12 lg:gap-14">
          <section className="lg:col-span-5">
            <div className="overflow-hidden rounded-3xl border border-white/70 bg-white shadow-[0_22px_44px_rgba(0,0,0,0.08)]">
              <div className="relative aspect-[4/3] w-full overflow-hidden">
                <img
                  src="https://images.unsplash.com/photo-1517048676732-d65bc937f952?auto=format&fit=crop&w=1200&q=80"
                  alt="Kolaborasi warga Surabaya"
                  className="h-full w-full object-cover"
                />
                <div className="absolute inset-0 bg-gradient-to-t from-[#0f3f2a]/45 to-transparent" />
                <div className="absolute bottom-4 left-4 rounded-full bg-white/85 px-3 py-1 text-xs font-semibold text-[#155738]">
                  Surabaya Sinergi
                </div>
              </div>
              <div className="p-6">
                <h1 className="text-4xl font-extrabold tracking-tight text-slate-900">
                  Kolaborasi <span className="text-[#155738]">SIMREKAP</span>
                </h1>
                <p className="mt-3 text-base leading-relaxed text-slate-600">
                  Platform kolaborasi resmi untuk mendukung kegiatan kampung melalui dukungan lintas sektor.
                </p>
                <div className="mt-5 inline-flex items-center gap-2 rounded-full border border-slate-200 bg-slate-50 px-3 py-1 text-xs text-slate-600">
                  <Handshake className="h-3.5 w-3.5 text-[#155738]" />
                  Bergabung dengan ratusan mitra kolaborasi
                </div>
              </div>
            </div>
          </section>

          <section className="lg:col-span-7">
            <Card className="rounded-[2rem] border border-slate-100 bg-white/95 shadow-[0_24px_48px_rgba(0,0,0,0.08)] backdrop-blur">
              <CardHeader className="space-y-2 pb-3">
                <CardTitle className="text-2xl font-bold text-slate-900">Ajukan Kolaborasi</CardTitle>
                <p className="text-sm text-slate-500">
                  Pengajuan akan tercatat sebagai <strong>collaboration_request</strong> dan diproses Moderator Tier 2.
                </p>
              </CardHeader>
              <CardContent>
                <form onSubmit={submit} className="space-y-5">
                  <div className="grid gap-5 md:grid-cols-2">
                    <div className="space-y-1.5">
                      <Label htmlFor="org_name" className="text-xs font-semibold uppercase tracking-[0.12em] text-slate-500">
                        Nama Organisasi
                      </Label>
                      <Input
                        id="org_name"
                        value={form.organizationName}
                        onChange={(event) => updateField("organizationName", event.target.value)}
                        placeholder="Contoh: Komunitas Surabaya Hebat"
                        className="h-11 rounded-xl border-slate-200 bg-slate-50"
                        required
                      />
                    </div>
                    <div className="space-y-1.5">
                      <Label htmlFor="pic_name" className="text-xs font-semibold uppercase tracking-[0.12em] text-slate-500">
                        Nama PIC
                      </Label>
                      <Input
                        id="pic_name"
                        value={form.picName}
                        onChange={(event) => updateField("picName", event.target.value)}
                        placeholder="Nama penanggung jawab"
                        className="h-11 rounded-xl border-slate-200 bg-slate-50"
                        required
                      />
                    </div>
                  </div>

                  <div className="space-y-1.5">
                    <Label htmlFor="email" className="text-xs font-semibold uppercase tracking-[0.12em] text-slate-500">
                      Email Kerja
                    </Label>
                    <Input
                      id="email"
                      type="email"
                      value={form.email}
                      onChange={(event) => updateField("email", event.target.value)}
                      placeholder="nama@organisasi.id"
                      className="h-11 rounded-xl border-slate-200 bg-slate-50"
                      required
                    />
                  </div>

                  <div className="space-y-1.5">
                    <Label htmlFor="support_type" className="text-xs font-semibold uppercase tracking-[0.12em] text-slate-500">
                      Kategori Dukungan
                    </Label>
                    <select
                      id="support_type"
                      value={form.supportType}
                      onChange={(event) => updateField("supportType", event.target.value as CollaborationForm["supportType"])}
                      className="h-11 w-full rounded-xl border border-slate-200 bg-slate-50 px-3 text-sm text-slate-800"
                      required
                    >
                      {supportOptions.map((option) => (
                        <option key={option.value} value={option.value}>
                          {option.label}
                        </option>
                      ))}
                    </select>
                  </div>

                  <div className="space-y-1.5">
                    <Label htmlFor="contribution_scope" className="text-xs font-semibold uppercase tracking-[0.12em] text-slate-500">
                      Skala Kontribusi
                    </Label>
                    <select
                      id="contribution_scope"
                      value={form.contributionScope}
                      onChange={(event) => updateField("contributionScope", event.target.value as CollaborationForm["contributionScope"])}
                      className="h-11 w-full rounded-xl border border-slate-200 bg-slate-50 px-3 text-sm text-slate-800"
                    >
                      <option value="kota">Kota</option>
                      <option value="kecamatan">Kecamatan</option>
                      <option value="kelurahan">Kelurahan (Kampung)</option>
                    </select>
                  </div>

                  {form.contributionScope !== "kota" && (
                    <div className="space-y-2">
                      <Label htmlFor="collab-kecamatan" className="text-xs font-semibold uppercase tracking-[0.12em] text-slate-500">
                        Kecamatan
                      </Label>
                      <div className="grid gap-2 sm:grid-cols-[1fr_auto]">
                        <Input
                          id="collab-kecamatan"
                          value={form.kecamatanName}
                          onChange={(event) => {
                            setForm((prev) => ({
                              ...prev,
                              kecamatanName: event.target.value,
                              kecamatanId: "",
                              kelurahanName: "",
                              kelurahanId: "",
                            }));
                          }}
                          onFocus={() => setFocusedGeoField("kecamatan")}
                          onBlur={closeGeoSuggestions}
                          placeholder="Ketik nama kecamatan"
                          autoComplete="off"
                          className="h-11 rounded-xl border-slate-200 bg-slate-50"
                          required
                        />
                        <Button
                          type="button"
                          variant="outline"
                          className="h-11 border-slate-200"
                          onClick={() => {
                            if (kecamatanSuggestions.length === 0) {
                              toast.error("Kecamatan tidak ditemukan.");
                              return;
                            }
                            pickKecamatan(kecamatanSuggestions[0].name);
                          }}
                        >
                          <Search className="mr-2 h-4 w-4" />
                          Cari
                        </Button>
                      </div>
                      {focusedGeoField === "kecamatan" && (
                        kecamatanSuggestions.length > 0 ? (
                          <div className="max-h-44 overflow-auto rounded-xl border border-slate-200 bg-white p-1 shadow-sm">
                            {kecamatanSuggestions.map((kecamatan) => (
                              <button
                                key={kecamatan.code}
                                type="button"
                                onMouseDown={(event) => {
                                  event.preventDefault();
                                  pickKecamatan(kecamatan.name);
                                }}
                                className="w-full rounded-lg px-3 py-2 text-left text-sm text-slate-700 transition hover:bg-slate-100"
                              >
                                {kecamatan.name}
                              </button>
                            ))}
                          </div>
                        ) : (
                          <p className="rounded-xl border border-slate-200 bg-white px-3 py-2 text-xs text-slate-500">
                            Tidak ada kecamatan yang cocok.
                          </p>
                        )
                      )}
                    </div>
                  )}

                  {form.contributionScope === "kelurahan" && (
                    <div className="space-y-2">
                      <Label htmlFor="collab-kelurahan" className="text-xs font-semibold uppercase tracking-[0.12em] text-slate-500">
                        Kelurahan (Kampung)
                      </Label>
                      <div className="grid gap-2 sm:grid-cols-[1fr_auto]">
                        <Input
                          id="collab-kelurahan"
                          value={form.kelurahanName}
                          onChange={(event) => {
                            setForm((prev) => ({
                              ...prev,
                              kelurahanName: event.target.value,
                              kelurahanId: "",
                            }));
                          }}
                          onFocus={() => setFocusedGeoField("kelurahan")}
                          onBlur={closeGeoSuggestions}
                          placeholder={form.kecamatanName ? "Ketik nama kelurahan" : "Isi kecamatan dulu atau ketik kelurahan"}
                          autoComplete="off"
                          className="h-11 rounded-xl border-slate-200 bg-slate-50"
                          required
                        />
                        <Button
                          type="button"
                          variant="outline"
                          className="h-11 border-slate-200"
                          onClick={() => {
                            if (kelurahanSuggestions.length === 0) {
                              toast.error("Kelurahan tidak ditemukan.");
                              return;
                            }
                            pickKelurahan(kelurahanSuggestions[0]);
                          }}
                        >
                          <Search className="mr-2 h-4 w-4" />
                          Cari
                        </Button>
                      </div>
                      {focusedGeoField === "kelurahan" && (
                        kelurahanSuggestions.length > 0 ? (
                          <div className="max-h-44 overflow-auto rounded-xl border border-slate-200 bg-white p-1 shadow-sm">
                            {kelurahanSuggestions.map((kelurahan) => (
                              <button
                                key={`${kelurahan.kecamatanName}-${kelurahan.name}`}
                                type="button"
                                onMouseDown={(event) => {
                                  event.preventDefault();
                                  pickKelurahan(kelurahan);
                                }}
                                className="flex w-full items-start justify-between rounded-lg px-3 py-2 text-left text-sm text-slate-700 transition hover:bg-slate-100"
                              >
                                <span>{kelurahan.name}</span>
                                <span className="ml-3 text-xs text-slate-500">{kelurahan.kecamatanName}</span>
                              </button>
                            ))}
                          </div>
                        ) : (
                          <p className="rounded-xl border border-slate-200 bg-white px-3 py-2 text-xs text-slate-500">
                            Tidak ada kelurahan yang cocok.
                          </p>
                        )
                      )}
                    </div>
                  )}

                  {geoOptions.length === 0 && form.contributionScope !== "kota" && (
                    <p className="rounded-xl border border-amber-200 bg-amber-50 px-3 py-2 text-xs text-amber-700">
                      Data ID wilayah dari server belum termuat. Pencarian nama tetap aktif dan akan dicocokkan saat kirim.
                    </p>
                  )}

                  <div className="space-y-1.5">
                    <Label htmlFor="support_description" className="text-xs font-semibold uppercase tracking-[0.12em] text-slate-500">
                      Gambaran Dukungan
                    </Label>
                    <Textarea
                      id="support_description"
                      value={form.supportDescription}
                      onChange={(event) => updateField("supportDescription", event.target.value)}
                      placeholder="Jelaskan kontribusi yang ingin Anda berikan"
                      rows={5}
                      className="rounded-xl border-slate-200 bg-slate-50"
                      required
                    />
                  </div>

                  <Button
                    type="submit"
                    disabled={submitting}
                    className="h-12 w-full rounded-xl bg-[#155738] text-white hover:bg-[#0f4a2f]"
                  >
                    {submitting ? "Mengirim..." : "Kirim Proposal"}
                    <ArrowRight className="ml-2 h-4 w-4" />
                  </Button>

                  <p className="flex items-center justify-center gap-1 text-center text-xs text-slate-400">
                    <Sparkles className="h-3.5 w-3.5" />
                    Data diproses sesuai kebijakan privasi Pemerintah Kota Surabaya.
                  </p>
                </form>
              </CardContent>
            </Card>
          </section>
        </div>
      </div>
    </div>
  );
}
