import { Card, CardBody, Chip } from "@heroui/react"
import { ShieldCheck } from "lucide-react"

import { useTranslation } from "react-i18next"

const SecurityCard = ({ securityTips }: { securityTips: string[] }) => {
  const { t } = useTranslation()
  return (
    <Card>
      <CardBody className="p-6">
        <div className="flex items-center gap-2 mb-4 text-danger font-bold">
          <ShieldCheck size={20} />
          <h3>{t("security")}</h3>
        </div>
        <div className="flex flex-wrap gap-2">
          {securityTips.map((tip) => (
            <Chip key={tip} variant="flat" color="danger" size="sm">
              {tip}
            </Chip>
          ))}
        </div>
      </CardBody>
    </Card>
  )
}

export default SecurityCard
