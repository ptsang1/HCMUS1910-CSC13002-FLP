import sqlite3
import uuid
from datetime import datetime
from flask.views import MethodView
from flask_restful import  reqparse

class User:
    def __init__(self,_id,_username,_password):
        self.id=_id
        self.username=_username
        self.password=_password
    @classmethod
    def find_by_username(cls,username):
        connection = sqlite3.connect("database/database.db")
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE email=?"
        result= cursor.execute(query,(username,))
        row=result.fetchone()
        if row:
            user = cls(*row)
        else:
            user=None
        connection.close()
        return user

    @classmethod
    def find_by_id(cls, id):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE userid=?"
        result = cursor.execute(query, (id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None
        connection.close()
        return user

class UserRegister(MethodView):

    parser = reqparse.RequestParser()
    parser.add_argument('email',type=str,required=True,help="This field cannot be blank")
    parser.add_argument('password',type=str,required=True,help="This field cannot be blank")
    parser.add_argument('full_name',type=str,required=True,help="This field cannot be blank")
    def post(self):
        data = UserRegister.parser.parse_args()
        connection = sqlite3.connect('database/database.db')
        cursor = connection.cursor()
        query = "INSERT INTO users VALUES (?,?,?,?,?,?)"
        time = datetime.now().strftime("%B %d, %Y %I:%M%p")
        cursor.execute(query,(str(uuid.uuid1()),str(data['email']),str(data['password']),str(data['full_name']),str(time),str("no_link")))
        connection.commit()
        connection.close()
        return{'message':'Create user successfully.'},201