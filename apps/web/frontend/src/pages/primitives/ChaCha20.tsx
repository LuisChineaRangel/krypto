import { Lock } from "lucide-react";
import CryptoPageLayout from "../../layouts/PrimitivePageLayout";

const CHACHA20_DATA = {
  title: "ChaCha20",
  description: "ChaCha20 es un cifrador de flujo moderno, rápido y seguro, ampliamente utilizado en protocolos como TLS y VPNs.",
  icon: <Lock size={32} />,
  features: [
    "Cifrado de flujo (stream cipher)",
    "Clave de 256 bits",
    "Nonce de 96 bits",
    "Diseñado para alta seguridad y rendimiento"
  ],
  codeExample: `from krypto_lib import chacha20\n\nkey = b'...'\nnonce = b'...'\ntext = b'...'\ncipher = chacha20(text, key, nonce)`,
  securityTips: ["Usa nonces únicos", "No reutilices clave+nonce"],
  links: [
    { label: "RFC 8439", url: "https://datatracker.ietf.org/doc/html/rfc8439" },
    { label: "GitHub Krypto", url: "https://..." }
  ]
};

const ChaCha20Page = () => <CryptoPageLayout data={CHACHA20_DATA} />;

export default ChaCha20Page;
