import { Pie } from 'react-chartjs-2';
import ChartDataLabels from 'chartjs-plugin-datalabels';
import {
    Chart as ChartJS, 
    ArcElement,
    Tooltip,
    Legend,
} from 'chart.js'; 

ChartJS.register(ArcElement, Tooltip, Legend, ChartDataLabels);

type FinancePieChartProps = {
    data: {
        category: string;
        amount: number;
    }[];
};

const FinancePieChart = ({ data }: FinancePieChartProps) => {
    const chartData = {
        labels: data.map((item) => item.category),
        datasets: [
            {
                label: 'Spending by category',
                data: data.map((item) => item.amount),
                backgroundColor: [
                    '#4ade80',
                    '#f87171', 
                    '#60a5fa', 
                    '#facc15', 
                    '#a78bfa', 
                ],
                borderWidth: 1,
            },
        ],
    };

    const options = {
        plugins: {
            datalabels: {
                formatter: (value: number, context: any) => {
                    const dataset = context.chart.data.datasets[0].data as number[];
                    const total = dataset.reduce((a,b) => a+b, 0);
                    const percentage = ((value / total) * 100).toFixed(1);
                    return `${percentage}%`;
                },
                color: '#fff',
                font: {
                    weight: 'bold' as const,
                },
            },
            legend: {
                position: 'bottom' as const,
            },
        },
    };

    return (
        <div className = "p-4 bg-white shadow rounded-lg">
            <h2 className = "text-lg font-semibold mb-2">Spending breakdown</h2>
            <Pie data = {chartData} options = {options}/>
        </div>
    )
};

export default FinancePieChart