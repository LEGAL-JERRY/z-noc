
type Props = {
  overview: any
}

export default function OverviewCards({ overview }: Props) {
  return (
    <div className="grid grid-cols-4 gap-4">
      <div className="panel">
        <div className="text-xs text-gray-500">PROPERTIES</div>
        <div className="text-3xl mt-2">{overview.properties}</div>
      </div>

      <div className="panel">
        <div className="text-xs text-gray-500">DEVICES</div>
        <div className="text-3xl mt-2">{overview.devices}</div>
      </div>

      <div className="panel">
        <div className="text-xs text-gray-500">ONLINE</div>
        <div className="text-3xl mt-2 status-green">
          {overview.online}
        </div>
      </div>

      <div className="panel">
        <div className="text-xs text-gray-500">ACTIVE INCIDENTS</div>
        <div className="text-3xl mt-2 status-red">
          {overview.incidents}
        </div>
      </div>
    </div>
  )
}
