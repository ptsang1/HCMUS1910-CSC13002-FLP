from app import db

class Roles(db.Model):
    roleID = db.Column(db.INT, primary_key=True)
    roleName = db.Column(db.VARCHAR(5))

    def __repr__(self):
        return '<Role {}>'.format(self.roleName)

class Genders(db.Model):
    genderID = db.Column(db.BOOLEAN, primary_key=True)
    genderName = db.Column(db.VARCHAR(4))

    def __repr__(self):
        return '<Gender {}>'.format(self.genderName)


class Users(db.Model):
    userID = db.Column(db.VARCHAR(50), primary_key=True)
    email = db.Column(db.VARCHAR(50))
    password = db.Column(db.VARCHAR(128))
    roleID = db.Column(db.INT, db.ForeignKey('ROLES.roleID'))
    fullName = db.Column(db.NVARCHAR(50))
    genderID = db.Column(db.BOOLEAN, db.ForeignKey('GENDERS.genderID'))
    birthDate = db.Column(db.DATE)
    avatalink = db.Column(db.VARCHAR(100))

    def __repr__(self):
        return '<User {}>'.format(self.username)    

class Recipe_Posts(db.Model):
    ownerID = db.Column(db.VARCHAR(50), db.ForeignKey('USERS.userID'), primary_key=True)
    postID = db.Column(db.INT, primary_key=True)
    typeID = db.Column(db.INT)
    description = db.Column(db.TEXT)
    ingredients = db.Column(db.TEXT)
    image = db.Column(db.VARCHAR(100))

class Posts_Saved_By_Users(db.Model):
    userID = db.Column(db.VARCHAR(50), db.ForeignKey('USERS.userID'), primary_key=True)
    ownerID = db.Column(db.VARCHAR(50), db.ForeignKey('RECIPE_POSTS.ownerID'), primary_key=True)
    postID = db.Column(db.INT,  db.ForeignKey('RECIPE_POSTS.postID'), primary_key=True)

class Comments_In_Posts(db.Model):
    ownerPostID = db.Column(db.VARCHAR(50), db.ForeignKey('RECIPE_POSTS.ownerID'), primary_key=True)
    postID = db.Column(db.INT, db.ForeignKey('RECIPE_POSTS.postID'), primary_key=True)
    commentID = db.Column(db.INT, primary_key=True)
    userID = db.Column(db.VARCHAR(50), db.ForeignKey('USERS.userID'))

class Posts_Types(db.Model):
    ownerID = db.Column(db.VARCHAR(50), db.ForeignKey('RECIPE_POSTS.ownerID'), primary_key=True)
    postID = db.Column(db.INT, db.ForeignKey('RECIPE_POSTS.postID'), primary_key=True)
    i = db.Column(db.INT, primary_key=True)
    typeID = db.Column(db.INT, db.ForeignKey('FOOD_TYPES.typeID'))

class Food_Types(db.Model):
    typeID = db.Column(db.INT, primary_key=True)
    typeName = db.Column(db.NVARCHAR(20))

