import { Divider, Link } from "@heroui/react";
import { useTranslation } from "react-i18next";

import Brand from "@components/ui/Brand";
import useFooterTranslations from "@config/Footer";

const Footer = () => {
	const { t } = useTranslation();
	const currentYear = new Date().getFullYear();
	const { footerSections: FOOTER_SECTIONS, legalLinks: LEGAL_LINKS } = useFooterTranslations();
	return (
		<footer className="py-10 px-4 md:px-6">
			<Divider className="mb-10" />

			<div className="max-w-7xl mx-auto grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-10">
				<div className="sm:col-span-2 space-y-4">
					<Brand />
					<p className="text-default-500 text-sm max-w-xs leading-relaxed">
						{t("footer.description")}
					</p>
				</div>

				{FOOTER_SECTIONS.map((section) => (
					<div key={section.title} className="flex flex-col gap-3">
						<p className="font-semibold text-foreground">{section.title}</p>
						{section.items.map((link) => (
							<Link
								key={link.name}
								href={link.href}
								color="foreground"
								size="sm"
								className="opacity-70 hover:opacity-100 transition-opacity">
								{link.name}
							</Link>
						))}
					</div>
				))}
			</div>

			<div className="max-w-7xl mx-auto mt-16 pt-8 border-t border-divider flex flex-col md:flex-row justify-between items-center gap-4 text-tiny text-default-400">
				<p>{t("footer.copyright", { year: currentYear })}</p>

				<div className="flex gap-6">
					{LEGAL_LINKS.map((link) => (
						<Link
							key={link.name}
							href={link.href}
							size="sm"
							color="foreground"
							className="text-tiny opacity-60 hover:opacity-100">
							{link.name}
						</Link>
					))}
				</div>
			</div>
		</footer>
	);
};

export default Footer;
