import { useState } from "react";
import * as authApi from "@/api/auth";

export function useAuth() {
  const [loading, setLoading] = useState(false);

  async function login(payload: unknown) {
    setLoading(true);
    try {
      return await authApi.login(payload);
    } finally {
      setLoading(false);
    }
  }

  async function signup(payload: unknown) {
    setLoading(true);
    try {
      return await authApi.signup(payload);
    } finally {
      setLoading(false);
    }
  }

  return { loading, login, signup, logout: authApi.logout, getMe: authApi.getMe };
}
