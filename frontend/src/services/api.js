import axios from 'axios';

const API_URL = 'http://127.0.0.1:5000/api';

export const getPriceTrends = () => axios.get(`${API_URL}/price-trends`);
export const getEventsCorrelation = () => axios.get(`${API_URL}/events-correlation`);
export const getModelMetrics = () => axios.get(`${API_URL}/model-metrics`);
