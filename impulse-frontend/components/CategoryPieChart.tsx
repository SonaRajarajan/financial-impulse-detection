"use client";

import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  ResponsiveContainer
} from "recharts";

export default function CategoryPieChart({ data }: any) {
  if (!data || data.length === 0) return null;

  // Group by category
  const grouped: any = {};
  data.forEach((item: any) => {
    const key = item.category;
    grouped[key] = (grouped[key] || 0) + Number(item.amount);
  });

  const chartData = Object.keys(grouped).map((key) => ({
    name: key,
    value: grouped[key],
  }));

  // 🎨 Dark-friendly premium palette (no red dominance)
  const COLORS = [
    "#2563eb", // blue
    "#7c3aed", // violet
    "#0891b2", // cyan
    "#14b8a6", // teal
    "#f59e0b", // amber
  ];

  return (
    <div className="bg-black rounded-2xl p-8 border border-gray-900">

      {/* 🔵 Heading */}
      <h2 className="text-lg text-blue-400 mb-6">
        Category Distribution
      </h2>

      <ResponsiveContainer width="100%" height={350}>
        <PieChart>
          <Pie
            data={chartData}
            dataKey="value"
            nameKey="name"
            innerRadius={90}
            outerRadius={130}
            paddingAngle={4}
            stroke="#0f172a"
            strokeWidth={2}
          >
            {chartData.map((entry: any, index: number) => (
              <Cell
                key={`cell-${index}`}
                fill={COLORS[index % COLORS.length]}
              />
            ))}
          </Pie>

          {/* ✅ FIXED TOOLTIP */}
          <Tooltip
            formatter={(value: any) =>
              `₹ ${Number(value).toLocaleString()}`
            }
            contentStyle={{
              backgroundColor: "#0f172a",
              border: "1px solid #2563eb",
              borderRadius: "12px",
              color: "#ffffff",
              boxShadow: "0 0 20px rgba(37,99,235,0.3)",
            }}
            itemStyle={{
              color: "#ffffff",
              fontWeight: 500,
            }}
            labelStyle={{
              color: "#ffffff",
              fontWeight: 600,
            }}
          />
        </PieChart>
      </ResponsiveContainer>
    </div>
  );
}