import { Button, Divider } from "@heroui/react";
import { motion } from "framer-motion";
import { ChevronLeft, ChevronRight } from "lucide-react";

import { useLocalStorage } from "../../hooks/useLocalStorage";
import LanguageSelector from "@components/ui/LanguageSelector";

import SIDEBAR_STRUCTURE from "@config/Sidebar";
import SidebarItem from "@layouts/core/SidebarItem";
import Brand from "@components/ui/Brand";

const Sidebar = () => {
	const [isExpanded, setIsExpanded] = useLocalStorage("sidebar-expanded", true);

	return (
		<motion.div
			layout
			animate={{ width: isExpanded ? 300 : 80 }}
			className="hidden sm:flex h-full bg-background flex-col p-4 relative overflow-y-auto border-r border-divider">
			<div
				className={`flex items-center h-12 mb-8 px-2 ${isExpanded ? "justify-between" : "justify-center"}`}>
				{isExpanded && <Brand />}

				<Button isIconOnly size="sm" variant="light" onPress={() => setIsExpanded(!isExpanded)}>
					{isExpanded ?
						<ChevronLeft size={20} />
					:	<ChevronRight size={20} />}
				</Button>
			</div>

			<nav className="flex flex-col gap-2 flex-grow">
				{SIDEBAR_STRUCTURE.map((item) => (
					<SidebarItem
						key={item.id}
						item={item}
						isExpanded={isExpanded}
						setIsExpanded={setIsExpanded}
					/>
				))}
			</nav>

			<Divider className="my-4" />
			<LanguageSelector isExpanded={isExpanded} />
		</motion.div>
	);
};

export default Sidebar;
