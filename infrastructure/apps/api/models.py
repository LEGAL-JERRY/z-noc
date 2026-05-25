
from sqlalchemy import String, ForeignKey, DateTime
from sqlalchemy.orm import mapped_column, Mapped
from database import Base
from datetime import datetime
import uuid

class Property(Base):
    __tablename__ = "properties"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    name: Mapped[str]
    location: Mapped[str]

class Device(Base):
    __tablename__ = "devices"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    hostname: Mapped[str]
    management_ip: Mapped[str]
    status: Mapped[str] = mapped_column(default="UNKNOWN")

    property_id: Mapped[str] = mapped_column(
        ForeignKey("properties.id")
    )

    last_seen_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

class Incident(Base):
    __tablename__ = "incidents"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    severity: Mapped[str]
    status: Mapped[str] = mapped_column(default="OPEN")
    title: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )
