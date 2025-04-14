import { useEffect, useState } from 'react';
import api from '../api';
import FinancePieChart from '../components//FinancePIeChart'

type Expense = {
    id: number,
    amount: number,
    category: string
}

const Dashboard = () => {
    const [expenses, setExpenses] = useState<Expense[]>([]);

    const loadExpenses = async () => {
        try{
            const res = await api.get('/api/expenses');
            setExpenses(res.data.expenses);
        } catch (err) {
            console.error(err);
        }
    };

  useEffect(() => {
    loadExpenses();
  }, []);
  
  return (
    <div className = "p-4 max-w-2xl mx-auto">
        <h2 className = "text-xl font-bold mb-4"> My Expenses</h2>
        <FinancePieChart data = {expenses} />
        <ul className = "mt-6 space-y-2">
            {expenses.map((expense) => (
                <li
                    key={expense.id}
                    className="bg-white p-3 shadow rounded-log flex justify-between"
                >
                    <span>{expense.category}</span>
                    <span>{expense.amount}</span>

                </li>
            ))}

        </ul>
    </div>
  );
}

export default Dashboard

