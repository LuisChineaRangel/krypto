import { Lock } from "lucide-react";
import CryptoPageLayout from "../../layouts/PrimitivePageLayout";

const DIFFIE_HELLMAN_DATA = {
  title: "Diffie-Hellman",
  description: "Diffie-Hellman es un protocolo de intercambio de claves que permite a dos partes establecer una clave secreta compartida sobre un canal inseguro.",
  icon: <Lock size={32} />,
  features: [
    "Intercambio de claves basado en logaritmo discreto",
    "No requiere compartir la clave secreta",
    "Base para muchos protocolos modernos",
    "Vulnerable a ataques MITM si no se autentica"
  ],
  codeExample: `from krypto_lib import diffie_hellman\n\n# Alice y Bob acuerdan p, g\nsecret = diffie_hellman(p, g, a_priv, b_priv)`,
  securityTips: ["Autentica las partes", "Usa parámetros seguros"],
  links: [
    { label: "Wikipedia Diffie-Hellman", url: "https://es.wikipedia.org/wiki/Intercambio_de_claves_Diffie-Hellman" },
    { label: "GitHub Krypto", url: "https://..." }
  ]
};

const DiffieHellmanPage = () => <CryptoPageLayout data={DIFFIE_HELLMAN_DATA} />;

export default DiffieHellmanPage;
