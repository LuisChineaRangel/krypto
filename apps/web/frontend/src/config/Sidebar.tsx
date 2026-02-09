import { ShieldCheck, Key } from "lucide-react";

const SIDEBAR_STRUCTURE = [
	{
		id: "symmetric",
		icon: <ShieldCheck size={20} />,
		children: [
			{ id: "block", children: [{ id: "aes" }] },
			{ id: "classical", children: [{ id: "vigenere" }] },
			{ id: "stream", children: [{ id: "arc4" }, { id: "chacha20" }] },
		],
	},
	{
		id: "asymmetric",
		icon: <Key size={20} />,
		children: [
			{ id: "factorization", children: [{ id: "rsa" }] },
			{ id: "discrete-log", children: [{ id: "diffie-hellman" }, { id: "elgamal" }] },
			{ id: "elliptic-curve", children: [{ id: "ecc" }, { id: "ecdh" }, { id: "eceg" }] },
		],
	},
];

export default SIDEBAR_STRUCTURE;
