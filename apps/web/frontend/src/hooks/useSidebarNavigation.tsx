import { useNavigate } from "react-router-dom";

export function useSidebarNavigation() {
    const routes: Record<string, string> = {
        "aes": "/aes",
        "vigenere": "/vigenere",
        "arc4": "/arc4",
        "chacha20": "/chacha20",
        "rsa": "/rsa",
        "ecc": "/ecc",
        "ecdh": "/ecdh",
        "eceg": "/eceg",
        "diffie-hellman": "/diffie-hellman",
        "elgamal": "/elgamal",
        "gps-l1-ca": "/gps-l1-ca",
        "prga": "/prga",
        "default": "/"
    };

    const navigate = useNavigate();
    const getPath = (id: string) => routes[id] || routes["default"];
    return { navigate, getPath };
}
