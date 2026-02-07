export interface CryptographyInfo {
    title: string;
    summary?: string;
    description: string;
    icon: React.ReactNode;
    features: string[];
    codeExample: string;
    securityTips: string[];
    links: { label: string; url: string }[];
    mathContext?: string;
}
