import { Lock } from "lucide-react";
import CryptoPageLayout from "../../layouts/PrimitivePageLayout";

const ECDH_DATA = {
  title: "ECDH (Diffie-Hellman de Curva Elíptica)",
  description: "ECDH es una variante de Diffie-Hellman que utiliza curvas elípticas para el intercambio de claves, ofreciendo mayor seguridad con claves más pequeñas.",
  icon: <Lock size={32} />,
  features: [
    "Intercambio de claves sobre curvas elípticas",
    "Alta eficiencia y seguridad",
    "Usado en protocolos modernos (TLS, Signal)",
    "Claves cortas, bajo consumo de recursos"
  ],
  codeExample: `from krypto_lib import ecdh\n\n# Alice y Bob generan sus pares de claves\nsecret = ecdh.exchange(alice_priv, bob_pub)`,
  securityTips: ["Verifica la autenticidad de las claves", "Usa curvas seguras"],
  links: [
    { label: "Wikipedia ECDH", url: "https://es.wikipedia.org/wiki/Intercambio_de_claves_Diffie-Hellman#Curvas_el%C3%ADpticas" },
    { label: "GitHub Krypto", url: "https://..." }
  ]
};

const ECDHPage = () => <CryptoPageLayout data={ECDH_DATA} />;

export default ECDHPage;
