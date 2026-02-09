import { NavbarContent, NavbarItem, Link } from "@heroui/react";

interface NavItem {
	name: string;
	href: string;
}

const DesktopNav = ({ items }: { items: NavItem[] }) => (
	<NavbarContent className="hidden sm:flex gap-6" justify="start">
		{items.map((item) => (
			<NavbarItem key={item.name}>
				<Link
					href={item.href}
					size="lg"
					color="foreground"
					className="hover:opacity-70 transition-opacity">
					{item.name}
				</Link>
			</NavbarItem>
		))}
	</NavbarContent>
);

export default DesktopNav;
