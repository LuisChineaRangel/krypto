import { Lock } from "lucide-react";
import CryptoPageLayout from "../../layouts/PrimitivePageLayout";

const ARC4_DATA = {
  title: "ARC4 (RC4)",
  description: "ARC4 (también conocido como RC4) es un cifrador de flujo ampliamente utilizado, aunque hoy en día no se recomienda para nuevas aplicaciones por vulnerabilidades conocidas.",
  icon: <Lock size={32} />,
  features: [
    "Cifrado de flujo (stream cipher)",
    "Clave variable hasta 256 bytes",
    "Rápido y simple de implementar",
    "Vulnerable a varios ataques si no se usa correctamente"
  ],
  codeExample: `from krypto_lib import arc4\n\nkey = b'secret'\ntext = b'hello'\ncipher = arc4(text, key)`,
  securityTips: ["Evita reutilizar claves", "No recomendado para datos sensibles"],
  links: [
    { label: "Wikipedia RC4", url: "https://es.wikipedia.org/wiki/RC4" },
    { label: "GitHub Krypto", url: "https://..." }
  ]
};

const ARC4Page = () => <CryptoPageLayout data={ARC4_DATA} />;

export default ARC4Page;
