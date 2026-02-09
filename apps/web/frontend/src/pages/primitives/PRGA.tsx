import { Lock } from "lucide-react";
import CryptoPageLayout from "../../layouts/PrimitivePageLayout";

const PRGA_DATA = {
  title: "PRGA (Pseudorandom Generation Algorithm)",
  description: "PRGA es el algoritmo generador de secuencias pseudoaleatorias usado en cifrados de flujo como RC4.",
  icon: <Lock size={32} />,
  features: [
    "Generador de secuencias pseudoaleatorias",
    "Usado en cifrados de flujo",
    "Produce un byte por iteración",
    "Base para el cifrado RC4"
  ],
  codeExample: `from krypto_lib import prga\n\nkey = b'clave'\nprng = prga(key)\nbyte = next(prng)`,
  securityTips: ["No usar solo PRGA para cifrado", "Combinar con KSA en RC4"],
  links: [
    { label: "Wikipedia RC4", url: "https://es.wikipedia.org/wiki/RC4" },
    { label: "GitHub Krypto", url: "https://..." }
  ]
};

const PRGAPage = () => <CryptoPageLayout data={PRGA_DATA} />;

export default PRGAPage;
