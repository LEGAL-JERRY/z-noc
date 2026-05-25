
import asyncio
from datetime import datetime, timedelta
from sqlalchemy import select

from app.db.session import SessionLocal
from app.models.models import Device
from app.services.incidents import create_incident_if_needed

STALE_AFTER_SECONDS = 90

async def monitor_devices():
    while True:
        async with SessionLocal() as db:
            result = await db.execute(select(Device))
            devices = result.scalars().all()

            for device in devices:
                if datetime.utcnow() - device.last_seen_at > timedelta(seconds=STALE_AFTER_SECONDS):
                    device.status = "OFFLINE"

                    await create_incident_if_needed(db, device)

            await db.commit()

        await asyncio.sleep(30)

asyncio.run(monitor_devices())
