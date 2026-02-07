import { Card, CardBody, Chip, Button, Link } from "@heroui/react";
import { motion } from "framer-motion";
import { ExternalLink, Terminal, ShieldCheck, Cpu } from "lucide-react";
import type { CryptographyInfo } from "../../types/cryptography";

interface Props {
	data: CryptographyInfo;
}

const CryptoPageLayout = ({ data }: Props) => {
	return (
		<motion.div
			initial={{ opacity: 0, y: 20 }}
			animate={{ opacity: 1, y: 0 }}
			className="max-w-4xl mx-auto space-y-8 py-10 px-4"
		>
			<div className="flex items-center gap-6 mb-10">
				<div className="p-4 bg-primary/10 rounded-2xl text-primary ring-1 ring-primary/20">
					{data.icon}
				</div>
				<div>
					<h1 className="text-4xl font-extrabold tracking-tight text-foreground">
						{data.title}
					</h1>
					<p className="text-default-500 mt-1">{data.summary}</p>
				</div>
			</div>

			<Card className="shadow-sm">
				<CardBody className="p-6">
					<p className="text-lg leading-relaxed text-default-700">
						{data.description}
					</p>
				</CardBody>
			</Card>

			<div className="grid grid-cols-1 md:grid-cols-2 gap-6">
				<Card>
					<CardBody className="p-6">
						<div className="flex items-center gap-2 mb-4 text-primary font-bold">
							<Cpu size={20} />
							<h3>Especificaciones</h3>
						</div>
						<ul className="space-y-3">
							{data.features.map((f) => (
								<li
									key={f}
									className="text-sm text-default-600 flex items-start gap-2"
								>
									<span className="text-primary mt-1">•</span> {f}
								</li>
							))}
						</ul>
					</CardBody>
				</Card>

				<Card>
					<CardBody className="p-6">
						<div className="flex items-center gap-2 mb-4 text-danger font-bold">
							<ShieldCheck size={20} />
							<h3>Seguridad</h3>
						</div>
						<div className="flex flex-wrap gap-2">
							{data.securityTips.map((tip) => (
								<Chip key={tip} variant="flat" color="danger" size="sm">
									{tip}
								</Chip>
							))}
						</div>
					</CardBody>
				</Card>
			</div>

			<Card className="bg-black border border-white/10 overflow-hidden">
				<div className="bg-white/5 px-4 py-2 flex items-center justify-between border-b border-white/10">
					<div className="flex items-center gap-2">
						<Terminal size={14} className="text-default-400" />
						<span className="text-xs text-default-400 font-mono">
							krypto_lib_example.py
						</span>
					</div>
					<Button
						size="sm"
						variant="light"
						isIconOnly
						className="text-default-400 hover:text-white"
					>
						<ExternalLink size={14} />
					</Button>
				</div>
				<CardBody className="p-0">
					<pre className="p-6 text-sm font-mono text-purple-300 overflow-x-auto leading-6">
						<code>{data.codeExample}</code>
					</pre>
				</CardBody>
			</Card>

			{/* Enlaces de interés */}
			<div className="flex flex-wrap gap-6 pt-4">
				{data.links.map((link) => (
					<Link
						key={link.url}
						href={link.url}
						isExternal
						showAnchorIcon
						className="text-primary font-medium"
					>
						{link.label}
					</Link>
				))}
			</div>
		</motion.div>
	);
};

export default CryptoPageLayout;
