
import { useTranslation } from "react-i18next";

const useHeaderTranslations = () => {
  const { t } = useTranslation();

  return {
    menuItems: [
      { name: t("header.home"), href: "/#" },
      { name: t("header.docs"), href: "/docs" },
      { name: t("header.github"), href: "https://github.com/LuisChineaRangel/krypto " },
    ],
  };
}

export default useHeaderTranslations;
