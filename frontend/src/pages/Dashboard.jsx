import { useEffect, useState } from "react";
import KPI from "../components/KPI";
import AudienceTable from "../components/AudienceTable";
import Charts from "../components/Charts";
import { getAnalytics, getLatest, getHistory } from "../services/api";

function Dashboard() {
    const [analytics, setAnalytics] = useState(null);
    const [latest, setLatest] = useState([]);
    const [history, setHistory] = useState([]);

    async function loadData() {
        try {
            const analyticsData = await getAnalytics();
            const latestData = await getLatest();
            const historyData = await getHistory();

            setAnalytics(analyticsData);
            setLatest(latestData);
            setHistory(historyData);
        } catch (err) {
            console.error(err);
        }
    }

    useEffect(() => {
        loadData();

        // Auto refresh every 2 seconds
        const interval = setInterval(() => {
            loadData();
        }, 2000);

        return () => clearInterval(interval);
    }, []);

    if (!analytics) {
        return (
            <div
                style={{
                    background: "#111827",
                    color: "white",
                    minHeight: "100vh",
                    display: "flex",
                    justifyContent: "center",
                    alignItems: "center",
                    fontSize: "30px"
                }}
            >
                Loading...
            </div>
        );
    }

    return (
        <div
            style={{
                padding: "40px",
                background: "#111827",
                minHeight: "100vh",
                color: "white"
            }}
        >
            <h1
                style={{
                    textAlign: "center",
                    marginBottom: "40px"
                }}
            >
                🎭 Audience Reaction Dashboard
            </h1>

            {/* KPI Cards */}

            <div
                style={{
                    display: "flex",
                    justifyContent: "center",
                    gap: "30px",
                    flexWrap: "wrap"
                }}
            >
                <KPI
                    title="👥 People"
                    value={analytics.people}
                    color="#22c55e"
                />

                <KPI
                    title="🎯 Attention"
                    value={`${analytics.avg_attention}%`}
                    color="#facc15"
                />

                <KPI
                    title="🔥 Engagement"
                    value={`${analytics.avg_engagement}%`}
                    color="#ef4444"
                />
            </div>

            {/* Audience Table */}

            <h2
                style={{
                    marginTop: "60px",
                    marginBottom: "20px",
                    textAlign: "center"
                }}
            >
                👥 Live Audience Status
            </h2>

            <AudienceTable data={latest} />
            <Charts data={history} />
        </div>
    );
}

export default Dashboard;