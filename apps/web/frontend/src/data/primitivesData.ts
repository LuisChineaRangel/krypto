import type { PrimitivePageData } from "@layouts/PrimitivePageLayout";

export const PRIMITIVES: Record<string, PrimitivePageData> = {
  "aes": {
    title: "AES",
    description:
      "Advanced Encryption Standard (AES) es el estándar de cifrado simétrico líder. Utiliza aritmética en $GF(2^8)$ para sus transformaciones.",
    icon: "Lock",
    features: [
      "Cifrado por bloques de 128 bits",
      "Claves de 128, 192 o 256 bits",
      "Transformaciones: SubBytes, ShiftRows, MixColumns",
      "Implementación optimizada con NumPy",
    ],
    codeExample: `from krypto_lib import aes\n\nkey = b"2b7e1516..."\ntext = b"3243f6a8..."\ncipher = aes(text, key)`,
    securityTips: ["Evita modo ECB", "Usa IV aleatorio", "Claves > 128 bits"],
    links: [
      { label: "Documentación NIST", url: "https://..." },
      { label: "GitHub Krypto", url: "https://..." },
    ],
  },

  "vigenere": {
    title: "Vigenère",
    description:
      "El cifrado de Vigenère es un método clásico de cifrado por sustitución polialfabética, fácil de implementar pero vulnerable a análisis de frecuencia.",
    icon: "Lock",
    features: [
      "Cifrado clásico por sustitución",
      "Clave repetitiva",
      "Fácil de romper con análisis de frecuencia",
      "Base para métodos polialfabéticos",
    ],
    codeExample: `from krypto_lib import vigenere\n\nkey = b'LEMON'\ntext = b'ATTACKATDAWN'\ncipher = vigenere.encrypt(text, key)`,
    securityTips: ["No usar para datos sensibles", "Clave larga mejora seguridad"],
    links: [
      { label: "Wikipedia Vigenère", url: "https://es.wikipedia.org/wiki/Cifrado_Vigen%C3%A8re" },
      { label: "GitHub Krypto", url: "https://..." },
    ],
  },

  "arc4": {
    title: "ARC4 (RC4)",
    description:
      "ARC4 (también conocido como RC4) es un cifrador de flujo ampliamente utilizado, aunque hoy en día no se recomienda para nuevas aplicaciones por vulnerabilidades conocidas.",
    icon: "Lock",
    features: [
      "Cifrado de flujo (stream cipher)",
      "Clave variable hasta 256 bytes",
      "Rápido y simple de implementar",
      "Vulnerable a varios ataques si no se usa correctamente",
    ],
    codeExample: `from krypto_lib import arc4\n\nkey = b'secret'\ntext = b'hello'\ncipher = arc4(text, key)`,
    securityTips: ["Evita reutilizar claves", "No recomendado para datos sensibles"],
    links: [
      { label: "Wikipedia RC4", url: "https://es.wikipedia.org/wiki/RC4" },
      { label: "GitHub Krypto", url: "https://..." },
    ],
  },

  "chacha20": {
    title: "ChaCha20",
    description:
      "ChaCha20 es un cifrador de flujo moderno, rápido y seguro, ampliamente utilizado en protocolos como TLS y VPNs.",
    icon: "Lock",
    features: [
      "Cifrado de flujo (stream cipher)",
      "Clave de 256 bits",
      "Nonce de 96 bits",
      "Diseñado para alta seguridad y rendimiento",
    ],
    codeExample: `from krypto_lib import chacha20\n\nkey = b'...'\nnonce = b'...'\ntext = b'...'\ncipher = chacha20(text, key, nonce)`,
    securityTips: ["Usa nonces únicos", "No reutilices clave+nonce"],
    links: [
      { label: "RFC 8439", url: "https://datatracker.ietf.org/doc/html/rfc8439" },
      { label: "GitHub Krypto", url: "https://..." },
    ],
  },

  "rsa": {
    title: "RSA",
    description:
      "RSA es uno de los algoritmos de cifrado asimétrico más conocidos, basado en la factorización de números enteros grandes.",
    icon: "Lock",
    features: [
      "Cifrado y firma digital",
      "Basado en la dificultad de factorizar números grandes",
      "Claves públicas y privadas",
      "Usado en SSL/TLS, PGP, etc.",
    ],
    codeExample: `from krypto_lib import rsa\n\n# Generar claves, cifrar y descifrar\npriv, pub = rsa.generate_keypair()\ncipher = rsa.encrypt(pub, msg)\nplain = rsa.decrypt(priv, cipher)`,
    securityTips: ["Usa claves de al menos 2048 bits", "Protege la clave privada"],
    links: [
      { label: "Wikipedia RSA", url: "https://es.wikipedia.org/wiki/RSA" },
      { label: "GitHub Krypto", url: "https://..." },
    ],
  },

  "ecc": {
    title: "ECC (Criptografía de Curva Elíptica)",
    description:
      "ECC es una técnica criptográfica basada en las propiedades algebraicas de las curvas elípticas sobre campos finitos. Ofrece alta seguridad con claves más cortas.",
    icon: "Lock",
    features: [
      "Basado en el problema del logaritmo discreto en curvas elípticas",
      "Claves más cortas para igual nivel de seguridad",
      "Eficiente para dispositivos con recursos limitados",
      "Usado en criptomonedas y TLS",
    ],
    codeExample: `from krypto_lib import ecc\n\n# Generar clave privada y pública\npriv, pub = ecc.generate_keypair()`,
    securityTips: ["Usa curvas recomendadas", "Protege la clave privada"],
    links: [
      { label: "Wikipedia ECC", url: "https://es.wikipedia.org/wiki/Criptograf%C3%ADa_de_curva_el%C3%ADptica" },
      { label: "GitHub Krypto", url: "https://..." },
    ],
  },

  "ecdh": {
    title: "ECDH (Diffie-Hellman de Curva Elíptica)",
    description:
      "ECDH es una variante de Diffie-Hellman que utiliza curvas elípticas para el intercambio de claves, ofreciendo mayor seguridad con claves más pequeñas.",
    icon: "Lock",
    features: [
      "Intercambio de claves sobre curvas elípticas",
      "Alta eficiencia y seguridad",
      "Usado en protocolos modernos (TLS, Signal)",
      "Claves cortas, bajo consumo de recursos",
    ],
    codeExample: `from krypto_lib import ecdh\n\n# Alice y Bob generan sus pares de claves\nsecret = ecdh.exchange(alice_priv, bob_pub)`,
    securityTips: ["Verifica la autenticidad de las claves", "Usa curvas seguras"],
    links: [
      { label: "Wikipedia ECDH", url: "https://es.wikipedia.org/wiki/Intercambio_de_claves_Diffie-Hellman#Curvas_el%C3%ADpticas" },
      { label: "GitHub Krypto", url: "https://..." },
    ],
  },

  "eceg": {
    title: "ECEG (ElGamal de Curva Elíptica)",
    description:
      "ECEG es la versión de ElGamal implementada sobre curvas elípticas, combinando la seguridad de ElGamal con la eficiencia de ECC.",
    icon: "Lock",
    features: [
      "Cifrado asimétrico sobre curvas elípticas",
      "Basado en el problema del logaritmo discreto",
      "Claves cortas, alta seguridad",
      "Usado en sistemas modernos de cifrado",
    ],
    codeExample: `from krypto_lib import eceg\n\n# Cifrado y descifrado\ncipher = eceg.encrypt(pub, msg)\nplain = eceg.decrypt(priv, cipher)`,
    securityTips: ["Protege la clave privada", "Usa curvas recomendadas"],
    links: [
      { label: "Wikipedia ElGamal", url: "https://es.wikipedia.org/wiki/ElGamal" },
      { label: "GitHub Krypto", url: "https://..." },
    ],
  },

  "diffie-hellman": {
    title: "Diffie-Hellman",
    description:
      "Diffie-Hellman es un protocolo de intercambio de claves que permite a dos partes establecer una clave secreta compartida sobre un canal inseguro.",
    icon: "Lock",
    features: [
      "Intercambio de claves basado en logaritmo discreto",
      "No requiere compartir la clave secreta",
      "Base para muchos protocolos modernos",
      "Vulnerable a ataques MITM si no se autentica",
    ],
    codeExample: `from krypto_lib import diffie_hellman\n\n# Alice y Bob acuerdan p, g\nsecret = diffie_hellman(p, g, a_priv, b_priv)`,
    securityTips: ["Autentica las partes", "Usa parámetros seguros"],
    links: [
      { label: "Wikipedia Diffie-Hellman", url: "https://es.wikipedia.org/wiki/Intercambio_de_claves_Diffie-Hellman" },
      { label: "GitHub Krypto", url: "https://..." },
    ],
  },

  "elgamal": {
    title: "ElGamal",
    description:
      "ElGamal es un sistema de cifrado asimétrico basado en el problema del logaritmo discreto, ampliamente usado en criptografía moderna.",
    icon: "Lock",
    features: [
      "Cifrado asimétrico",
      "Basado en logaritmo discreto",
      "Permite cifrado y firma digital",
      "Usado en sistemas de voto electrónico",
    ],
    codeExample: `from krypto_lib import elgamal\n\n# Generar claves, cifrar y descifrar\npriv, pub = elgamal.generate_keypair()\ncipher = elgamal.encrypt(pub, msg)\nplain = elgamal.decrypt(priv, cipher)`,
    securityTips: ["Usa parámetros grandes y seguros", "Protege la clave privada"],
    links: [
      { label: "Wikipedia ElGamal", url: "https://es.wikipedia.org/wiki/ElGamal" },
      { label: "GitHub Krypto", url: "https://..." },
    ],
  },

  "gps-l1-ca": {
    title: "GPS L1 C/A (PRNG)",
    description:
      "El generador GPS L1 C/A es un PRNG utilizado en los sistemas de posicionamiento global, basado en registros de desplazamiento de retroalimentación lineal (LFSR).",
    icon: "Lock",
    features: [
      "Generador de secuencias pseudoaleatorias",
      "Basado en LFSR",
      "Usado en GPS para autenticación y cifrado",
      "Secuencia de longitud 1023",
    ],
    codeExample: `from krypto_lib import gps_l1_ca\n\nseq = gps_l1_ca.generate()`,
    securityTips: ["No usar para cifrado fuerte", "Solo para aplicaciones GPS"],
    links: [
      { label: "Wikipedia GPS L1 C/A", url: "https://en.wikipedia.org/wiki/CA_code" },
      { label: "GitHub Krypto", url: "https://..." },
    ],
  },

  "prga": {
    title: "PRGA (Pseudorandom Generation Algorithm)",
    description:
      "PRGA es el algoritmo generador de secuencias pseudoaleatorias usado en cifrados de flujo como RC4.",
    icon: "Lock",
    features: [
      "Generador de secuencias pseudoaleatorias",
      "Usado en cifrados de flujo",
      "Produce un byte por iteración",
      "Base para el cifrado RC4",
    ],
    codeExample: `from krypto_lib import prga\n\nkey = b'clave'\nprng = prga(key)\nbyte = next(prng)`,
    securityTips: ["No usar solo PRGA para cifrado", "Combinar con KSA en RC4"],
    links: [
      { label: "Wikipedia RC4", url: "https://es.wikipedia.org/wiki/RC4" },
      { label: "GitHub Krypto", url: "https://..." },
    ],
  },
};

export default PRIMITIVES;
