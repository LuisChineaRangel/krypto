import { Button } from "@heroui/react";
import { motion } from "framer-motion";
import {
	ChevronLeft,
	ChevronRight,
	ShieldCheck,
	Key,
	FileCode,
	Zap,
} from "lucide-react";

import SidebarItem from "./SidebarItem";
import { useLocalStorage } from "../hooks/useLocalStorage";

const Sidebar = () => {
	const [isExpanded, setIsExpanded] = useLocalStorage(
		"sidebar-expanded",
		true,
	);

	const menuItems = [
		{
			id: "symmetric",
			icon: <ShieldCheck size={20} />,
			label: "Symmetric Encryption",
			children: [
				{ id: "aes", label: "AES" },
				{ id: "vigenere", label: "Vigenere" },
				{
					id: "stream",
					label: "Stream Ciphers",
					children: [
						{ id: "arc4", label: "ARC4" },
						{ id: "chacha20", label: "ChaCha20" },
					],
				},
			],
		},
		{
			id: "asymmetric",
			icon: <Key size={20} />,
			label: "Asymmetric Encryption",
			children: [
				{
					id: "factorization",
					label: "Factorization",
					children: [{ id: "rsa", label: "RSA" }],
				},
				{
					id: "elliptic-curve",
					label: "Elliptic Curve",
					children: [
						{ id: "ecc", label: "ECC" },
						{ id: "ecdh", label: "ECDH" },
						{ id: "eceg", label: "ECEG" },
					],
				},
				{
					id: "discrete-log",
					label: "Discrete Logarithm",
					children: [
						{ id: "diffie-hellman", label: "Diffie-Hellman" },
						{ id: "elgamal", label: "ElGamal" },
					],
				},
			],
		},
		{
			id: "cryptographic",
			icon: <Zap size={20} />,
			label: "Cryptographic Primitives",
			children: [
				{
					id: "prng",
					label: "PRNG",
					children: [
						{ id: "gps-l1-ca", label: "GPS L1 CA" },
						{ id: "prga", label: "PRGA" },
					],
				},
			],
		},
		{ id: "python-api", icon: <FileCode size={20} />, label: "Python API" },
	];

	return (
		<motion.div
			layout
			animate={{ width: isExpanded ? 300 : 80 }}
			className="hidden md:flex h-full bg-background flex flex-col p-4 relative overflow-y-auto"
		>
			<div
				className={`flex items-center h-12 mb-8 px-2 ${isExpanded ? "justify-between" : "justify-center"}`}
			>
				<div className="flex items-center gap-3">
					{isExpanded && (
						<motion.span
							initial={{ opacity: 0, x: -10 }}
							animate={{ opacity: 1, x: 0 }}
							className="font-bold text-xl tracking-tighter"
						>
							KRYPTO
						</motion.span>
					)}
				</div>

				<Button
					isIconOnly
					size="sm"
					variant="flat"
					className={`text-default-500 ${!isExpanded && "absolute"}`}
					onPress={() => setIsExpanded(!isExpanded)}
				>
					{isExpanded ? (
						<ChevronLeft size={20} />
					) : (
						<ChevronRight size={20} />
					)}
				</Button>
			</div>

			<nav className="flex flex-col gap-2 flex-grow">
				{menuItems.map((item) => (
					<SidebarItem
						key={item.id}
						item={item}
						isExpanded={isExpanded}
					/>
				))}
			</nav>
		</motion.div>
	);
};

export default Sidebar;
