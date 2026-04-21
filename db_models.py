from sqlmodel import SQLModel, Field

class StudentORM(SQLModel, table = True):
    __tablename__ = "students"

    id: str = Field(primary_key=True)
    name: str
    age: int
    major: str
    score: int

      