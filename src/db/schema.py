from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing import Optional


class Base(DeclarativeBase):
    pass


class NetworkEntry(Base):
    __tablename__ = "network"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    prefix: Mapped[str]
    path: Mapped[str]
    destination: Mapped[str]
    ingress: Mapped[str]
    egress: Mapped[str]
    shortest_path: Mapped[bool]
    traffic_size: Mapped[int]
    additional_features: Mapped[Optional[str]]

    def __repr__(self) -> str:
        return f"""Network Entry:
			prefix: {self.prefix}
			path: {self.path}
			destination: {self.destination}
			traffic_size: {self.traffic_size}
			ingress: {self.ingress}
			egress: {self.egress}
			shortest_path: {self.shortest_path}
			additional_features: {self.additional_features}
		"""
