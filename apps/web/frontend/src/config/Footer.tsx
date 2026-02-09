import { useTranslation } from "react-i18next";

const useFooterTranslations = () => {
	const { t } = useTranslation();

	return {
		footerSections: [
			{
				title: t("footer.resources"),
				items: [
					{ name: t("footer.home"), href: "/#" },
					{ name: t("footer.docs"), href: "/docs" },
				],
			},
			{
				title: t("footer.contact"),
				items: [{ name: t("footer.email"), href: "mailto:luischinearangel@gmail.com?subject=Query" }],
			},
		],
		legalLinks: [
			{ name: t("footer.privacy"), href: "#" },
			{ name: t("footer.terms"), href: "#" },
		],
	};
};

export default useFooterTranslations;
