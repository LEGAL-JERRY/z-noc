
from fastapi import APIRouter, HTTPException
from sqlalchemy import select
from datetime import datetime

from app.db.session import SessionLocal
from app.models.models import Device, DeviceStatusLog
from app.schemas.schemas import HeartbeatRequest

router = APIRouter(prefix="/devices", tags=["devices"])

@router.post("/heartbeat")
async def heartbeat(payload: HeartbeatRequest):
    async with SessionLocal() as db:
        result = await db.execute(
            select(Device).where(Device.id == payload.device_id)
        )

        device = result.scalar()

        if not device:
            raise HTTPException(status_code=404, detail="Device not found")

        device.last_seen_at = datetime.utcnow()
        device.status = "ONLINE"
        device.uptime_seconds += 15

        log = DeviceStatusLog(
            device_id=device.id,
            status="ONLINE",
            latency_ms=payload.latency_ms,
            packet_loss=payload.packet_loss
        )

        db.add(log)

        await db.commit()

        return {
            "status": "heartbeat_received",
            "device_id": device.id
        }

@router.get("/status")
async def device_status():
    async with SessionLocal() as db:
        result = await db.execute(select(Device))
        devices = result.scalars().all()

        return [
            {
                "id": d.id,
                "hostname": d.hostname,
                "status": d.status,
                "last_seen_at": d.last_seen_at
            }
            for d in devices
        ]
