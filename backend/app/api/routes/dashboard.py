
from fastapi import APIRouter
from sqlalchemy import select, func

from app.db.session import SessionLocal
from app.models.models import Device, Incident, Property

router = APIRouter(prefix="/dashboard", tags=["dashboard"])

@router.get("/overview")
async def overview():
    async with SessionLocal() as db:
        devices = await db.scalar(select(func.count(Device.id)))
        incidents = await db.scalar(select(func.count(Incident.id)))
        properties = await db.scalar(select(func.count(Property.id)))

        return {
            "devices": devices,
            "incidents": incidents,
            "properties": properties
        }
