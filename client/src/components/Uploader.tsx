import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Button } from "@/components/ui/button"

const Uploader = () => {


  return (
    <div className="w-full max-w-sm flex flex-col gap-2">
      <Label htmlFor="picture">Upload your resume</Label>
      <div className="flex items-center justify-center gap-2">
        <Input id="picture" type="file" />
        <Button type="submit" >Upload</Button>
      </div>
    </div>
  )
}

export default Uploader