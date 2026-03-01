"use client";
import { useState } from "react";

export default function Dashboard(){
  const [amount,setAmount]=useState("");
  const [category,setCategory]=useState("");
  const [result,setResult]=useState<any>(null);

  const addTransaction = async ()=>{
    const token = localStorage.getItem("token");

    await fetch(`http://localhost:8000/add-transaction?token=${token}`,{
      method:"POST",
      headers:{"Content-Type":"application/json"},
      body:JSON.stringify({
        amount:parseFloat(amount),
        timestamp:new Date().toISOString(),
        category
      })
    });

    alert("Transaction Added");
  };

  const analyze = async ()=>{
    const token = localStorage.getItem("token");

    const res = await fetch(`http://localhost:8000/analyze?token=${token}`);
    const data = await res.json();
    setResult(data);
  };

  return (
    <div className="min-h-screen bg-black text-white p-10 space-y-6">

      <h1 className="text-3xl">Dashboard</h1>

      <input placeholder="Amount" onChange={e=>setAmount(e.target.value)} className="text-black p-2"/>
      <input placeholder="Category" onChange={e=>setCategory(e.target.value)} className="text-black p-2"/>

      <button onClick={addTransaction} className="bg-indigo-600 px-4 py-2">
        Add Transaction
      </button>

      <button onClick={analyze} className="bg-purple-600 px-4 py-2">
        Analyze Expenses
      </button>

      {result && (
        <div className="mt-6 bg-gray-900 p-6 rounded">
          <h2>Impulse Risk: {result.impulse_risk_score}</h2>
          <h3>Profile: {result.profile}</h3>
          <pre>{JSON.stringify(result.features,null,2)}</pre>
          <ul>
            {result.suggestions?.map((s:any,i:number)=>(
              <li key={i}>• {s}</li>
            ))}
          </ul>
        </div>
      )}

    </div>
  );
}