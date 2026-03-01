import { useState } from 'react';
import { Button } from '@/app/components/ui/button';
import { Card, CardContent } from '@/app/components/ui/card';
import { Input } from '@/app/components/ui/input';
import { Label } from '@/app/components/ui/label';
import { Alert, AlertDescription } from '@/app/components/ui/alert';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/app/components/ui/tabs';
import { ArrowLeft, AlertCircle, Loader2, Info } from 'lucide-react';
import { apiPublicPost } from '@/lib/api';

interface LoginPageProps {
  onNavigate: (page: 'landing' | 'register') => void;
  onLogin: (user: any, token: string) => void;
}

export function LoginPage({ onNavigate, onLogin }: LoginPageProps) {
  const showDemoCredentials = import.meta.env.DEV || import.meta.env.VITE_SHOW_DEMO_CREDENTIALS === 'true';
  const [activeTab, setActiveTab] = useState('user');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const switchTab = (tab: string) => {
    setActiveTab(tab);
    setEmail('');
    setPassword('');
    setError('');
  };

  const handleAuthLogin = async (e: React.FormEvent, expectedRole: 'user' | 'moderator') => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      const data = await apiPublicPost('/auth/login', { email, password });

      if (data.user?.role && data.user.role !== expectedRole) {
        throw new Error(expectedRole === 'moderator' ? 'Akun ini bukan moderator' : 'Akun ini bukan relawan');
      }

      onLogin(data.user, data.token);
    } catch (err: any) {
      setError(err.message || 'Email atau password salah');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-white text-gray-900 font-sans selection:bg-[#FFC107] selection:text-black flex flex-col">
      <header className="bg-white border-b border-gray-100">
        <div className="container mx-auto px-4 py-4 flex items-center justify-between">
          <button
            onClick={() => onNavigate('landing')}
            className="flex items-center gap-2 text-gray-600 hover:text-black transition-colors font-medium"
          >
            <ArrowLeft className="w-5 h-5" />
            <span>Kembali</span>
          </button>
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 bg-black text-[#FFC107] rounded-lg flex items-center justify-center font-bold text-xl">
              SR
            </div>
          </div>
        </div>
      </header>

      <div className="flex-1 flex items-center justify-center p-4">
        <div className="w-full max-w-md">
          <div className="text-center mb-8">
            <h2 className="text-3xl font-bold mb-2">Selamat Datang Kembali</h2>
            <p className="text-gray-600">Masuk untuk mengelola kegiatan relawan</p>
          </div>

          <Card className="border-gray-200 shadow-xl rounded-2xl overflow-hidden">
            <Tabs value={activeTab} onValueChange={switchTab}>
              <div className="bg-gray-50 border-b border-gray-100 p-1">
                <TabsList className="grid w-full grid-cols-2 bg-transparent h-12">
                  <TabsTrigger
                    value="user"
                    className="data-[state=active]:bg-white data-[state=active]:shadow-sm rounded-lg text-gray-600 data-[state=active]:text-black font-semibold"
                  >
                    Relawan
                  </TabsTrigger>
                  <TabsTrigger
                    value="moderator"
                    className="data-[state=active]:bg-white data-[state=active]:shadow-sm rounded-lg text-gray-600 data-[state=active]:text-black font-semibold"
                  >
                    Moderator
                  </TabsTrigger>
                </TabsList>
              </div>

              <CardContent className="p-6 md:p-8">
                <TabsContent value="user" className="mt-0">
                  <form onSubmit={(e) => handleAuthLogin(e, 'user')} className="space-y-5">
                    {error && (
                      <Alert variant="destructive" className="bg-red-50 text-red-900 border-red-200">
                        <AlertCircle className="h-4 w-4" />
                        <AlertDescription>{error}</AlertDescription>
                      </Alert>
                    )}

                    <div className="space-y-2">
                      <Label htmlFor="email" className="font-semibold">Email</Label>
                      <Input
                        id="email"
                        type="email"
                        placeholder="nama@email.com"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                        disabled={loading}
                        className="h-12 border-gray-300 focus:border-black focus:ring-black rounded-xl"
                      />
                    </div>

                    <div className="space-y-2">
                      <Label htmlFor="password">Password</Label>
                      <Input
                        id="password"
                        type="password"
                        placeholder="********"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                        disabled={loading}
                        className="h-12 border-gray-300 focus:border-black focus:ring-black rounded-xl"
                      />
                    </div>

                    {showDemoCredentials && (
                      <div className="bg-blue-50 p-3 rounded-lg flex items-start gap-3 border border-blue-100">
                        <Info className="w-5 h-5 text-blue-600 flex-shrink-0 mt-0.5" />
                        <div className="text-sm text-blue-800">
                          <p className="font-semibold mb-1">Akun Demo Relawan:</p>
                          <p>Email: <code className="bg-blue-100 px-1 rounded">relawan.demo@simrp.app</code></p>
                          <p>Pass: <code className="bg-blue-100 px-1 rounded">password123</code></p>
                        </div>
                      </div>
                    )}

                    <Button type="submit" className="w-full bg-black text-white hover:bg-gray-800 h-12 rounded-xl text-lg font-bold" disabled={loading}>
                      {loading ? <><Loader2 className="mr-2 h-4 w-4 animate-spin" />Memuat...</> : 'Masuk'}
                    </Button>

                    <div className="text-center text-sm pt-2">
                      Belum punya akun?{' '}
                      <button type="button" onClick={() => onNavigate('register')} className="text-black font-bold hover:underline">
                        Daftar Sekarang
                      </button>
                    </div>
                  </form>
                </TabsContent>

                <TabsContent value="moderator" className="mt-0">
                  <form onSubmit={(e) => handleAuthLogin(e, 'moderator')} className="space-y-5">
                    {error && (
                      <Alert variant="destructive" className="bg-red-50 text-red-900 border-red-200">
                        <AlertCircle className="h-4 w-4" />
                        <AlertDescription>{error}</AlertDescription>
                      </Alert>
                    )}

                    {showDemoCredentials && (
                      <Alert className="bg-blue-50 border-blue-100 text-blue-900">
                        <Info className="h-4 w-4 text-blue-700" />
                        <AlertDescription className="text-sm">
                          <strong>Akses Moderator (ASN):</strong><br />
                          Contoh akun: moderator1.demo@simrp.app / password123
                        </AlertDescription>
                      </Alert>
                    )}

                    <div className="space-y-2">
                      <Label htmlFor="moderator-email">Email</Label>
                      <Input
                        id="moderator-email"
                        type="email"
                        placeholder="asn@email.com"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                        disabled={loading}
                        className="h-12 border-gray-300 focus:border-black focus:ring-black rounded-xl"
                      />
                    </div>

                    <div className="space-y-2">
                      <Label htmlFor="moderator-password">Password</Label>
                      <Input
                        id="moderator-password"
                        type="password"
                        placeholder="********"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                        disabled={loading}
                        className="h-12 border-gray-300 focus:border-black focus:ring-black rounded-xl"
                      />
                    </div>

                    <Button type="submit" className="w-full bg-black text-white hover:bg-gray-800 h-12 rounded-xl text-lg font-bold" disabled={loading}>
                      {loading ? <><Loader2 className="mr-2 h-4 w-4 animate-spin" />Memuat...</> : 'Masuk sebagai Moderator'}
                    </Button>
                  </form>
                </TabsContent>
              </CardContent>
            </Tabs>
          </Card>
        </div>
      </div>
    </div>
  );
}
