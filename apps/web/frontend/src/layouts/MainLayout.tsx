import Header from "./Header";
import Footer from "./Footer";
import Sidebar from "./Sidebar";

interface MainLayoutProps {
	children: React.ReactNode;
}

const MainLayout = ({ children }: MainLayoutProps) => {
	return (
		<div className="flex h-screen w-full overflow-hidden bg-background text-foreground">
			<Sidebar />
			<div className="flex flex-col flex-1 h-full overflow-hidden">
				<Header />
				<main className="flex-1 overflow-y-auto">
					<div className="max-w-7xl mx-auto w-full flex flex-col min-h-full">
						<div className="flex-grow">{children}</div>
						<Footer />
					</div>
				</main>
			</div>
		</div>
	);
};

export default MainLayout;
