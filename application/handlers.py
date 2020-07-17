from application.service import StudentService
import json


def get_student(event, context):
    query_parameters = event.get("queryStringParameters")
    roll_no = None
    name = None
    if query_parameters is not None:
        roll_no = query_parameters.get("roll_no")
        name = query_parameters("name")

    response = StudentService.get_student(roll_no, name)
    return {"statusCode": 200, "body": json.dumps(response) }

def add_student(event,context):
    d1=json.loads(event['body'])
    StudentService.add_student(d1)
    return {"statusCode": 200, "body": json.dumps("") }

def delete_student(event,context):
    roll_no=event['pathParameters']['roll_no']
    StudentService.delete_student(roll_no)
    return {"statusCode": 200, "body": json.dumps("") }

def edit_student(event,context):
    d1=json.loads(event['body'])
    StudentService.edit_student(d1)
    return {"statusCode": 200, "body": json.dumps("") }
