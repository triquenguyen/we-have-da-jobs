import { Terminal } from "lucide-react"

import {
  Alert,
  AlertDescription,
  AlertTitle,
} from "@/components/ui/alert"

export function AlertModal(props: { title: string, description: string }) {
  return (
    <Alert>
      <Terminal className="h-4 w-4" />
      <AlertTitle>{props.title}</AlertTitle>
      <AlertDescription>
        {props.description}
      </AlertDescription>
    </Alert>
  )
}
