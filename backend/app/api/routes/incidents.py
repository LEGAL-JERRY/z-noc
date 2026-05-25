
from fastapi import APIRouter, HTTPException
from sqlalchemy import select
from datetime import datetime

from app.db.session import SessionLocal
from app.models.models import Incident, IncidentEvent
from app.schemas.schemas import IncidentCreate, IncidentUpdate

router = APIRouter(prefix="/incidents", tags=["incidents"])

@router.post("")
async def create_incident(payload: IncidentCreate):
    async with SessionLocal() as db:
        incident = Incident(
            property_id=payload.property_id,
            device_id=payload.device_id,
            severity=payload.severity,
            title=payload.title,
            description=payload.description,
            status="OPEN",
            dedup_key=f"{payload.device_id}:{payload.title}"
        )

        db.add(incident)

        event = IncidentEvent(
            incident_id=incident.id,
            event_type="INCIDENT_CREATED",
            message=payload.description,
            created_at=datetime.utcnow()
        )

        db.add(event)

        await db.commit()

        return {"incident_id": incident.id}

@router.get("")
async def get_incidents():
    async with SessionLocal() as db:
        result = await db.execute(select(Incident))
        incidents = result.scalars().all()

        return incidents

@router.patch("/{incident_id}")
async def update_incident(incident_id: str, payload: IncidentUpdate):
    async with SessionLocal() as db:
        result = await db.execute(
            select(Incident).where(Incident.id == incident_id)
        )

        incident = result.scalar()

        if not incident:
            raise HTTPException(status_code=404, detail="Incident not found")

        if payload.status:
            incident.status = payload.status

        if payload.description:
            incident.description = payload.description

        event = IncidentEvent(
            incident_id=incident.id,
            event_type="INCIDENT_UPDATED",
            message=f"Status updated to {incident.status}",
            created_at=datetime.utcnow()
        )

        db.add(event)

        await db.commit()

        return {"status": "updated"}
