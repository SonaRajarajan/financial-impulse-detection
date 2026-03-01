"use client";

import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid,
} from "recharts";

export default function SpendingTrendChart({ data }: any) {

  const chartData = data.map((item: any) => ({
    date: new Date(item.timestamp).toLocaleDateString(),
    amount: Number(item.amount),
  }));

  return (
    <div className="bg-gradient-to-br from-white/5 to-white/10
                    backdrop-blur-lg p-6 rounded-2xl
                    border border-white/10 shadow-xl
                    h-[350px] w-full">

      <h3 className="text-indigo-400 mb-4">Spending Trend</h3>

      <div className="h-[260px] w-full">
        <ResponsiveContainer width="100%" height="100%">
          <LineChart data={chartData}>
            <CartesianGrid strokeDasharray="3 3" stroke="#222" />
            <XAxis dataKey="date" stroke="#aaa" />
            <YAxis stroke="#aaa" />
            <Tooltip
              contentStyle={{
                backgroundColor: "#111",
                border: "1px solid #444",
                color: "#fff",
              }}
            />
            <Line
              type="monotone"
              dataKey="amount"
              stroke="#6366f1"
              strokeWidth={3}
              dot={{ r: 5 }}
            />
          </LineChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}