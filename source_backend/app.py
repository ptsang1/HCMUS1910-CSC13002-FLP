from flask import Flask,render_template,redirect,url_for,request
from flask_restful import Resource,Api,reqparse
from flask_jwt import JWT,jwt_required

from security import authenicate, indentity
from user import UserRegister

import os
APP_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_PATH = os.path.join(APP_PATH, './source_frontend/templates/')
STATIC_DIR = os.path.join(APP_PATH, './source_frontend/static/')

app = Flask(__name__,template_folder=TEMPLATE_PATH,static_folder=STATIC_DIR)
print(app.template_folder)
app.secret_key = "Ма́ша и Медве́дь"
api = Api(app)

jwt = JWT(app,authenicate,indentity)

items = []

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type==float,
                        required=True,
                        help="This field cannot be blank!")

    @jwt_required
    def get(self,name):
        item = next(filter(lambda x: x['name']== name,items),None)
        return {'item':item},200 if item else 404
    def post(self,name):
        if next(filter(lambda x: x['name']== name,items),None):
            return {'message':"An item with name '{}' already exists." .format(name)},400
        data= Item.parser.parse_args()
        item = {'name':name,'price':data['price']}
        items.append(item)
        return item,201
    def delete(self,name):
        global items
        items = list(filter(lambda x:x['name']!=name,items))
        return {'message':"Item with name {} have been " .format(name)}
    def put(self,name):
        data = Item.parser.parse_args()

        item = next(filter(lambda x: x['name']==name,items),None)
        if item is None:
            item = {'name' : name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item

class ItemList(Resource):
    def get(self):
        return{'item':items}
class CheckOn(Resource):
    def get(self):
        return{'message':app.root_path},404


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    return render_template('login.html', error=error)

api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister,'/register')
api.add_resource(CheckOn,'/helloworld')

app.run(port=5000,debug=True)
    
