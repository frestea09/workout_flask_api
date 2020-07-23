from flask import Flask,render_template
from flask_sqlalchemy import  SQLAlchemy
app = Flask(__name__,template_folder='templates')
# @app.route('/')
# @app.route('/home')
# def hello():
#     return 'hello world'

# input String
# @app.route('/home/<string:name>')
# def hello(name):
#     return 'Hello, '+name

# input Integer
# @app.route('/home/<int:id>')
# def hello(id):
#     return  'Umur : ' + str(id)

# input get post
# @app.route('/onlyget',methods=['GET'])
# def getMetode():
#     return 'you can read this'

postAll = [
    {
        'nim' : '10112299',
        'name' : 'ilman teguh prasetya'
    }
]
postAllIf = [
    {
    }
]

# @app.route('/')
# def index():
#     return render_template('index.html')
#
# @app.route('/post')
# def post():
#     return render_template('post.html',posts = postAll)
# @app.route('/post-kondisi')
# def postKondisi():
#     return render_template('post-kondisi.html',posts = postAllIf)
if __name__ == '__main__':
    app.run(debug=True)