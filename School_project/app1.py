from flask import Flask,render_template,request
import mysql.connector
user_dict={'admin':'1234','user':'5678'}
conn = mysql.connector.connect(host='localhost',user='root',password='',database='school')
mycursor=conn.cursor()
#create a flask application
app = Flask(__name__)

#Define the route 

@app.route('/')
def hello():
    return render_template('first.html')
@app.route('/employee')
def employee():
    return render_template('student.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/home',methods=['POST'])
def home():
    uname=request.form['username']
    pwd=request.form['password']

    if uname not in user_dict:
        return render_template('login.html',msg='Invalid User')
    elif user_dict[uname] != pwd:
        return render_template('login.html',msg='Invalid Password')
    else:
        return render_template('home.html')
@app.route('/view')
def view():
    query="SELECT * FROM students"
    mycursor.execute(query)
    data=mycursor.fetchall()
    return render_template('view.html',sqldata=data)

@app.route('/search')
def searchpage():
    return render_template('search.html')
@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')
@app.route('/searchresult',methods=['POST'])
def search():
    rollno= request.form['roll_no']
    query="SELECT * FROM students WHERE rollno="+rollno
    mycursor.execute(query)
    data=mycursor.fetchall()
    return render_template('view.html',sqldata=data)
    
@app.route('/add')
def add():
    return render_template('student.html')

@app.route('/read',methods=['POST'])
def read():
    rollno = request.form['rollno']
    name = request.form['name']
    grade= request.form['grade']
    phone_number= request.form['phone_number']
    query = "INSERT INTO students(rollno,name,grade,phone_number) VALUES (%s,%s,%s,%s)"
    data = (rollno,name,grade,phone_number)
    mycursor.execute(query,data)
    conn.commit()
    return render_template('student.html',msgdata='Added Successfully')
@app.route('/contactus')
def contactus():
    return render_template('contactus.html')

#Run the flask app
if __name__=='__main__':
    app.run(port=5001,debug = True)