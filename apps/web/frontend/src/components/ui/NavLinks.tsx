import { NavbarItem, NavbarMenuItem, Link } from "@heroui/react";

export interface MenuLink {
  name: string;
  href: string;
}

interface NavLinksProps {
  links: MenuLink[];
  isMobile?: boolean;
  onAction?: () => void;
}

const NavLinks = ({ links, isMobile = false, onAction }: NavLinksProps) => {
  return (
    <>
      {links.map((item) => (
        <NavbarItem key={item.name} as={isMobile ? NavbarMenuItem : "li"}>
          <Link
            href={item.href}
            size="lg"
            className={isMobile ? "w-full" : "px-2"}
            color="foreground"
            onClick={onAction}
          >
            {item.name}
          </Link>
        </NavbarItem>
      ))}
    </>
  );
};

export default NavLinks;
