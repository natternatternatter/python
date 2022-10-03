from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE, EMAIL_REGEX


class User:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def register(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW())"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def validate_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        result = connectToMySQL(DATABASE).query_db(query, data)

        if len(result) > 0:
            current_user = cls(result[0])
            return current_user
        else:
            return None

    @staticmethod
    def validate_registration(data):

        is_valid = True

        if len(data['first_name']) < 2:
            flash("Your first name is too short")
            is_valid = False

        if len(data['last_name']) < 2:
            flash("Your last name is too short")
            is_valid = False

        if not EMAIL_REGEX.match(data['email']):
            flash("That is not a proper email address")
            is_valid = False

        if data['password'] != data['confirm_password']:
            flash("Your passwords do not match")
            is_valid = False

        return is_valid
