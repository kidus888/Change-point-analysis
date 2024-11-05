from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# Load Brent oil price data (assuming pre-processed data is stored as a CSV)
brent_data = pd.read_csv("data/brent_oil_analysis.csv", parse_dates=["Date"])

@app.route('/api/price-trends', methods=['GET'])
def get_price_trends():
    data = brent_data[['Date', 'Brent_Price']].to_dict(orient='records')
    return jsonify(data)

@app.route('/api/events-correlation', methods=['GET'])
def get_events_correlation():
    # Serve correlation data with events, assuming it's available in a CSV
    events_data = pd.read_csv("data/events_correlation.csv")
    data = events_data.to_dict(orient='records')
    return jsonify(data)

@app.route('/api/model-metrics', methods=['GET'])
def get_model_metrics():
    # Model performance metrics like RMSE, MAE
    metrics = {"RMSE": 2.54, "MAE": 1.76}
    return jsonify(metrics)

if __name__ == '__main__':
    app.run(debug=True)
