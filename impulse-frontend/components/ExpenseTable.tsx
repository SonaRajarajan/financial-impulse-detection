"use client";

export default function ExpenseTable({
  expenses,
  setExpenses,
  period
}: any) {

  const update = (i: number, key: string, value: any) => {
    const copy = [...expenses];
    copy[i][key] = value;
    setExpenses(copy);
  };

  const add = () => {
    setExpenses([
      ...expenses,
      {
        amount: "",
        timestamp: new Date().toISOString().slice(0, 16),
        category: "food",
        receipt: null
      }
    ]);
  };

  const remove = (i: number) => {
    setExpenses(expenses.filter((_: any, index: number) => index !== i));
  };

  const handleReceipt = (i: number, file: File) => {
    const copy = [...expenses];
    copy[i].receipt = file; // just storing locally
    setExpenses(copy);
  };

  return (
    <div className="bg-white/5 p-8 rounded-2xl border border-white/10">

      {expenses.map((e: any, i: number) => (

        <div key={i} className="grid grid-cols-5 gap-4 mb-4">

          {/* AMOUNT */}
          <input
            type="number"
            placeholder="Amount"
            value={e.amount}
            onChange={(ev) => update(i, "amount", ev.target.value)}
            className="bg-gray-800 p-3 rounded border border-gray-600
                       text-white placeholder-gray-400"
          />

          {/* DATE */}
          <input
            type="datetime-local"
            value={e.timestamp}
            onChange={(ev) => update(i, "timestamp", ev.target.value)}
            className="bg-gray-800 p-3 rounded border border-gray-600
                       text-white appearance-auto"
          />

          {/* CATEGORY */}
          <select
            value={e.category}
            onChange={(ev) => update(i, "category", ev.target.value)}
            className="bg-gray-800 p-3 rounded border border-gray-600 text-white"
          >
            <option value="food">Food</option>
            <option value="shopping">Shopping</option>
            <option value="transport">Transport</option>
            <option value="entertainment">Entertainment</option>
            <option value="bills">Bills</option>
            <option value="other">Other</option>
          </select>

          {/* UPLOAD RECEIPT (REFERENCE ONLY) */}
          <label className="bg-indigo-600 rounded text-center cursor-pointer
                            hover:bg-indigo-700 transition-all flex items-center justify-center">
            Upload Receipt
            <input
              type="file"
              className="hidden"
              onChange={(ev: any) => {
                if (ev.target.files[0]) {
                  handleReceipt(i, ev.target.files[0]);
                }
              }}
            />
          </label>

          {/* REMOVE BUTTON */}
          <button
            onClick={() => remove(i)}
            className="bg-red-600 rounded hover:bg-red-700 transition-all"
          >
            Remove
          </button>

        </div>
      ))}

      <button
        onClick={add}
        className="bg-purple-600 px-6 py-2 rounded-xl hover:scale-105 transition-all"
      >
        + Add Expense
      </button>

    </div>
  );
}