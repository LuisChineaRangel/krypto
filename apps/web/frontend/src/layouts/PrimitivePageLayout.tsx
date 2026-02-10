import { motion } from "framer-motion";
import { Lock } from "lucide-react";

import SpecCard from "@components/ui/SpecCard";
import LinksList from "@components/ui/LinksList";
import SecurityCard from "@components/ui/SecurityCard";
import CodeExampleCard from "@components/ui/CodeExampleCard";

export interface PrimitivePageData {
	title: string;
	summary?: string;
	description: string;
	icon?: React.ReactNode | string;
	features: string[];
	codeExample: string;
	securityTips: string[];
	links: { label: string; url: string }[];
	mathContext?: string;
}

export type PrimitivePageProps = { data: PrimitivePageData };

const renderIcon = (icon?: React.ReactNode | string) => {
	if (!icon) return null;
	if (typeof icon === "string") return <Lock size={32} />;
	return icon;
};

const PrimitivePageLayout = ({ data }: PrimitivePageProps) => {
	return (
		<motion.div
			initial={{ opacity: 0, y: 20 }}
			animate={{ opacity: 1, y: 0 }}
			className="max-w-4xl mx-auto space-y-8 py-6 md:py-10 px-4">
			<header className="flex flex-col sm:flex-row items-center sm:items-start gap-4 sm:gap-6 mb-8 md:mb-10 text-center sm:text-left">
				<div className="p-4 bg-primary/10 rounded-2xl text-primary border border-primary/20 shrink-0">
					{renderIcon(data.icon)}
				</div>

				<div className="space-y-2">
					<h1 className="text-3xl md:text-4xl font-extrabold tracking-tight">{data.title}</h1>
					{data.summary && (
						<p className="text-default-500 text-sm md:text-base max-w-lg">{data.summary}</p>
					)}
				</div>
			</header>

			<main className="space-y-6">
				<section className="p-4 md:p-6 bg-content1 rounded-3xl border border-divider">
					<p className="text-base md:text-lg leading-relaxed text-default-700">
						{data.description}
					</p>
				</section>

				<div className="grid grid-cols-1 md:grid-cols-2 gap-4 md:gap-6">
					<SpecCard features={data.features} />
					<SecurityCard securityTips={data.securityTips} />
				</div>

				<CodeExampleCard codeExample={data.codeExample} />

				<LinksList links={data.links} />
			</main>
		</motion.div>
	);
};

export default PrimitivePageLayout;
