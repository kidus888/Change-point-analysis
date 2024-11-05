// frontend/src/components/MetricsDisplay.js
import React from 'react';

function MetricsDisplay({ metrics }) {
    return (
        <div>
            <h2>Model Performance Metrics</h2>
            <p>RMSE: {metrics.RMSE}</p>
            <p>MAE: {metrics.MAE}</p>
        </div>
    );
}

export default MetricsDisplay;
