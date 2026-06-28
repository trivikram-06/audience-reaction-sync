function KPI({ title, value, color }) {
    return (
        <div
            style={{
                background: "#1f2937",
                borderRadius: "16px",
                padding: "25px",
                width: "250px",
                boxShadow: "0 0 15px rgba(0,0,0,0.25)",
                textAlign: "center",
                border: `2px solid ${color}`
            }}
        >
            <h3
                style={{
                    color: "#ffffff",
                    marginBottom: "15px"
                }}
            >
                {title}
            </h3>

            <h1
                style={{
                    color: color,
                    fontSize: "40px"
                }}
            >
                {value}
            </h1>
        </div>
    );
}

export default KPI;