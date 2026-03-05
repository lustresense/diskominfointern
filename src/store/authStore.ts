import type { User } from "@/types/user";

type AuthState = {
  token: string | null;
  user: User | null;
};

type AuthListener = (state: AuthState) => void;

let state: AuthState = {
  token: null,
  user: null,
};

const listeners = new Set<AuthListener>();

function emit() {
  for (const listener of listeners) {
    listener(state);
  }
}

export const authStore = {
  getState(): AuthState {
    return state;
  },
  setState(next: Partial<AuthState>) {
    state = { ...state, ...next };
    emit();
  },
  clear() {
    state = { token: null, user: null };
    emit();
  },
  subscribe(listener: AuthListener) {
    listeners.add(listener);
    return () => listeners.delete(listener);
  },
};
