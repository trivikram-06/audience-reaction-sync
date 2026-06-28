function AudienceTable({ data }) {

    return (

        <table
            style={{
                width: "100%",
                borderCollapse: "collapse",
                marginTop: "40px"
            }}
        >

            <thead>

                <tr
                    style={{
                        background: "#1f2937"
                    }}
                >
                    <th>ID</th>
                    <th>Eyes</th>
                    <th>Blinks</th>
                    <th>Attention</th>
                    <th>Engagement</th>
                </tr>

            </thead>

            <tbody>

                {data.map(person => (

                    <tr
                        key={person.person_id}
                        style={{
                            textAlign: "center",
                            borderBottom: "1px solid gray"
                        }}
                    >

                        <td>{person.person_id}</td>

                        <td>{person.eye_status}</td>

                        <td>{person.blink_count}</td>

                        <td>{person.attention}%</td>

                        <td>{person.engagement}%</td>

                    </tr>

                ))}

            </tbody>

        </table>

    );

}

export default AudienceTable;