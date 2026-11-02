from typing import Annotated,ConfigDict,Field,StringConstraints
from pydantic import BaseModel

BorrowerStr=Annotated[str,StringConstraints(min_lenght=2, max_lengt=60)]
PurposeStr=Annotated[str,StringConstraints(min_lenght=5, max_lenght=100)]

class LoanCreate(BaseModel):
    equipment_id:int = Field(gt=1)
    borrower_name:BorrowerStr
    loan_days:int = Field(gt=1, lt=14)
    purpose:PurposeStr
    status:bool

class LoanRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id:int
    equipment_id:int
    borrower_name:BorrowerStr
    loan_days:int
    purpose:PurposeStr
    status:bool

