from sqlalchemy  import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class WorkDB(Base):
    __tablename__ = "work"
    id:Mapped[int] = mapped_column(primary_key=True, index=True)
    equipment_id:Mapped[int] = mapped_column(
        Integer,unique= True, nullable=False
    )
    borrower_name:Mapped[int] = mapped_column(String(60), nullable= False)
    loan_days:Mapped[int] = mapped_column(Integer(14),nullable= False )
    purpose:Mapped[str] = mapped_column(String(100), nullable= False)
    status:Mapped[bool] = mapped_column(True,False, nullable=False)