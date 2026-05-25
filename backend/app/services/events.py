
from sqlalchemy import insert
from app.models.models import SystemEvent
from datetime import datetime

async def log_event(db, event_type, actor, entity_type, entity_id, payload):
    stmt = insert(SystemEvent).values(
        event_type=event_type,
        actor=actor,
        entity_type=entity_type,
        entity_id=entity_id,
        payload=str(payload),
        created_at=datetime.utcnow()
    )
    await db.execute(stmt)
    await db.commit()
