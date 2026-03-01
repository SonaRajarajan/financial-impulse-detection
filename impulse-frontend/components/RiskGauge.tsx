"use client";
import { PieChart, Pie, Cell, ResponsiveContainer } from "recharts";

export default function RiskGauge({ risk }: any) {

  const data = [
    { name: "risk", value: risk },
    { name: "rest", value: 100 - risk }
  ];

  return (
    <div className="h-[300px] bg-white/5 p-6 rounded-2xl">

      <h3 className="text-indigo-400 mb-4">Impulse Risk Score</h3>

      <ResponsiveContainer width="100%" height="100%">
        <PieChart>
          <Pie
            data={data}
            innerRadius={70}
            outerRadius={100}
            startAngle={180}
            endAngle={0}
            dataKey="value"
          >
            <Cell fill="#ef4444" />
            <Cell fill="#222" />
          </Pie>
        </PieChart>
      </ResponsiveContainer>

      <div className="text-center text-3xl font-bold mt-[-160px]">
        {risk}%
      </div>
    </div>
  );
}