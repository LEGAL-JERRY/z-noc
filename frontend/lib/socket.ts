export function connectSocket(onMessage: (data: any) => void) {
  const API_URL = process.env.NEXT_PUBLIC_API_URL || ""

  const WS_URL = API_URL
    .replace("https://", "wss://")
    .replace("http://", "ws://")

  const socket = new WebSocket(`${WS_URL}/ws`)

  socket.onopen = () => {
    console.log("WebSocket connected")
  }

  socket.onmessage = (event) => {
    try {
      const data = JSON.parse(event.data)
      onMessage(data)
    } catch (err) {
      console.error("WebSocket parse error", err)
    }
  }

  socket.onerror = (err) => {
    console.error("WebSocket error", err)
  }

  socket.onclose = () => {
    console.log("WebSocket disconnected")
  }

  return socket
}
