from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
import sqlite3

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type==float,
                        required=True,
                        help="This field cannot be blank!")

    @jwt_required
    def get(self,name):
        connection = sqlite3.connect('database/database.db')
        cursor = connection.cursor()

        query = "SELECT * FROM recipe where foodname=?"

        result = cursor.execute(query,(name,))
        row =  result.fetchall()
        connection.close()

        if row:
            return {'message':'successful',
                    'items':row}
        else:
            return {'message':'fail'},404


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