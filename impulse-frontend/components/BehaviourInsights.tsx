"use client";

export default function BehaviourInsights({
  analysis,
  suggestions,
  detectedBehavior,
  severity,
  confidence,
  bannerColor,
  executiveSummary,
  explainability
}: any) {

  const colorMap: any = {
    red: "text-red-500",
    yellow: "text-yellow-400",
    green: "text-green-400"
  };

  return (
    <div className="mt-16 space-y-16">

      {/* DETECTED BANNER */}
      <div className="text-center space-y-4">
        <h2 className={`text-3xl font-extrabold ${colorMap[bannerColor]}`}>
          Detected: {detectedBehavior}
        </h2>

        <p className="text-gray-400">
          Severity Level: <span className="font-bold">{severity}</span> | 
          Confidence: <span className="font-bold">{confidence}%</span>
        </p>
      </div>

      {/* EXECUTIVE SUMMARY */}
      <div className="bg-black border border-gray-800 rounded-2xl p-10 text-center max-w-4xl mx-auto">
        <h3 className="text-xl text-blue-400 mb-6">
          Executive Summary
        </h3>

        <p className="text-gray-300 leading-relaxed text-lg">
          {executiveSummary}
        </p>
      </div>

      {/* ROW 1 - ANALYSIS & RECOMMENDATIONS */}
      <div className="grid grid-cols-2 gap-10">

        {/* ANALYSIS */}
        <div className="bg-black border border-gray-800 rounded-2xl p-8 min-h-[320px] text-center">
          <h3 className="text-xl text-blue-400 mb-6">
            Behaviour Analysis
          </h3>

          <ul className="space-y-3 text-gray-300">
            {analysis.map((item: string, i: number) => (
              <li key={i}>• {item}</li>
            ))}
          </ul>
        </div>

        {/* RECOMMENDATIONS */}
        <div className="bg-black border border-gray-800 rounded-2xl p-8 min-h-[320px] text-center">
          <h3 className="text-xl text-blue-400 mb-6">
            Strategic Recommendations
          </h3>

          <ul className="space-y-3 text-gray-300">
            {suggestions.map((item: string, i: number) => (
              <li key={i}>• {item}</li>
            ))}
          </ul>
        </div>

      </div>

      {/* ROW 2 - ML EXPLAINABILITY CENTERED */}
      <div className="flex justify-center">
        <div className="bg-black border border-gray-800 rounded-2xl p-8 w-1/2 min-h-[320px] text-center">
          <h3 className="text-xl text-blue-400 mb-6">
            ML Explainability Breakdown
          </h3>

          <ul className="space-y-3 text-gray-300">
            {explainability.map((item: string, i: number) => (
              <li key={i}>• {item}</li>
            ))}
          </ul>
        </div>
      </div>

    </div>
  );
}