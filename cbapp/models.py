from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(db.Model):
  """
  Chorus battle user class
  """
  __tablename__ = 'users'
  user_id = db.Column(db.Integer, primary_key = True)
  firstname = db.Column(db.String(100))
  lastname = db.Column(db.String(100))
  email = db.Column(db.String(120), unique=True)
  password_hash = db.Column(db.String(54))

  def __init__(self, firstname, lastname, email, password):
    self.firstname = firstname.title()
    self.lastname = lastname.title()
    self.email = email.lower()
    self.set_password(password)

  def set_password(self, password):
  """
  Allows password to be changed.
  
  Args:
    password (str): new password to replace current password
  """
    self.password_hash = generate_password_hash(password)

  def check_password(self, password):
  """
  Checks if password matches hashed password

  Args:
    password (str): password to be checked

  Returns:
    bool: True if password matches hashed password and false if not
  """  
    return check_password_hash(self.password_hash,password)