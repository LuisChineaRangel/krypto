import { NavbarMenu, NavbarMenuItem, Link } from "@heroui/react";

interface MenuItem {
	name: string;
	href: string;
}

const MobileMenu = ({ items, onAction }: { items: MenuItem[]; onAction: () => void }) => (
	<NavbarMenu className="pt-6">
		{items.map((item) => (
			<NavbarMenuItem key={item.name}>
				<Link
					href={item.href}
					size="lg"
					className="w-full py-2"
					color="foreground"
					onClick={onAction}>
					{item.name}
				</Link>
			</NavbarMenuItem>
		))}
	</NavbarMenu>
);

export default MobileMenu;
