import { Lock } from "lucide-react";
import CryptoPageLayout from "../../components/templates/CryptoPageLayout";

const VIGENERE_DATA = {
  title: "Vigenère",
  description: "El cifrado de Vigenère es un método clásico de cifrado por sustitución polialfabética, fácil de implementar pero vulnerable a análisis de frecuencia.",
  icon: <Lock size={32} />,
  features: [
    "Cifrado clásico por sustitución",
    "Clave repetitiva",
    "Fácil de romper con análisis de frecuencia",
    "Base para métodos polialfabéticos"
  ],
  codeExample: `from krypto_lib import vigenere\n\nkey = b'LEMON'\ntext = b'ATTACKATDAWN'\ncipher = vigenere.encrypt(text, key)`,
  securityTips: ["No usar para datos sensibles", "Clave larga mejora seguridad"],
  links: [
    { label: "Wikipedia Vigenère", url: "https://es.wikipedia.org/wiki/Cifrado_Vigen%C3%A8re" },
    { label: "GitHub Krypto", url: "https://..." }
  ]
};

const VigenerePage = () => <CryptoPageLayout data={VIGENERE_DATA} />;

export default VigenerePage;
