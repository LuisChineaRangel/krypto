import { Lock } from "lucide-react";
import CryptoPageLayout from "../../layouts/PrimitivePageLayout";


const AES_DATA = {
  title: "AES",
  description: "Advanced Encryption Standard (AES) es el estándar de cifrado simétrico líder. Utiliza aritmética en $GF(2^8)$ para sus transformaciones.",
  icon: <Lock size={32} />,
  features: [
    "Cifrado por bloques de 128 bits",
    "Claves de 128, 192 o 256 bits",
    "Transformaciones: SubBytes, ShiftRows, MixColumns",
    "Implementación optimizada con NumPy"
  ],
  codeExample: `from krypto_lib import aes\n\nkey = b"2b7e1516..."\ntext = b"3243f6a8..."\ncipher = aes(text, key)`,
  securityTips: ["Evita modo ECB", "Usa IV aleatorio", "Claves > 128 bits"],
  links: [
    { label: "Documentación NIST", url: "https://..." },
    { label: "GitHub Krypto", url: "https://..." }
  ]
};

const AESPage = () => <CryptoPageLayout data={AES_DATA} />;

export default AESPage;
