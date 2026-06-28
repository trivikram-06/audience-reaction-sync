import axios from "axios";

const api = axios.create({
    baseURL: "http://127.0.0.1:8000",
});

export const getAnalytics = async () => {
    const response = await api.get("/analytics");
    return response.data;
};

export const getLatest = async () => {
    const response = await axios.get("http://127.0.0.1:8000/latest");
    return response.data;
};

export const getHistory = async () => {
    const response = await axios.get("http://127.0.0.1:8000/history");
    return response.data;
};

export default api;