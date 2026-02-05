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
		{ name: "Inicio", href: "#" },
		{ name: "Proyectos", href: "#" },
		{ name: "Algoritmos", href: "#" },
		{ name: "Documentación", href: "#" },
		{ name: "GitHub", href: "#" },
	];

	return (
		<Navbar shouldHideOnScroll onMenuOpenChange={setIsMenuOpen} isBordered maxWidth="xl">
			<NavbarContent>
				<NavbarMenuToggle
					aria-label={isMenuOpen ? "Close menu" : "Open menu"}
					className="sm:hidden"
				/>
				<NavbarBrand className="md:hidden">
					<p className="text-3xl font-bold">KRYPTO</p>
				</NavbarBrand>
			</NavbarContent>

			<NavbarContent className="hidden sm:flex gap-4 flex-1" justify="center">
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
					<Button as={Link} color="danger" href="#" variant="flat">
						Mi Librería
					</Button>
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
