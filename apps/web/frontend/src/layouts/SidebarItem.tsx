import { useState } from "react";
import { useSidebarNavigation } from "../hooks/useSidebarNavigation";
import { motion } from "framer-motion";
import { ChevronRight } from "lucide-react";
import { Button, Tooltip } from "@heroui/react";

interface SidebarItemProps {
    id: string;
    icon?: React.ReactNode;
    label: string;
    children?: SidebarItemProps[];
}

const SidebarItem: React.FC<{
	item: SidebarItemProps;
	isExpanded: boolean;
	depth?: number;
}> = ({
	item,
	isExpanded,
	depth = 0,
}) => {
	const [isOpen, setIsOpen] = useState(false);
	const hasChildren = item.children && item.children.length > 0;
	const { navigate, getPath } = useSidebarNavigation();

	// Estilo de indentado dinámico basado en la profundidad
	const paddingLeft = isExpanded ? (depth === 0 ? "px-4" : "") : "px-0";
	const marginLeft = isExpanded ? `calc(${depth} * 12px)` : "0px";

	return (
		<div className="flex flex-col gap-1 w-full">
			<Tooltip
				content={item.label}
				placement="right"
				isDisabled={isExpanded}
				className="bg-purple-900 text-purple-50"
			>
				<Button
					variant="light"
					// Ajustamos el estilo según la profundidad
					className={`justify-start h-12 transition-all ${paddingLeft} ${!isExpanded && "min-w-0 w-12 justify-center"}`}
					style={{ marginLeft: isExpanded ? marginLeft : "0px" }}
					fullWidth={isExpanded}
					onPress={() => {
						if (hasChildren && isExpanded) {
							setIsOpen(!isOpen);
						} else {
							navigate(getPath(item.id));
						}
					}}
				>
					{/* Solo mostramos icono si existe (normalmente el nivel 0 lo tiene) */}
					{item.icon ? (
						<span className="text-danger shrink-0">
							{item.icon}
						</span>
					) : (
						// Un puntito decorativo para hijos sin icono
						isExpanded && (
							<div className="w-1.5 h-1.5 rounded-full bg-purple-500/50 ml-1 shrink-0" />
						)
					)}

					{isExpanded && (
						<div className="flex justify-between items-center w-full ml-3 overflow-hidden">
							<span
								className={`truncate ${depth > 0 ? "text-sm text-default-600" : "font-medium"}`}
							>
								{item.label}
							</span>
							{hasChildren && (
								<motion.div
									animate={{ rotate: isOpen ? 90 : 0 }}
									className="text-default-400"
								>
									<ChevronRight size={14} />
								</motion.div>
							)}
						</div>
					)}
				</Button>
			</Tooltip>

			{/* RENDERIZADO RECURSIVO */}
			{hasChildren && isExpanded && (
				<motion.div
					initial={false}
					animate={{
						height: isOpen ? "auto" : 0,
						opacity: isOpen ? 1 : 0,
					}}
					className="overflow-hidden flex flex-col gap-1"
				>
					{item.children!.map((child) => (
						<SidebarItem
							key={child.id}
							item={child}
							isExpanded={isExpanded}
							depth={depth + 1} // Aumentamos la profundidad
						/>
					))}
				</motion.div>
			)}
		</div>
	);
};
export default SidebarItem;
