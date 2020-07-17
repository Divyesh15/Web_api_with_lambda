from repository.repository import Repository
from student_factory import StudentFactory
user_repo = Repository()


class StudentService:

    @staticmethod
    def get_student(roll_no, name):
        student_list = user_repo.get_student(roll_no, name)
        return [student.to_dict() for student in student_list]
    
    def add_student(payload):
        item=StudentFactory.student_from_payload(payload)
        user_repo.add_item(item)

    def delete_student(roll_no):
        user_repo.delete_student(roll_no)

    def edit_student(payload):
        item=StudentFactory.non_orm_student_from_payload(payload)
        user_repo.edit_item(item)
        
    
        

