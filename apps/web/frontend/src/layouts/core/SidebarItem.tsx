import { useState } from "react";
import { motion } from "framer-motion";
import { ChevronRight } from "lucide-react";
import { useTranslation } from "react-i18next";
import { Button, Tooltip } from "@heroui/react";
import { useSidebarNavigation } from "@hooks/useSidebarNavigation";

interface MenuItem {
  id: string;
  icon?: React.ReactNode;
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
  const { navigate, getPath } = useSidebarNavigation();
  const { t } = useTranslation();

  const hasChildren = !!item.children?.length;
  const label = hasChildren
    ? t(`sidebar.categories.${item.id}`, { defaultValue: item.id })
    : t(`sidebar.primitives.${item.id}`, { defaultValue: item.id });

  const handlePress = () => {
    if (hasChildren) {
      setIsExpanded(true);
      setIsOpen(!isOpen || !isExpanded);
    } else {
      navigate(getPath(item.id));
    }
  };

  return (
    <div className="flex flex-col gap-1 w-full">
      <Tooltip
        content={label}
        placement="right"
        isDisabled={isExpanded}
        className="bg-default-800 text-white font-medium"
      >
        <Button
          variant="light"
          onPress={handlePress}
          fullWidth={isExpanded}
          className={`justify-start h-12 min-w-0 transition-all ${
            isExpanded ? "px-4" : "w-12 justify-center px-0"
          }`}
          style={{ paddingLeft: isExpanded ? `${depth * 12 + 16}px` : "" }}
        >
          <div className="shrink-0 flex items-center justify-center">
            {item.icon ? (
              <span className="text-danger">{item.icon}</span>
            ) : (
              isExpanded && <div className="w-1.5 h-1.5 rounded-full bg-danger ml-1" />
            )}
          </div>

          {isExpanded && (
            <div className="flex justify-between items-center w-full ml-3 overflow-hidden">
              <span
                className={`truncate ${
                  depth > 0 ? "text-sm text-default-600" : "font-medium"
                }`}
              >
                {label}
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

      {hasChildren && isExpanded && (
        <motion.div
          initial={false}
          animate={{ height: isOpen ? "auto" : 0, opacity: isOpen ? 1 : 0 }}
          transition={{ duration: 0.2, ease: "easeInOut" }}
          className="overflow-hidden flex flex-col gap-1"
        >
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
