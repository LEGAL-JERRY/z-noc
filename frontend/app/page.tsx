
"use client"

import { useEffect, useState } from "react"

import OverviewCards from "./components/OverviewCards"
import PropertyHealthPanel from "./components/PropertyHealthPanel"
import DeviceTable from "./components/DeviceTable"
import IncidentPanel from "./components/IncidentPanel"
import TechnicianPanel from "./components/TechnicianPanel"
import EventLog from "./components/EventLog"

import { connectSocket } from "../lib/socket"

export default function DashboardPage() {
  const [events, setEvents] = useState<any[]>([])

  const [overview, setOverview] = useState({
    properties: 12,
    devices: 284,
    online: 267,
    incidents: 4
  })

  const [properties] = useState([
    {
      id: 1,
      name: "Hostel Alpha",
      status: "GREEN",
      uptime: 99.7,
      online: 48,
      offline: 2,
      incidents: 1
    },
    {
      id: 2,
      name: "Campus East",
      status: "YELLOW",
      uptime: 97.1,
      online: 62,
      offline: 7,
      incidents: 3
    }
  ])

  const [devices] = useState([
    {
      id: 1,
      hostname: "RTR-01",
      device_type: "ROUTER",
      status: "ONLINE",
      last_seen_at: "2s ago",
      uptime: 99.99
    },
    {
      id: 2,
      hostname: "AP-22",
      device_type: "AP",
      status: "OFFLINE",
      last_seen_at: "4m ago",
      uptime: 92.4
    }
  ])

  const [incidents] = useState([
    {
      id: 1,
      title: "Router unreachable",
      severity: "RED",
      status: "OPEN",
      technician: "Daniel",
      time_open: "14m"
    }
  ])

  const [technicians] = useState([
    {
      id: 1,
      name: "Daniel",
      assigned: 4,
      workload: "HIGH",
      response_time: "11m"
    }
  ])

  useEffect(() => {
    const socket = connectSocket((data) => {
      setEvents((prev) => [
        {
          timestamp: new Date().toISOString(),
          message: JSON.stringify(data)
        },
        ...prev
      ])
    })

    return () => socket.close()
  }, [])

  return (
    <main className="p-6 space-y-6">

      <div className="border-b border-[#111] pb-4">
        <div className="text-2xl font-bold">
          Z-NETWORK OPS CORE
        </div>

        <div className="text-xs text-gray-500 mt-1">
          REAL-TIME INFRASTRUCTURE OPERATIONS DASHBOARD
        </div>
      </div>

      <OverviewCards overview={overview} />

      <PropertyHealthPanel properties={properties} />

      <DeviceTable devices={devices} />

      <div className="grid grid-cols-2 gap-6">
        <IncidentPanel incidents={incidents} />
        <TechnicianPanel technicians={technicians} />
      </div>

      <EventLog events={events} />

    </main>
  )
}
