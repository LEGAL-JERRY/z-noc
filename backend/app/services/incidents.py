
from sqlalchemy import select
from app.models.models import Incident
from datetime import datetime

async def create_incident_if_needed(db, device):
    dedup_key = f"{device.id}:OFFLINE"

    existing = await db.execute(
        select(Incident).where(
            Incident.dedup_key == dedup_key,
            Incident.status.in_(["OPEN", "INVESTIGATING"])
        )
    )

    if existing.scalar():
        return None

    severity = "LOW"

    if device.device_type == "ROUTER":
        severity = "HIGH"

    incident = Incident(
        property_id=device.property_id,
        device_id=device.id,
        severity=severity,
        title=f"Device Offline: {device.hostname}",
        description="Monitoring engine detected offline device.",
        status="OPEN",
        dedup_key=dedup_key,
        created_at=datetime.utcnow()
    )

    db.add(incident)
    await db.commit()

    return incident
