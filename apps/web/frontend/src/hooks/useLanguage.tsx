import { useTranslation } from "react-i18next";

export const useLanguage = () => {
	const { i18n } = useTranslation();

	const toggleLanguage = () => {
		const newLang = i18n.language === "es" ? "en" : "es";
		i18n.changeLanguage(newLang);
	};

	return {
		currentLanguage: i18n.language,
		toggleLanguage,
		languageLabel: i18n.language === "es" ? "EN" : "ES",
		tooltipLabel:
			i18n.language === "es" ? "Switch to English" : "Cambiar a Español",
	};
};
