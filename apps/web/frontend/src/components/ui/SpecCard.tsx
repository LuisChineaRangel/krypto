import { Card, CardBody } from "@heroui/react"
import { Cpu } from "lucide-react"

import { useTranslation } from "react-i18next"

const SpecCard = ({ features }: { features: string[] }) => {
  const { t } = useTranslation()
  return (
    <Card>
      <CardBody className="p-6">
        <div className="flex items-center gap-2 mb-4 text-primary font-bold">
          <Cpu size={20} />
          <h3>{t("specifications")}</h3>
        </div>
        <ul className="space-y-3">
          {features.map((f) => (
            <li key={f} className="text-sm text-default-600 flex items-start gap-2">
              <span className="text-primary mt-1">•</span> {f}
            </li>
          ))}
        </ul>
      </CardBody>
    </Card>
  )
}

export default SpecCard
