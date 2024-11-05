import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';

function PriceTrendChart({ data }) {
    return (
        <LineChart width={600} height={300} data={data}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="Date" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Line type="monotone" dataKey="Brent_Price" stroke="#8884d8" activeDot={{ r: 8 }} />
        </LineChart>
    );
}

export default PriceTrendChart;
