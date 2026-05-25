
export default function TechnicianPanel({ technicians }: any) {
  return (
    <div className="panel">
      <div className="text-sm mb-4 text-gray-400">
        TECHNICIANS
      </div>

      <table>
        <thead>
          <tr>
            <th>NAME</th>
            <th>ASSIGNED</th>
            <th>WORKLOAD</th>
            <th>AVG RESPONSE</th>
          </tr>
        </thead>

        <tbody>
          {technicians.map((tech: any) => (
            <tr key={tech.id}>
              <td>{tech.name}</td>
              <td>{tech.assigned}</td>
              <td>{tech.workload}</td>
              <td>{tech.response_time}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
