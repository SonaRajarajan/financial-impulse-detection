export default function NudgesPanel({ nudges, profile }: any) {
  return (
    <div className="bg-white/5 p-6 rounded-2xl border border-white/10">

      <h3 className="text-xl text-indigo-400 mb-4">
        {profile}
      </h3>

      {nudges.map((n: string, i: number) => (
        <p key={i} className="mb-2 text-gray-300">
          • {n}
        </p>
      ))}

    </div>
  );
}