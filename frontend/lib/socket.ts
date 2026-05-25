
export const connectSocket = (onMessage: (data: any) => void) => {
  const socket = new WebSocket("ws://localhost:8000/ws")

  socket.onmessage = (event) => {
    const data = JSON.parse(event.data)
    onMessage(data)
  }

  return socket
}
