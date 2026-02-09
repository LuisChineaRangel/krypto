import { Lock } from "lucide-react";
import CryptoPageLayout from "../../layouts/PrimitivePageLayout";

const ELGAMAL_DATA = {
  title: "ElGamal",
  description: "ElGamal es un sistema de cifrado asimétrico basado en el problema del logaritmo discreto, ampliamente usado en criptografía moderna.",
  icon: <Lock size={32} />,
  features: [
    "Cifrado asimétrico",
    "Basado en logaritmo discreto",
    "Permite cifrado y firma digital",
    "Usado en sistemas de voto electrónico"
  ],
  codeExample: `from krypto_lib import elgamal\n\n# Generar claves, cifrar y descifrar\npriv, pub = elgamal.generate_keypair()\ncipher = elgamal.encrypt(pub, msg)\nplain = elgamal.decrypt(priv, cipher)`,
  securityTips: ["Usa parámetros grandes y seguros", "Protege la clave privada"],
  links: [
    { label: "Wikipedia ElGamal", url: "https://es.wikipedia.org/wiki/ElGamal" },
    { label: "GitHub Krypto", url: "https://..." }
  ]
};

const ElGamalPage = () => <CryptoPageLayout data={ELGAMAL_DATA} />;

export default ElGamalPage;
