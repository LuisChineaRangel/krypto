import { useNavigate } from "react-router-dom";

export function useSidebarNavigation() {
  const navigate = useNavigate();
  const getPath = (id : string) => {
    switch (id) {
      case "aes": return "/aes";
      case "vigenere": return "/vigenere";
      case "arc4": return "/arc4";
      case "chacha20": return "/chacha20";
      case "rsa": return "/rsa";
      case "ecc": return "/ecc";
      case "ecdh": return "/ecdh";
      case "eceg": return "/eceg";
      case "diffie-hellman": return "/diffie-hellman";
      case "elgamal": return "/elgamal";
      case "gps-l1-ca": return "/gps-l1-ca";
      case "prga": return "/prga";
      default: return "/";
    }
  };
  return { navigate, getPath };
}
