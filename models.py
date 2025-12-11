from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import json

db = SQLAlchemy()


class Country(db.Model):
    __tablename__ = "countries"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)

    recipes = db.relationship("Recipe", backref="country", lazy=True)
    quiz_questions = db.relationship("QuizQuestion", backref="country", lazy=True)


class Recipe(db.Model):
    __tablename__ = "recipes"

    id = db.Column(db.Integer, primary_key=True)
    country_id = db.Column(db.Integer, db.ForeignKey("countries.id"), nullable=False)

    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(200))
    _ingredients = db.Column("ingredients", db.Text)
    _instructions = db.Column("instructions", db.Text)

    @property
    def ingredients(self):
        """Get ingredients as a Python list"""
        if self._ingredients:
            return json.loads(self._ingredients)
        return []

    @ingredients.setter
    def ingredients(self, value):
        """Set ingredients from a Python list or JSON string"""
        if isinstance(value, str):
            self._ingredients = value
        else:
            self._ingredients = json.dumps(value)

    @property
    def instructions(self):
        """Get instructions as a Python list"""
        if self._instructions:
            return json.loads(self._instructions)
        return []

    @instructions.setter
    def instructions(self, value):
        """Set instructions from a Python list or JSON string"""
        if isinstance(value, str):
            self._instructions = value
        else:
            self._instructions = json.dumps(value)


class QuizQuestion(db.Model):
    __tablename__ = "quiz_questions"

    id = db.Column(db.Integer, primary_key=True)
    country_id = db.Column(db.Integer, db.ForeignKey("countries.id"), nullable=False)

    question = db.Column(db.Text, nullable=False)
    type = db.Column(db.String(20))
    _options = db.Column("options", db.Text)
    _answer = db.Column("answer", db.String(200))

    @property
    def options(self):
        """Get options as a Python list"""
        if self._options:
            return json.loads(self._options)
        return []

    @options.setter
    def options(self, value):
        """Set options from a Python list or JSON string"""
        if isinstance(value, str):
            self._options = value
        else:
            self._options = json.dumps(value)

    @property
    def answer(self):
        """Get answer (can be string or boolean)"""
        if self._answer:
            return json.loads(self._answer)
        return None

    @answer.setter
    def answer(self, value):
        """Set answer from any value or JSON string"""
        if isinstance(value, str) and (value.startswith('[') or value.startswith('{') or value == 'true' or value == 'false' or value == 'null'):
            self._answer = value
        else:
            self._answer = json.dumps(value)


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)