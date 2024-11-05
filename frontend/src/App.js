// frontend/src/App.js
import React, { useState, useEffect } from 'react';
import { getPriceTrends, getEventsCorrelation, getModelMetrics } from './services/api';
import PriceTrendChart from './charts/PriceTrendChart';
import MetricsDisplay from './components/MetricsDisplay';

function App() {
    const [priceTrends, setPriceTrends] = useState([]);
    const [eventsCorrelation, setEventsCorrelation] = useState([]);
    const [metrics, setMetrics] = useState({});

    useEffect(() => {
        // Fetch data on component mount
        getPriceTrends().then(response => setPriceTrends(response.data));
        getEventsCorrelation().then(response => setEventsCorrelation(response.data));
        getModelMetrics().then(response => setMetrics(response.data));
    }, []);

    return (
        <div className="App">
            <h1>Brent Oil Price Analysis Dashboard</h1>
            <MetricsDisplay metrics={metrics} />
            <PriceTrendChart data={priceTrends} />
        </div>
    );
}

export default App;
