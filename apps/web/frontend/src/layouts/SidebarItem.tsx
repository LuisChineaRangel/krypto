import { useState } from "react";
import { useSidebarNavigation } from "../hooks/useSidebarNavigation";
import { motion } from "framer-motion";
import { ChevronRight } from "lucide-react";
import { Button, Tooltip } from "@heroui/react";

interface SidebarItemProps {
    id: string;
    icon: React.ReactNode;
    label: string;
    children?: { id: string; label: string }[];
}

const SidebarItem : React.FC<{ item: SidebarItemProps; isExpanded: boolean }> = ({ item, isExpanded }) => {
  const [isOpen, setIsOpen] = useState(false);
  const hasChildren = item.children && item.children.length > 0;
  const { navigate, getPath } = useSidebarNavigation();

  return (
    <div className="flex flex-col gap-1">
      <Tooltip content={item.label} placement="right" isDisabled={isExpanded} className="text-purple-50">
        <Button
          variant="light"
          className={`justify-start h-12 ${isExpanded ? "px-4" : "min-w-0 w-12 px-0 justify-center"}`}
          fullWidth={isExpanded}
          onPress={() => {
            if (hasChildren) {
              setIsOpen(!isOpen);
            } else {
              navigate(getPath(item.id));
            }
          }}
        >
          <span className="text-danger shrink-0">{item.icon}</span>
          {isExpanded && (
            <div className="flex justify-between items-center w-full ml-3">
              <span className="font-medium">{item.label}</span>
              {hasChildren && (
                <motion.div animate={{ rotate: isOpen ? 90 : 0 }}>
                  <ChevronRight size={16} />
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
          className="overflow-hidden flex flex-col pl-10 gap-1"
        >
          {item.children!.map((child) => (
            <Button
              key={child.id}
              size="sm"
              variant="light"
              className="justify-start h-9 text-default-500 font-normal"
              onPress={() => navigate(getPath(child.id))}
            >
              {child.label}
            </Button>
          ))}
        </motion.div>
      )}
    </div>
  );
};

export default SidebarItem;
