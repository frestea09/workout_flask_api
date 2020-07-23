from flask import Flask,jsonify
from flask_restful import Resource,Api
from flask_sqlalchemy import SQLAlchemy
import mysql.connector

myDb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='pegawai14'
)
myCursor = myDb.cursor()
app = Flask(__name__)
api = Api(app)

class Buku(Resource):
    def get(self):
        sql = '''
           SELECT * 
           FROM bagian
        '''
        myCursor.execute(sql)
        hasilSelect = myCursor.fetchall()
        resp = jsonify(hasilSelect)
        return resp

api.add_resource(Buku,'/')

if __name__ == '__main__':
    app.run(debug=True)