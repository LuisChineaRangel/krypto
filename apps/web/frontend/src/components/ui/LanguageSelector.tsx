import { Button } from "@heroui/react";
import { Globe } from "lucide-react";
import { motion } from "framer-motion";
import { useLanguage } from "../../hooks/useLanguage";

interface Props {
	isExpanded: boolean;
}

export const LanguageSelector = ({ isExpanded }: Props) => {
	const { toggleLanguage, languageLabel, tooltipLabel } = useLanguage();

	return (
		<Button
			isIconOnly={!isExpanded}
			size="sm"
			variant="flat"
			className="text-default-500 w-full justify-center transition-all rounded-md"
			onPress={toggleLanguage}
			title={tooltipLabel}
		>
			<Globe size={20} />
			{isExpanded && (
				<motion.span
					initial={{ opacity: 0, x: -10 }}
					animate={{ opacity: 1, x: 0 }}
					className="ml-2 text-sm font-medium"
				>
					{languageLabel}
				</motion.span>
			)}
		</Button>
	);
};
