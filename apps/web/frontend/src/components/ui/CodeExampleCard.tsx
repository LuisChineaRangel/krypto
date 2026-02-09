import { Card, CardBody, Button } from "@heroui/react"
import { ExternalLink, Terminal } from "lucide-react"

const CodeExampleCard = ({ codeExample }: { codeExample: string }) => {
  return (
    <Card className="bg-black border border-white/10 overflow-hidden">
      <div className="bg-white/5 px-4 py-2 flex items-center justify-between border-b border-white/10">
        <div className="flex items-center gap-2">
          <Terminal size={14} className="text-default-400" />
          <span className="text-xs text-default-400 font-mono">krypto_lib_example.py</span>
        </div>
        <Button size="sm" variant="light" isIconOnly className="text-default-400 hover:text-white">
          <ExternalLink size={14} />
        </Button>
      </div>
      <CardBody className="p-0">
        <pre className="p-6 text-sm font-mono text-purple-300 overflow-x-auto leading-6">
          <code>{codeExample}</code>
        </pre>
      </CardBody>
    </Card>
  )
}

export default CodeExampleCard
