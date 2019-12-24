from app import db
from app import bcrypt
from flask_login import UserMixin
from app import login
import uuid

class Roles(db.Model):
    __tablename__ = 'roles'
    roleid = db.Column(db.INT, primary_key=True)
    rolename = db.Column(db.VARCHAR(5))

    def __repr__(self):
        return '<Role {}>'.format(self.rolename)

class Genders(db.Model):
    __tablename__ = 'genders'
    genderid = db.Column(db.BOOLEAN, primary_key=True)
    gendername = db.Column(db.VARCHAR(4))

    def __repr__(self):
        return '<Gender {}>'.format(self.gendername)


class Users(UserMixin, db.Model):
    __tablename__ = "users"
    userid = db.Column(db.VARCHAR(100), primary_key=True)
    email = db.Column(db.VARCHAR(50))
    password = db.Column(db.VARCHAR(128))
    roleid = db.Column(db.INT, db.ForeignKey('roles.roleid'))
    fullname = db.Column(db.NVARCHAR(50))
    genderid = db.Column(db.BOOLEAN, db.ForeignKey('genders.genderid'))
    birthday = db.Column(db.DATE)
    avatarlink = db.Column(db.VARCHAR(100))
    confirmed = db.Column(db.BOOLEAN)

    def __repr__(self):
        return '<User {}>'.format(self.email)

    def set_password(self, password):
        self.password = (bcrypt.generate_password_hash(password, 10)).decode("utf8")

    def set_userID(self, email):
        self.userid = (bcrypt.generate_password_hash(email, 10)).decode("utf8")

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def get_id(self):
        return self.userid

class Recipe_Posts(db.Model):
    __tablename__ = "recipe_posts"
    ownerid = db.Column(db.VARCHAR(100), db.ForeignKey('users.userid'), primary_key=True)
    postid = db.Column(db.INT, primary_key=True)
    description = db.Column(db.TEXT)
    ingredients = db.Column(db.TEXT)
    image = db.Column(db.VARCHAR(100))
    foodname = db.Column(db.NVARCHAR(50))

class Posts_Saved_By_Users(db.Model):
    __tablename__ = "posts_saved_by_users"
    userid = db.Column(db.VARCHAR(100), db.ForeignKey('users.userid'), primary_key=True)
    ownerid = db.Column(db.VARCHAR(100), db.ForeignKey('recipe_posts.ownerid'), primary_key=True)
    postid = db.Column(db.INT, db.ForeignKey('recipe_posts.postid'), primary_key=True)
    fownerid = db.relationship('Recipe_Posts', foreign_keys=[ownerid])
    fpostid = db.relationship('Recipe_Posts', foreign_keys=[postid])

class Comments_In_Posts(db.Model):
    __tablename__ = "comments_in_posts"
    ownerpostid = db.Column(db.VARCHAR(100), db.ForeignKey('recipe_posts.ownerid'), primary_key=True)
    postid = db.Column(db.INT, db.ForeignKey('recipe_posts.postid'), primary_key=True)
    commentid = db.Column(db.INT, primary_key=True)
    userid = db.Column(db.VARCHAR(100), db.ForeignKey('users.userid'))
    fownerid = db.relationship('Recipe_Posts', foreign_keys=[ownerpostid])
    fpostid = db.relationship('Recipe_Posts', foreign_keys=[postid])

class Food_Types(db.Model):
    __tablename__ = "food_types"
    typeid = db.Column(db.INT, primary_key=True)
    typename = db.Column(db.NVARCHAR(20))


class Posts_Types(db.Model):
    __tablename__ = "posts_types"
    ownerid = db.Column(db.VARCHAR(100), db.ForeignKey('recipe_posts.ownerid'), primary_key=True)
    postid = db.Column(db.INT, db.ForeignKey('recipe_posts.postid'), primary_key=True)
    i = db.Column(db.INT, primary_key=True)
    typeid = db.Column(db.INT, db.ForeignKey('food_types.typeid'))
    fownerid = db.relationship('Recipe_Posts', foreign_keys=[ownerid])
    fpostid = db.relationship('Recipe_Posts', foreign_keys=[postid])

@login.user_loader
def load_user(id):
    return Users.query.get(id)
