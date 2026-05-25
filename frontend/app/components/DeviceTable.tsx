
import StatusBadge from "./StatusBadge"

export default function DeviceTable({ devices }: any) {
  return (
    <div className="panel">
      <div className="text-sm mb-4 text-gray-400">
        LIVE DEVICE MONITORING
      </div>

      <table>
        <thead>
          <tr>
            <th>DEVICE</th>
            <th>TYPE</th>
            <th>STATUS</th>
            <th>LAST HEARTBEAT</th>
            <th>UPTIME</th>
          </tr>
        </thead>

        <tbody>
          {devices.map((device: any) => (
            <tr key={device.id}>
              <td>{device.hostname}</td>
              <td>{device.device_type}</td>
              <td>
                <StatusBadge status={device.status} />
              </td>
              <td>{device.last_seen_at}</td>
              <td>{device.uptime}%</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
