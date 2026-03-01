"use client";

import {
  RadarChart,
  Radar,
  PolarGrid,
  PolarAngleAxis,
  PolarRadiusAxis,
  ResponsiveContainer
} from "recharts";

export default function RadarBehaviorChart({ features }: any) {

  if (!features || Object.keys(features).length === 0) return null;

  const data = Object.entries(features).map(([key, value]: any) => ({
    feature: key,
    value: value
  }));

  return (
    <div className="bg-white/5 p-8 rounded-2xl border border-white/10">
      <h2 className="text-xl mb-6 text-indigo-400">
        Behaviour Signal Radar
      </h2>

      <ResponsiveContainer width="100%" height={350}>
        <RadarChart data={data}>
          <PolarGrid stroke="#555" />
          <PolarAngleAxis dataKey="feature" stroke="#aaa" />
          <PolarRadiusAxis stroke="#666" />
          <Radar
            dataKey="value"
            stroke="#6366f1"
            fill="#6366f1"
            fillOpacity={0.4}
          />
        </RadarChart>
      </ResponsiveContainer>
    </div>
  );
}