type UiState = {
  loading: boolean;
  toastMessage: string | null;
};

type UiListener = (state: UiState) => void;

let state: UiState = {
  loading: false,
  toastMessage: null,
};

const listeners = new Set<UiListener>();

function emit() {
  for (const listener of listeners) {
    listener(state);
  }
}

export const uiStore = {
  getState(): UiState {
    return state;
  },
  setLoading(loading: boolean) {
    state = { ...state, loading };
    emit();
  },
  setToast(message: string | null) {
    state = { ...state, toastMessage: message };
    emit();
  },
  subscribe(listener: UiListener) {
    listeners.add(listener);
    return () => listeners.delete(listener);
  },
};
