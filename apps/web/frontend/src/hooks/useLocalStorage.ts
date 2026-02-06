import { useState, useEffect } from "react";

export function useLocalStorage<T>(key: string, initialValue: T) {
  const [storedValue, setStoredValue] = useState<T>(() => {
    if (globalThis.window === undefined) return initialValue;

    try {
      const item = globalThis.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch (error) {
      console.error("Error leyendo localStorage", error);
      return initialValue;
    }
  });

  useEffect(() => {
    try {
      if (globalThis.window !== undefined) {
        globalThis.localStorage.setItem(key, JSON.stringify(storedValue));
      }
    } catch (error) {
      console.error("Error guardando en localStorage", error);
    }
  }, [key, storedValue]);

  return [storedValue, setStoredValue] as const;
}
