from flask import Flask,abort,render_template,request,redirect,url_for
from werkzeug import secure_filename
import os
app = Flask(__name__)

@app.route('/upload/',methods = ['GET','POST'])
def upload_file():
    if request.method =='POST':
        global file
        file = request.files['file[]']
        if file:
            global filename
            filename = secure_filename(file.filename)
            return hello()
    return render_template('uploading.html')

@app.route('/hello')
def hello():
    return render_template('hello.html',name=filename)#,text=f)

@app.route('/des/')

def des():
    f = file.open()
    read = f.read()
    return render_template('des.html',descript=read)

if __name__ == '__main__':
    app.run(debug = True)