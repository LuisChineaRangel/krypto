import { Button, Divider } from "@heroui/react";
import { motion } from "framer-motion";
import { ChevronLeft, ChevronRight, ShieldCheck, Key, FileCode, Zap } from "lucide-react";

import { useTranslation } from "react-i18next";
import { useLocalStorage } from "../hooks/useLocalStorage";
import { LanguageSelector } from "../components/ui/LanguageSelector";

import SidebarItem from "./SidebarItem";

const Sidebar = () => {
	const [isExpanded, setIsExpanded] = useLocalStorage("sidebar-expanded", true);
	const { t } = useTranslation();

	const menuItems = [
		{
			id: "symmetric",
			icon: <ShieldCheck size={20} />,
			label: t("sidebar.menu.symmetric"),
			children: [
				{
					id: "block",
					label: t("sidebar.menu.block"),
					children: [{ id: "aes", label: t("sidebar.items.aes") }],
				},
				{ id: "aes", label: t("sidebar.items.aes") },
				{ id: "vigenere", label: t("sidebar.items.vigenere") },
				{
					id: "stream",
					label: t("sidebar.menu.stream"),
					children: [
						{ id: "arc4", label: t("sidebar.items.arc4") },
						{ id: "chacha20", label: t("sidebar.items.chacha20") },
					],
				},
			],
		},
		{
			id: "asymmetric",
			icon: <Key size={20} />,
			label: t("sidebar.menu.asymmetric"),
			children: [
				{
					id: "factorization",
					label: t("sidebar.menu.factorization"),
					children: [{ id: "rsa", label: t("sidebar.items.rsa") }],
				},
				{
					id: "elliptic-curve",
					label: t("sidebar.menu.ellipticCurve"),
					children: [
						{ id: "ecc", label: t("sidebar.items.ecc") },
						{ id: "ecdh", label: t("sidebar.items.ecdh") },
						{ id: "eceg", label: t("sidebar.items.eceg") },
					],
				},
				{
					id: "discrete-log",
					label: t("sidebar.menu.discreteLog"),
					children: [
						{ id: "diffie-hellman", label: t("sidebar.items.diffieHellman") },
						{ id: "elgamal", label: t("sidebar.items.elgamal") },
					],
				},
			],
		},
		{
			id: "cryptographic",
			icon: <Zap size={20} />,
			label: t("sidebar.menu.cryptographic"),
			children: [
				{
					id: "prng",
					label: t("sidebar.menu.prng"),
					children: [
						{ id: "gps-l1-ca", label: t("sidebar.items.gpsL1Ca") },
						{ id: "prga", label: t("sidebar.items.prga") },
					],
				},
			],
		},
		{ id: "python-api", icon: <FileCode size={20} />, label: t("sidebar.menu.pythonApi") },
	];

	return (
		<motion.div
			layout
			animate={{ width: isExpanded ? 300 : 80 }}
			className="hidden md:flex h-full bg-background flex flex-col p-4 relative overflow-y-auto">
			<div
				className={`flex items-center h-12 mb-8 px-2 ${isExpanded ? "justify-between" : "justify-center"}`}>
				<div className="flex items-center gap-3">
					{isExpanded && (
						<motion.span
							initial={{ opacity: 0, x: -10 }}
							animate={{ opacity: 1, x: 0 }}
							className="font-bold text-xl tracking-tighter">
							KRYPTO
						</motion.span>
					)}
				</div>

				<Button
					isIconOnly
					size="sm"
					variant="flat"
					className={`text-default-500 ${!isExpanded && "absolute"}`}
					onPress={() => setIsExpanded(!isExpanded)}>
					{isExpanded ?
						<ChevronLeft size={20} />
					:	<ChevronRight size={20} />}
				</Button>
			</div>

			<nav className="flex flex-col gap-2 flex-grow">
				{menuItems.map((item) => (
					<SidebarItem
						key={item.id}
						item={item}
						isExpanded={isExpanded}
						setIsExpanded={setIsExpanded}
					/>
				))}
			</nav>

			<Divider className="my-4" />

			<LanguageSelector isExpanded={isExpanded} />
		</motion.div>
	);
};

export default Sidebar;
