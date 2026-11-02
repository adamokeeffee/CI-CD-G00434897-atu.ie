from fastapi import Depends, FastAPI, HTTPException, Response, status

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from sqlalchemy import Select

from app.database import engine,get_db
from app.models import Base, LoanDB
from app.schemas import LoanCreate, LoanRead

Base.matadata.create_all(bind=engine)

app = FastAPI(title="Example template")

@app.get("/health")
def health():
    return{"status": "ok"}

@app.post("/api/loans",response_model = LoanRead,
          status_code=status.HTTP_201_CREATED,)

def add_loan(new_loan:LoanCreate,db:Session= Depends(get_db)):
    db_loans = LoanDB (**new_loan.model_dump())
    db.add(db_loans)

    try:
        db.commit()
        db.refresh(db_loans)
    except IntegrityError: db.rollback()

    return db_loans

@app.get("/api/loans/{loans_id}", response_model = LoanRead)

def get_loans(Loan_id: int,db:Session=Depends(get_db)):
    db_loans = db.get(LoanDB,Loan_id)
    if db_loans is None:
        raise HTTPException(status_code=status. HTTP_404_NOT_FOUND,detail="Loan not found",)
    return db_loans

