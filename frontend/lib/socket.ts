export function connectSocket(onMessage: (data: any) => void) {
  const API_URL = process.env.NEXT_PUBLIC_API_URL || "";
  
  // Create a flag to track if the polling loop should stop
  let isStopped = false;
  let intervalId: NodeJS.Timeout | null = null;

  console.log("ZNOC Mode: Fetching dashboard overview via HTTP Polling.");

  // Function that simulates the WebSocket onmessage stream using fetch
  const pollBackendData = async () => {
    if (isStopped) return;

    try {
      // FIXED: Points straight to your real Python route (/dashboard/overview)
      const response = await fetch(`${API_URL}/dashboard/overview`);
      
      if (!response.ok) {
        throw new Error(`HTTP Error Status: ${response.status}`);
      }

      const data = await response.json();
      
      // Pass the data cleanly back to your dashboard UI, exactly like socket.onmessage did
      onMessage(data);

    } catch (err) {
      console.error("Polling error or backend is sleeping:", err);
    }
  };

  // Run the first fetch immediately when the dashboard loads
  pollBackendData();

  // Poll every 5 seconds (5000ms)
  intervalId = setInterval(pollBackendData, 5000);

  // Return a mock object so any calling code trying to run socket.close() won't crash
  return {
    close: () => {
      console.log("Polling stopped");
      isStopped = true;
      if (intervalId) clearInterval(intervalId);
    },
    // Adding standard readyState property so your frontend stays happy
    readyState: 1 // 1 means OPEN in WebSocket terms
  };
}
