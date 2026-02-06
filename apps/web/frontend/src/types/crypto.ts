export interface CryptoMethod {
    title: string;
    description: string;
    icon: React.ReactNode;
    features: string[];
    codeExample: string;
    securityTips: string[];
    links: { label: string; url: string }[];
    mathContext?: string;
}
