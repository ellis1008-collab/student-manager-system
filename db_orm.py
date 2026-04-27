import os

from sqlmodel import SQLModel, Session, create_engine, select

from db_models import StudentORM

##默认数据库文件路径：
DEFAULT_DB_PATH = "data/students.db"

##动态获取数据库文件路径（与测试对齐）：
def get_db_path():
    return os.getenv("STUDENT_DB_PATH",DEFAULT_DB_PATH)

##获取连接数据库文件所需的URL网址格式的字符串：
def get_database_url():
    db_path = get_db_path()
    return f"sqlite:///{db_path}"


def get_engine():
    return create_engine(get_database_url(),echo=False)


def create_db_and_tables():
    
    db_path = get_db_path()
    db_dir = os.path.dirname(db_path)

    if db_dir:
        os.makedirs(db_dir,exist_ok=True)
        
    engine = get_engine()

    SQLModel.metadata.create_all(engine)   ##SQL语句是由SQLAC根据matadata中的SQLModel模型信息生成的，engine传给数据库引擎来执行

##获取表中的全部记录（全部学生信息）：
def get_all_students_orm():
    engine = get_engine()
    with Session(engine) as session:
        statement = select(StudentORM)
        results = session.exec(statement)
        return list(results)
    
##根据学号查询对应学生信息：
def get_student_by_id_orm(student_id):
    engine = get_engine()
    ##用select对象加上session来读取：
    with Session(engine) as session:
        statement = select(StudentORM).where(StudentORM.id == student_id)
        result = session.exec(statement).first()
        return result
    
##添加学生：
def add_student_orm(student_data):
    engine = get_engine()
    with Session(engine) as session:
        student = StudentORM(
            id=student_data["id"],
            name=student_data["name"],
            age=student_data["age"],
            major=student_data["major"],
            score=student_data["score"],
        )
        session.add(student)
        session.commit()
        session.refresh(student)
        return student
    
##修改学生：
def update_student_by_id_orm(student_id,student_data):
    engine = get_engine()
    ##通过select对象加上session来读取：
    with Session(engine) as session:
        statement = select(StudentORM).where(StudentORM.id == student_id)
        student = session.exec(statement).first()

        if student is None:
            return None
        ##进行修改：
        student.name = student_data["name"]
        student.age = student_data["age"]
        student.major = student_data["major"]
        student.score = student_data["score"]

        session.commit()
        session.refresh(student)
        return student
    
##删除学生：
def delete_student_by_id_orm(student_id):
    engine = get_engine()
    with Session(engine) as session:
        statement = select(StudentORM).where(StudentORM.id == student_id)
        student = session.exec(statement).first()

        if student is None:
            return None
        session.delete(student)
        session.commit()
        return student


if __name__ == "__main__":
    
##创建数据库和学生表：
    create_db_and_tables()

##先确认要删除的学生的信息：
    target_id = "006"
    print(f"Before delete {target_id}:")
    print(get_student_by_id_orm(target_id))

##从返回结果上确认：
    deleted_student = delete_student_by_id_orm(target_id)
    print(f"Deleted {target_id} by ORM:")
    print(deleted_student)

##从数据库中再次确认：
    print(f"After delete {target_id}:")
    print(get_student_by_id_orm(target_id))

