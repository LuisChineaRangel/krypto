import { Lock } from "lucide-react";
import CryptoPageLayout from "../../layouts/PrimitivePageLayout";

const RSA_DATA = {
  title: "RSA",
  description: "RSA es uno de los algoritmos de cifrado asimétrico más conocidos, basado en la factorización de números enteros grandes.",
  icon: <Lock size={32} />,
  features: [
    "Cifrado y firma digital",
    "Basado en la dificultad de factorizar números grandes",
    "Claves públicas y privadas",
    "Usado en SSL/TLS, PGP, etc."
  ],
  codeExample: `from krypto_lib import rsa\n\n# Generar claves, cifrar y descifrar\npriv, pub = rsa.generate_keypair()\ncipher = rsa.encrypt(pub, msg)\nplain = rsa.decrypt(priv, cipher)`,
  securityTips: ["Usa claves de al menos 2048 bits", "Protege la clave privada"],
  links: [
    { label: "Wikipedia RSA", url: "https://es.wikipedia.org/wiki/RSA" },
    { label: "GitHub Krypto", url: "https://..." }
  ]
};

const RSAPage = () => <CryptoPageLayout data={RSA_DATA} />;

export default RSAPage;
