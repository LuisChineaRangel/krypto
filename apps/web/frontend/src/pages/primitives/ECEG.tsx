import { Lock } from "lucide-react";
import CryptoPageLayout from "../../layouts/PrimitivePageLayout";

const ECEG_DATA = {
  title: "ECEG (ElGamal de Curva Elíptica)",
  description: "ECEG es la versión de ElGamal implementada sobre curvas elípticas, combinando la seguridad de ElGamal con la eficiencia de ECC.",
  icon: <Lock size={32} />,
  features: [
    "Cifrado asimétrico sobre curvas elípticas",
    "Basado en el problema del logaritmo discreto",
    "Claves cortas, alta seguridad",
    "Usado en sistemas modernos de cifrado"
  ],
  codeExample: `from krypto_lib import eceg\n\n# Cifrado y descifrado\ncipher = eceg.encrypt(pub, msg)\nplain = eceg.decrypt(priv, cipher)`,
  securityTips: ["Protege la clave privada", "Usa curvas recomendadas"],
  links: [
    { label: "Wikipedia ElGamal", url: "https://es.wikipedia.org/wiki/ElGamal" },
    { label: "GitHub Krypto", url: "https://..." }
  ]
};

const ECEGPage = () => <CryptoPageLayout data={ECEG_DATA} />;

export default ECEGPage;
