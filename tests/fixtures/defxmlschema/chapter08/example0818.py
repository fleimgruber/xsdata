from dataclasses import dataclass, field
from typing import Optional


@dataclass
class SpecificTime:
    """
    :ivar value:
    """
    value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            explicit_timezone="required"
        )
    )
