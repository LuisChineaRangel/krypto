import { useState } from "react";
import { Button, Tooltip, Divider } from "@heroui/react";
import { motion } from "framer-motion";
import {
  ChevronLeft,
  ChevronRight,
  ShieldCheck,
  Key,
  Hash,
  Settings,
  FileCode
} from "lucide-react";

const Sidebar = () => {
  const [isExpanded, setIsExpanded] = useState(true);

  const menuItems = [
    { id: "symmetric", icon: <ShieldCheck size={20} />, label: "Cifrado Simétrico" },
    { id: "asymmetric", icon: <Key size={20} />, label: "Cifrado Asimétrico" },
    { id: "hash", icon: <Hash size={20} />, label: "Funciones Hash" },
    { id: "python-api", icon: <FileCode size={20} />, label: "API Python" },
  ];

  return (
    <motion.div
      animate={{ width: isExpanded ? 240 : 80 }}
      className="hidden md:flex h-full bg-background border-r border-divider flex flex-col p-4 relative"
    >
      <div className={`flex items-center mb-8 px-2 ${isExpanded ? "justify-between" : "justify-center"}`}>
        <div className="flex items-center gap-3">
          {/* <div className="p-2 bg-danger rounded-lg text-white shrink-0">
            <ShieldCheck size={24} />
          </div> */}
          {isExpanded && (
            <motion.span
              initial={{ opacity: 0, x: -10 }}
              animate={{ opacity: 1, x: 0 }}
              className="font-bold text-xl tracking-tighter"
            >
              KRYPTO
            </motion.span>
          )}
        </div>

        <Button
          isIconOnly
          size="sm"
          variant="flat"
          className={`text-default-500 ${!isExpanded && "absolute top-4"}`}
          onPress={() => setIsExpanded(!isExpanded)}
        >
          {isExpanded ? <ChevronLeft size={20} /> : <ChevronRight size={20} />}
        </Button>
      </div>

      <nav className="flex flex-col gap-2 flex-grow">
        {menuItems.map((item) => (
          <Tooltip
            key={item.id}
            content={item.label}
            placement="right"
            isDisabled={isExpanded}
          >
            <Button
              variant="light"
              className={`justify-start h-12 ${isExpanded ? "px-4" : "min-w-0 w-12 px-0 justify-center"}`}
              fullWidth={isExpanded}
            >
              <span className="text-danger shrink-0">{item.icon}</span>
              {isExpanded && (
                <motion.span
                  initial={{ opacity: 0, x: -10 }}
                  animate={{ opacity: 1, x: 0 }}
                  className="ml-3 font-medium overflow-hidden whitespace-nowrap"
                >
                  {item.label}
                </motion.span>
              )}
            </Button>
          </Tooltip>
        ))}
      </nav>

      <Divider className="my-4" />

      <Button
        variant="light"
        className={`justify-start h-12 ${isExpanded ? "px-4" : "min-w-0 w-12 px-0 justify-center"}`}
      >
        <Settings size={20} className="text-default-500 shrink-0" />
        {isExpanded && (
          <span className="ml-3 text-default-500 overflow-hidden whitespace-nowrap">
            Configuración
          </span>
        )}
      </Button>
    </motion.div>
  );
};

export default Sidebar;
