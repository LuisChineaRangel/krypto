import { Navbar, NavbarBrand, NavbarContent, NavbarMenuToggle } from "@heroui/react";
import { useState } from "react";

import Brand from "@components/ui/Brand";
import DesktopNav from "@components/ui/DesktopNav";
import MobileMenu from "@components/ui/MobileMenu";

import useHeaderTranslations from "@config/Header";

const Header = () => {
	const [isMenuOpen, setIsMenuOpen] = useState(false);
	const { menuItems } = useHeaderTranslations();
	return (
		<Navbar
			shouldHideOnScroll
			isMenuOpen={isMenuOpen}
			onMenuOpenChange={setIsMenuOpen}
			maxWidth="full"
			className="border-b border-divider">
			<NavbarContent className="sm:hidden" justify="start">
				<NavbarMenuToggle className="sm:hidden" />
				<NavbarBrand>
					<Brand />
				</NavbarBrand>
			</NavbarContent>

			<DesktopNav items={menuItems} />

			<NavbarContent justify="end">{/* Space for buttons or profile */}</NavbarContent>

			<MobileMenu items={menuItems} onAction={() => setIsMenuOpen(false)} />
		</Navbar>
	);
};

export default Header;
