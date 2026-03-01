"use client";

import { useState, useEffect } from "react";
import ExpenseTable from "../components/ExpenseTable";
import RiskGauge from "../components/RiskGauge";
import FeatureCards from "../components/FeatureCards";
import SpendingTrendChart from "../components/SpendingTrendChart";
import CategoryPieChart from "../components/CategoryPieChart";
import RadarBehaviorChart from "../components/RadarBehaviorChart";
import BehaviourInsights from "../components/BehaviourInsights";

export default function Home() {
  const [expenses, setExpenses] = useState<any[]>([]);
  const [period, setPeriod] = useState("weekly");
  const [result, setResult] = useState<any | null>(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    setExpenses([
      {
        amount: "",
        timestamp: new Date().toISOString().slice(0, 16),
        category: "food",
      },
    ]);
    setResult(null);
  }, [period]);

  const analyze = async () => {
    if (expenses.length < 2) {
      alert("Add at least 2 expenses");
      return;
    }

    setLoading(true);

    try {
      const res = await fetch("http://localhost:8000/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ expenses, period }),
      });

      const data = await res.json();

      if (data.error) {
        alert(data.error);
        setLoading(false);
        return;
      }

      setResult(data);
    } catch (err) {
      alert("Backend not reachable");
    }

    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-black text-white p-10 space-y-16">
      <h1 className="text-4xl text-center font-bold">
        Financial Impulse Intelligence
      </h1>

      {/* PERIOD SELECTOR */}
      <div className="flex justify-center gap-6">
        {["daily", "weekly", "monthly"].map((p) => (
          <button
            key={p}
            onClick={() => setPeriod(p)}
            className={`px-6 py-2 rounded-xl transition-all ${
              period === p
                ? "bg-purple-600 scale-105"
                : "bg-gray-800 border border-gray-700"
            }`}
          >
            {p.toUpperCase()}
          </button>
        ))}
      </div>

      {/* EXPENSE INPUT TABLE */}
      <ExpenseTable
        expenses={expenses}
        setExpenses={setExpenses}
        period={period}
      />

      {/* ANALYZE BUTTON */}
      <div className="text-center">
        <button
          onClick={analyze}
          disabled={loading}
          className="px-10 py-3 bg-gradient-to-r from-purple-600 to-indigo-600 rounded-xl"
        >
          {loading ? "Analyzing..." : "Analyze Behaviour"}
        </button>
      </div>

      {/* RESULTS SECTION */}
      {result && (
        <>
          {/* RISK + FEATURES */}
          <div className="grid grid-cols-12 gap-8 mt-12">
            <div className="col-span-4">
              <RiskGauge risk={result.impulse_risk_score ?? 0} />
            </div>

            <div className="col-span-8">
              <FeatureCards features={result.features ?? {}} />
            </div>
          </div>

          {/* CHARTS */}
          <div className="grid grid-cols-12 gap-8 mt-12">
            <div className="col-span-6">
              <SpendingTrendChart data={expenses} />
            </div>

            <div className="col-span-6">
              <CategoryPieChart data={expenses} />
            </div>
          </div>

          {/* RADAR */}
          <div className="mt-12">
            <RadarBehaviorChart features={result.features ?? {}} />
          </div>

          {/* PROFESSIONAL ANALYSIS + SUGGESTIONS */}
          <BehaviourInsights
           analysis={result.analysis}
           suggestions={result.suggestions}
           detectedBehavior={result.detected_behavior}
           severity={result.severity}
           confidence={result.confidence}
           bannerColor={result.banner_color}
           executiveSummary={result.executive_summary}
           explainability={result.explainability}
          />
        </>
      )}
    </div>
  );
}