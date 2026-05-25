
import StatusBadge from "./StatusBadge"

export default function IncidentPanel({ incidents }: any) {
  return (
    <div className="panel">
      <div className="text-sm mb-4 text-gray-400">
        INCIDENT MANAGEMENT
      </div>

      <table>
        <thead>
          <tr>
            <th>TITLE</th>
            <th>SEVERITY</th>
            <th>STATUS</th>
            <th>TECHNICIAN</th>
            <th>TIME OPEN</th>
          </tr>
        </thead>

        <tbody>
          {incidents.map((incident: any) => (
            <tr key={incident.id}>
              <td>{incident.title}</td>
              <td>
                <StatusBadge status={incident.severity} />
              </td>
              <td>{incident.status}</td>
              <td>{incident.technician}</td>
              <td>{incident.time_open}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
