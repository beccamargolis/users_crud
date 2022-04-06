from sqlite3 import connect
from flask_app.config.mysqlconnection import connectToMySQL

class User:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users = []

    @classmethod
    def get_all(cls): # always include "cls" for a classmethod
        query = "SELECT * FROM users;"
        results = connectToMySQL('basic_user_schema').query_db(query)
        users = []
        for d in results:
            users.append(cls(d))

        return users

    @classmethod
    def get_one(cls,id): # here we'll also pass in the id because we need that information to pull the data for one line item
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL('basic_user_schema').query_db(query, {'id':id})
        return cls(result[0])


    @classmethod
    def save(cls, data): # "data" is being passed in here, this represents the information the user is inputting
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        result = connectToMySQL('basic_user_schema').query_db(query, data)
        return result

    @classmethod
    def update(cls, data, id): # here we need both the id of the line item we're updating as well as the updated "data" that is being provided
        query = f"UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id = {id};" # we need an f string here to pass in the id
        return connectToMySQL('basic_user_schema').query_db(query,data)

    @classmethod # here we just need the id of the line item we are going to delete
    def destroy(cls, id):
        query = f"DELETE FROM users WHERE id = {id};"
        return connectToMySQL('basic_user_schema').query_db(query)