
from fastapi import APIRouter
from sqlalchemy import select

from app.db.session import SessionLocal
from app.models.models import Property, Device

router = APIRouter(prefix="/properties", tags=["properties"])

@router.get("/{property_id}/health")
async def property_health(property_id: str):
    async with SessionLocal() as db:
        devices_result = await db.execute(
            select(Device).where(Device.property_id == property_id)
        )

        devices = devices_result.scalars().all()

        total = len(devices)
        online = len([d for d in devices if d.status == "ONLINE"])

        health = "HEALTHY"

        if total > 0 and online / total < 0.5:
            health = "CRITICAL"

        return {
            "property_id": property_id,
            "health": health,
            "online_devices": online,
            "total_devices": total
        }
