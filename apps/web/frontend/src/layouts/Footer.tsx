import { Divider, Link } from "@heroui/react";

const Footer = () => {
	const currentYear = new Date().getFullYear();
	const links = [
		{ name: "Home", href: "#" },
		{ name: "Algorithms", href: "#" },
		{ name: "Docs", href: "#" },
		{ name: "API Python", href: "#" },
	];
	return (
		<footer className="w-full py-10 px-6 bg-background border-t border-default-200">
			<Divider className="my-5" />
			<div className="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-4 gap-8">
				<div className="col-span-1 md:col-span-2">
					<p className="text-2xl font-bold text-foreground tracking-tighter mb-4">
						KRYPTO
					</p>
					<p className="text-default-500 text-sm max-w-xs">
						An all-in-one Python framework for modern cryptography,
						providing modular tools for encryption, decryption,
						hashing, key management, and secure data handling.
					</p>
				</div>

				<div className="flex flex-col gap-2">
					<p className="font-semibold text-foreground mb-2">
						Resources
					</p>
					{links.map((link) => (
						<Link
							key={link.name}
							href={link.href}
							color="foreground"
							size="sm"
						>
							{link.name}
						</Link>
					))}
				</div>
				<div className="flex flex-col gap-2">
					<p className="font-semibold text-foreground mb-2">
						Contact
					</p>
					<p className="text-default-500 text-sm">
						<a
							href="mailto:luischinearangel@gmail.com"
							className="text-foreground"
						>
							Email
						</a>
					</p>
				</div>
			</div>

			<div className="max-w-7xl mx-auto mt-16 flex flex-col md:flex-row justify-between items-center gap-4 text-default-400 text-tiny">
				<p>© {currentYear} Krypto. All rights reserved.</p>
				<div className="flex gap-6">
					<Link
						href="#"
						size="sm"
						color="foreground"
						className="text-tiny opacity-60"
					>
						Privacy
					</Link>
					<Link
						href="#"
						size="sm"
						color="foreground"
						className="text-tiny opacity-60"
					>
						Terms of Use
					</Link>
				</div>
			</div>
		</footer>
	);
};

export default Footer;
