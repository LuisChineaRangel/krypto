import Header from "./Header";
import Footer from "./Footer";
import Sidebar from "./Sidebar";

interface MainLayoutProps {
	children: React.ReactNode;
}

const MainLayout = ({ children }: MainLayoutProps) => {
	return (
		<div className="flex min-h-screen w-full bg-background text-foreground">
			<aside className="sticky top-0 h-screen">
				<Sidebar />
			</aside>

			<div className="flex flex-col flex-1">
				<Header />
				<main className="flex flex-col flex-grow">{children}</main>
				<Footer />
			</div>
		</div>
	);
};

export default MainLayout;
