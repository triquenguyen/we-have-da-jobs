"use client"

import Image from "next/image";
import { Button } from "@/components/ui/button";
import Uploader from "@/components/Uploader";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { useState } from "react";
import { Alert } from "@/components/ui/alert";
import { AlertModal } from "@/components/AlertModal";
import { title } from "process";

export default function Home() {
  const [file, setFile] = useState<File | null>(null);
  const [error, setError] = useState<boolean>(false);
  const [message, setMessage] = useState<any>({ title: "", description: "" });
  const [result, setResult] = useState<string>("");

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const selectedFile = e.target.files?.[0];
    if (selectedFile) {
      setFile(selectedFile);
      console.log(selectedFile);
    }
  }

  const handleUpload = async () => {
    if (!file) {
      setError(true);
      setMessage({ title: "Error!", description: "Please upload a file" });
      return;
    }

    try {
      const data = new FormData();
      data.append('file', file);

      const res = await fetch("http://127.0.0.1:5000/upload", {
        method: "POST",
        body: data // Send the FormData object
      }).then(response => response.json());

      // const responseData = await res
      // // setResult(responseData); // Set result from response

      console.log(res);
      setError(false);
      console.log(file);
    } catch (e: any) {
      setError(true);
      setMessage({ title: "Error!", description: e.message });
      console.error(e);
    }
  }

  return (
    <div>
      <div className="w-full max-w-sm flex flex-col gap-2">
        <Label htmlFor="picture">Upload your resume</Label>
        <div className="flex items-center justify-center gap-2">
          <Input id="picture" type="file" onChange={handleFileChange} />
          <Button type="submit" onClick={handleUpload}>Upload</Button>
        </div>

        <div>
          result: {result}
        </div>

        {error && (
          <AlertModal title={message.title} description={message.description} />
        )}
      </div>
    </div>
  );
}