import {
    LineChart,
    Line,
    XAxis,
    YAxis,
    CartesianGrid,
    Tooltip,
    Legend,
    ResponsiveContainer
} from "recharts";

function Charts({ data }) {

    return (
        <div
            style={{
                marginTop: "50px"
            }}
        >
            <h2
                style={{
                    textAlign: "center",
                    marginBottom: "20px",
                    color: "white"
                }}
            >
                📈 Engagement Timeline
            </h2>

            <ResponsiveContainer
                width="100%"
                height={350}
            >
                <LineChart data={data}>
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="timestamp" hide />
                    <YAxis domain={[0, 100]} />
                    <Tooltip />
                    <Legend />

                    <Line
                        type="monotone"
                        dataKey="engagement"
                        stroke="#ef4444"
                        strokeWidth={3}
                        dot={false}
                    />
                </LineChart>
            </ResponsiveContainer>

            <h2
                style={{
                    textAlign: "center",
                    marginTop: "60px",
                    marginBottom: "20px",
                    color: "white"
                }}
            >
                🎯 Attention Timeline
            </h2>

            <ResponsiveContainer
                width="100%"
                height={350}
            >
                <LineChart data={data}>
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="timestamp" hide />
                    <YAxis domain={[0, 100]} />
                    <Tooltip />
                    <Legend />

                    <Line
                        type="monotone"
                        dataKey="attention"
                        stroke="#22c55e"
                        strokeWidth={3}
                        dot={false}
                    />
                </LineChart>
            </ResponsiveContainer>

        </div>
    );
}

export default Charts;