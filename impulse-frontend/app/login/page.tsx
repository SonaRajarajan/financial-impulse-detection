"use client";
import { useState } from "react";
import { useRouter } from "next/navigation";

export default function Login() {
  const [email,setEmail]=useState("");
  const [password,setPassword]=useState("");
  const router = useRouter();

  const login = async ()=>{
    const res = await fetch("http://localhost:8000/login",{
      method:"POST",
      headers:{"Content-Type":"application/json"},
      body:JSON.stringify({email,password})
    });
    const data = await res.json();
    localStorage.setItem("token",data.access_token);
    router.push("/dashboard");
  };

  return (
    <div className="h-screen flex flex-col justify-center items-center gap-4 bg-black text-white">
      <h1 className="text-3xl">Login</h1>
      <input placeholder="Email" onChange={e=>setEmail(e.target.value)} className="text-black p-2"/>
      <input type="password" placeholder="Password" onChange={e=>setPassword(e.target.value)} className="text-black p-2"/>
      <button onClick={login} className="bg-purple-600 px-4 py-2">Login</button>
    </div>
  );
}