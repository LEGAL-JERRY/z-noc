
import StatusBadge from "./StatusBadge"

export default function PropertyHealthPanel({ properties }: any) {
  return (
    <div className="panel">
      <div className="text-sm mb-4 text-gray-400">
        PROPERTY HEALTH
      </div>

      <table>
        <thead>
          <tr>
            <th>PROPERTY</th>
            <th>STATUS</th>
            <th>UPTIME</th>
            <th>ONLINE</th>
            <th>OFFLINE</th>
            <th>INCIDENTS</th>
          </tr>
        </thead>

        <tbody>
          {properties.map((p: any) => (
            <tr key={p.id}>
              <td>{p.name}</td>
              <td><StatusBadge status={p.status} /></td>
              <td>{p.uptime}%</td>
              <td>{p.online}</td>
              <td>{p.offline}</td>
              <td>{p.incidents}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
