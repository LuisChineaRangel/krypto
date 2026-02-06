import { Lock } from "lucide-react";
import CryptoPageLayout from "../../components/templates/CryptoPageLayout";

const ECC_DATA = {
  title: "ECC (Criptografía de Curva Elíptica)",
  description: "ECC es una técnica criptográfica basada en las propiedades algebraicas de las curvas elípticas sobre campos finitos. Ofrece alta seguridad con claves más cortas.",
  icon: <Lock size={32} />,
  features: [
    "Basado en el problema del logaritmo discreto en curvas elípticas",
    "Claves más cortas para igual nivel de seguridad",
    "Eficiente para dispositivos con recursos limitados",
    "Usado en criptomonedas y TLS"
  ],
  codeExample: `from krypto_lib import ecc\n\n# Generar clave privada y pública\npriv, pub = ecc.generate_keypair()`,
  securityTips: ["Usa curvas recomendadas", "Protege la clave privada"],
  links: [
    { label: "Wikipedia ECC", url: "https://es.wikipedia.org/wiki/Criptograf%C3%ADa_de_curva_el%C3%ADptica" },
    { label: "GitHub Krypto", url: "https://..." }
  ]
};

const ECCPage = () => <CryptoPageLayout data={ECC_DATA} />;

export default ECCPage;
