import { useState } from "react";
import { motion } from "framer-motion";
import { ChevronRight } from "lucide-react";
import { Button, Tooltip } from "@heroui/react";
import { useSidebarNavigation } from "../hooks/useSidebarNavigation";

interface MenuItem {
	id: string;
	icon?: React.ReactNode;
	label: string;
	children?: MenuItem[];
}

interface SidebarItemProps {
	item: MenuItem;
	isExpanded: boolean;
	setIsExpanded: (value: boolean) => void;
	depth?: number;
}

const SidebarItem: React.FC<SidebarItemProps> = ({
	item,
	isExpanded,
	setIsExpanded,
	depth = 0,
}) => {
	const [isOpen, setIsOpen] = useState(false);
	const hasChildren = item.children && item.children.length > 0;
	const { navigate, getPath } = useSidebarNavigation();

	const paddingX = depth === 0 ? "px-4" : "";
	const paddingLeft = isExpanded ? paddingX : "px-0";
	const marginLeft = isExpanded ? `calc(${depth} * 12px)` : "0px";

	const handlePress = () => {
		if (hasChildren) {
			if (isExpanded) {
				setIsOpen(!isOpen);
			} else {
				setIsExpanded(true);
				setIsOpen(true);
			}
		} else {
			navigate(getPath(item.id));
		}
	};

	return (
		<div className="flex flex-col gap-1 w-full">
			<Tooltip
				content={item.label}
				placement="right"
				isDisabled={isExpanded}
				className="bg-purple-900 text-purple-50">
				<Button
					variant="light"
					className={`justify-start h-12 transition-all ${paddingLeft} ${!isExpanded && "min-w-0 w-12 justify-center"}`}
					style={{ marginLeft: isExpanded ? marginLeft : "0px" }}
					fullWidth={isExpanded}
					onPress={handlePress}>
					{item.icon ?
						<span className="text-danger shrink-0">{item.icon}</span>
					:	isExpanded && <div className="w-1.5 h-1.5 rounded-full bg-danger ml-1 shrink-0" />}

					{isExpanded && (
						<div className="flex justify-between items-center w-full ml-3 overflow-hidden">
							<span
								className={`truncate ${depth > 0 ? "text-sm text-default-600" : "font-medium"}`}>
								{item.label}
							</span>
							{hasChildren && (
								<motion.div animate={{ rotate: isOpen ? 90 : 0 }} className="text-default-400">
									<ChevronRight size={14} />
								</motion.div>
							)}
						</div>
					)}
				</Button>
			</Tooltip>

			{hasChildren && isExpanded && (
				<motion.div
					initial={false}
					animate={{ height: isOpen ? "auto" : 0, opacity: isOpen ? 1 : 0 }}
					className="overflow-hidden flex flex-col gap-1">
					{item.children!.map((child) => (
						<SidebarItem
							key={child.id}
							item={child}
							isExpanded={isExpanded}
							setIsExpanded={setIsExpanded}
							depth={depth + 1}
						/>
					))}
				</motion.div>
			)}
		</div>
	);
};
export default SidebarItem;
