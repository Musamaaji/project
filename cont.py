from flask import Flask, render_template,request, redirect
from db import mydb, mycursor


app = Flask(__name__)


@app.route('/')
def index():
    mycursor.execute("SELECT * FROM student")
    x = mycursor.fetchall()
    return render_template('index.html',data = x)

    


'''

@app.route('/gotostudent')
def login():
    return redirect('/student')

'''

@app.route('/gotoadd')
def gotoadd():
    return render_template('record.html')


@app.route('/register')
def register():
    return render_template('student.html')



@app.route('/makerecord')
def makerecord():
    return render('RECORDCARD.html')



@app.route('/add', methods=['GET', 'POST'])
def add_Student():
    if request.method == 'GET':
        return redirect('/EXAM')
    if request.method == 'POST':
          # _ = request.form['name']
        _phone = request.form['phone']
        _name = request.form['name']
        _age = request.form['age']
        _DOB = request.form['DOB']
        _Student_ID= request.form['student_id']
        _maritual_status= request.form['maritual_status']
        _address = request.form['address']
        _city = request.form['city']

        sql = 'INSERT INTO student(phone,name,age,DOB, student_id,maritual_status,address,city) VALUE (%s, %s,%s, %s,%s, %s,%s, %s)'
        val = (_phone,_name,_age,_DOB,_Student_ID,_maritual_status,_address,_city)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/')




@app.route('/getresults', methods=['GET', 'POST'])
def getresults():
    if request.method == 'GET':
        return redirect('/EXAM')
    if request.method == 'POST':
          # _ = request.form['name']
        nam = request.form['name']
        mycursor.execute("SELECT * FROM card WHERE name = '" + nam + "'")
        x = mycursor.fetchall()
        return render_template('RECORDCARD.html',data = x, name = nam)








@app.route('/addcard', methods=['GET', 'POST'])
def addcard():
    if request.method == 'GET':
        return redirect('/EXAM')
    if request.method == 'POST':
          # _ = request.form['name']

        _name = request.form['name']
        _subject = request.form['record_no']
        _exam_no = request.form['subject']
        
        _score = request.form['score']   
        sql = 'INSERT INTO card(SUBJECT,EXAM_NO,NAME,SCORE) VALUE (%s, %s,%s, %s)'
        val = (_subject,_exam_no,_name,_score)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/')


@app.route('/addexam', methods=['GET', 'POST'])
def addexamm():
    if request.method == 'GET':
        return redirect('/EXAM')
    if request.method == 'POST':
          # _ = request.form['name']
        _subject = request.form['subject']
        _exam_no = request.form['exam_no']   
        sql = 'INSERT INTO EXAM(SUBJECT,EXAM_NO) VALUE (%s, %s)'
        val = (_subject,_exam_no)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/')



if __name__ == '__main__':
        app.run()




