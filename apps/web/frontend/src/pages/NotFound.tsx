import React from "react";
import { useTranslation } from "react-i18next";

const NotFound: React.FC = () => {
  const { t } = useTranslation();
  return (
    <div className="max-w-4xl mx-auto p-6 text-center">
      <h1 className="text-4xl font-semibold mb-4">{t("notFound.title")}</h1>
      <p className="text-lg text-muted-foreground">{t("notFound.message")}</p>
    </div>
  );
};

export default NotFound;
