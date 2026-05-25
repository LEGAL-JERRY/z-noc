
from fastapi import APIRouter
from app.db.session import SessionLocal
from app.models.models import Assignment
from app.schemas.schemas import AssignmentCreate

router = APIRouter(prefix="/assignments", tags=["assignments"])

@router.post("")
async def create_assignment(payload: AssignmentCreate):
    async with SessionLocal() as db:
        assignment = Assignment(
            incident_id=payload.incident_id,
            technician_id=payload.technician_id,
            notes=payload.notes
        )

        db.add(assignment)

        await db.commit()

        return {"assignment_id": assignment.id}
