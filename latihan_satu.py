from flask import Flask,request,jsonify,make_response
from flask_restful import Resource,Api,reqparse
import mysql.connector

myDb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'pegawai14'
)

myCursor = myDb.cursor()
app  = Flask(__name__)
api = Api(app)

class TodoList(Resource):
    def get(self):
        sql = '''
            SELECT * 
            FROM bagian
        '''
        myCursor.execute(sql)
        hasilQuery = myCursor.fetchall()
        resp = jsonify(hasilQuery)
        return resp
    def post(self):
        _json = request.json
        _kode_Bag = _json['Kode_Bagi']
        _nama_Bagi = _json['Nama_Bagi']
        _gaji_Pokok = _json['Gaji_Pokok']
        sql = '''
            INSERT 
            INTO bagian(Kode_Bagi,Nama_Bagi,Gaji_Pokok)
            VALUES(%s,%s,%s)
        '''
        inputParameter = (_kode_Bag,_nama_Bagi,_gaji_Pokok,)
        myCursor.execute(sql,inputParameter)
        myDb.commit()
        respone = jsonify('Employee added successfully!')
        respone.status_code = 200
        return respone
    def delete(self):
        _json = request.json
        _kode_Bag = _json['Kode_Bagi']
        sql = '''
            DELETE FROM bagian
            WHERE Kode_Bagi = %s 
        '''
        inputParameter = (_kode_Bag,)
        myCursor.execute(sql,inputParameter)
        myDb.commit()
        respone = jsonify('Employee added successfully!')
        respone.status_code = 200
        return respone
class Todo(Resource):
    def get(self,inputId):
        sql = '''
                   SELECT * 
                   FROM bagian
                   WHERE Kode_Bagi = %s
               '''
        inputParameter = (inputId,)
        myCursor.execute(sql,inputParameter)
        hasilQuery = myCursor.fetchall()
        resp = jsonify(hasilQuery)
        return resp
    def delete(self,inputId):
        sql = '''
            DELETE FROM bagian
            WHERE Kode_Bagi = %s 
        '''
        inputParameter = (inputId,)
        myCursor.execute(sql,inputParameter)
        myDb.commit()
        return '', 204
api.add_resource(TodoList,'/bagian')
api.add_resource(Todo,'/bagian/<inputId>')

if __name__ == '__main__':
    app.run(debug=True)