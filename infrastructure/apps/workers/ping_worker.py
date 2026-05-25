
import asyncio
import random
from datetime import datetime

async def monitor_device(device_ip: str):
    while True:
        latency = random.randint(5, 300)

        status = "GREEN"

        if latency > 150:
            status = "RED"
        elif latency > 50:
            status = "YELLOW"

        print({
            "device_ip": device_ip,
            "latency_ms": latency,
            "status": status,
            "timestamp": datetime.utcnow().isoformat()
        })

        await asyncio.sleep(15)

async def main():
    await asyncio.gather(
        monitor_device("10.0.0.1"),
        monitor_device("10.0.0.2"),
    )

asyncio.run(main())
