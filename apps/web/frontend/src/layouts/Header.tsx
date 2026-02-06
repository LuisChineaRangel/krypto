import {
	Button,
	Link,
	Navbar,
	NavbarBrand,
	NavbarContent,
	NavbarItem,
	NavbarMenu,
	NavbarMenuItem,
	NavbarMenuToggle,
} from "@heroui/react";
import { useState } from "react";

const Header = () => {
	const [isMenuOpen, setIsMenuOpen] = useState(false);
	const menuItems = [
		{ name: "Home", href: "/#" },
		{ name: "Algorithms", href: "/algorithms" },
		{ name: "Documentation", href: "/docs" },
		{ name: "GitHub", href: "https://github.com/LuisChineaRangel/krypto" },
	];

	return (
		<Navbar shouldHideOnScroll isBlurred={false} onMenuOpenChange={setIsMenuOpen} maxWidth="full" >
			<NavbarContent className="md:hidden">
				<NavbarMenuToggle
					aria-label={isMenuOpen ? "Close menu" : "Open menu"}
					className="sm:hidden"
				/>
				<NavbarBrand>
					<p className="text-3xl font-bold">KRYPTO</p>
				</NavbarBrand>
			</NavbarContent>

			<NavbarContent className="hidden sm:flex gap-4 flex-1" justify="start">
				{menuItems.map((item) => (
					<NavbarItem key={item.name}>
						<Link href={item.href} size="lg">
							{item.name}
						</Link>
					</NavbarItem>
				))}
			</NavbarContent>

			<NavbarContent className="hidden sm:flex items-center" justify="end">
				<NavbarItem>
					{/* <Button as={Link} color="danger" href="https://github.com/LuisChineaRangel/krypto" variant="flat">
						Mi Librería
					</Button> */}
				</NavbarItem>
			</NavbarContent>

			<NavbarMenu>
				{menuItems.map((item) => (
					<NavbarMenuItem key={item.name}>
						<Link
							href={item.href}
							size="lg"
							className="w-full"
							onClick={() => setIsMenuOpen(false)}
						>
							{item.name}
						</Link>
					</NavbarMenuItem>
				))}
			</NavbarMenu>
		</Navbar>
	);
};

export default Header;
