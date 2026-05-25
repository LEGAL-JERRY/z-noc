
export default function EventLog({ events }: any) {
  return (
    <div className="panel h-[400px] overflow-y-scroll">
      <div className="text-sm mb-4 text-gray-400">
        SYSTEM EVENT LOG
      </div>

      <div className="space-y-2 text-xs">
        {events.map((event: any, idx: number) => (
          <div
            key={idx}
            className="border-b border-[#111] pb-2"
          >
            <div>{event.timestamp}</div>
            <div>{event.message}</div>
          </div>
        ))}
      </div>
    </div>
  )
}
