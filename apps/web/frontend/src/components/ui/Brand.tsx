import { useTranslation } from "react-i18next";


const Brand = ({ className = "" }) => {
  const { t } = useTranslation();
  return (
    <div className={`flex items-center gap-2 ${className}`}>
      <p className="text-3xl font-bold tracking-tighter">{t("brand")}</p>
    </div>
  );
};

export default Brand;
