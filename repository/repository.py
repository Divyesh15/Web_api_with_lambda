from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DB_URL
from repository.model import StudentModel
from student_factory import StudentFactory

engine = create_engine(DB_URL, echo=False)
Session = sessionmaker(bind=engine)


class Repository:

    def __init__(self):
        self.session = Session()

    def add_item(self, item):
        
        try:
            self.session.add(item)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e

        self.session.commit()

    def add_all_items(self, items):
        try:
            self.session.add_all(items)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e

    def get_student(self, roll_no, name):
        student_query = self.session.query(StudentModel)
        if roll_no is not None:
            student_query = student_query.filter(StudentModel.roll_no == roll_no)
        if name is not None:
            student_query = student_query.filter(StudentModel.name == name)
        student_db = student_query.all()
        students = StudentFactory.student_list_from_db(student_db)
        self.session.commit()
        return students

    def delete_student(self,roll_no):
        student_query=self.session.query(StudentModel)
        if roll_no is not None:
            student_query=student_query.filter(StudentModel.roll_no==roll_no).delete()
            self.session.commit()

    def edit_item(self,item):
        if item.roll_no is None:
            return
        student_query=self.session.query(StudentModel).filter(StudentModel.roll_no==item.roll_no).one()
        if item.name is not None:
            student_query.name=item.name
        
        self.session.commit()
        

        
            

