"use client";

import { motion } from "framer-motion";

export default function FeatureCards({ features }: any) {

  if (!features || Object.keys(features).length === 0) {
    return (
      <div className="text-gray-500">
        No behavioural signals available.
      </div>
    );
  }

  return (
    <div className="grid grid-cols-3 gap-6">

      {Object.entries(features).map(([key, value]: any, i) => (

        <motion.div
          key={key}
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: i * 0.05 }}
          className="bg-gradient-to-br from-white/5 to-white/10
                     backdrop-blur-lg p-6 rounded-2xl
                     border border-white/10
                     hover:scale-105 transition-all"
        >
          <div className="text-sm text-indigo-400 tracking-wide">
            {key}
          </div>

          <div className="text-3xl font-bold mt-2">
            {Number(value).toFixed(2)}
          </div>

        </motion.div>

      ))}

    </div>
  );
}