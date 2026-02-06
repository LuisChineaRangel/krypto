import { Divider, Link } from "@heroui/react";

const Footer = () => {
	const currentYear = new Date().getFullYear();
	const links = [
        {
            title: "Resources",
            items: [
                { name: "Home", href: "/#" },
                { name: "Algorithms", href: "/algorithms" },
                { name: "Docs", href: "/docs" },
                { name: "API Python", href: "/api" },
            ],
        },
        {
            title: "Contact",
            items: [
                { name: "Email", href: "mailto:luischinearangel@gmail.com?subject=Query" },
            ],
        },
	];
	return (
		<footer className="py-10 px-6">
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

                {links.map((section) => (
                    <div key={section.title} className="flex flex-col gap-2">
                        <p className="font-semibold text-foreground mb-2">
                            {section.title}
                        </p>
                        {section.items.map((link) => (
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
                ))}
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
