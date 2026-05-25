
from pydantic import BaseModel
from typing import Optional

class HeartbeatRequest(BaseModel):
    device_id: str
    latency_ms: int
    packet_loss: int

class IncidentCreate(BaseModel):
    property_id: str
    device_id: str
    severity: str
    title: str
    description: str

class IncidentUpdate(BaseModel):
    status: Optional[str] = None
    description: Optional[str] = None

class AssignmentCreate(BaseModel):
    incident_id: str
    technician_id: str
    notes: Optional[str] = ""
