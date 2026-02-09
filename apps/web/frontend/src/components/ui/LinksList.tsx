import { Link } from "@heroui/react"

const LinksList = ({ links }: { links: { label: string; url: string }[] }) => {
  return (
    <div className="flex flex-wrap gap-6 pt-4">
      {links.map((link) => (
        <Link key={link.url} href={link.url} isExternal showAnchorIcon className="text-primary font-medium">
          {link.label}
        </Link>
      ))}
    </div>
  )
}

export default LinksList
