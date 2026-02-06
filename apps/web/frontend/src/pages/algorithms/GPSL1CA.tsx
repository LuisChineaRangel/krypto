import { Lock } from "lucide-react";
import CryptoPageLayout from "../../components/templates/CryptoPageLayout";

const GPSL1CA_DATA = {
  title: "GPS L1 C/A (PRNG)",
  description: "El generador GPS L1 C/A es un PRNG utilizado en los sistemas de posicionamiento global, basado en registros de desplazamiento de retroalimentación lineal (LFSR).",
  icon: <Lock size={32} />,
  features: [
    "Generador de secuencias pseudoaleatorias",
    "Basado en LFSR",
    "Usado en GPS para autenticación y cifrado",
    "Secuencia de longitud 1023"
  ],
  codeExample: `from krypto_lib import gps_l1_ca\n\nseq = gps_l1_ca.generate()`,
  securityTips: ["No usar para cifrado fuerte", "Solo para aplicaciones GPS"],
  links: [
    { label: "Wikipedia GPS L1 C/A", url: "https://en.wikipedia.org/wiki/CA_code" },
    { label: "GitHub Krypto", url: "https://..." }
  ]
};

const GPSL1CAPage = () => <CryptoPageLayout data={GPSL1CA_DATA} />;

export default GPSL1CAPage;
