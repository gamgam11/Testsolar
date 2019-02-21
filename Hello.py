from flask import Flask,render_template,request,redirect,url_for
import pymysql

app = Flask(__name__)

conn=pymysql.connect('localhost','root','','studentdb')

@app.route("/")
def showData():
       with conn:
              cur=conn.cursor()
              cur.execute("select * from student")
              rows=cur.fetchall()
              return render_template('index.html',datas=rows)

@app.route("/student")
def showForm():
       return render_template('addstudent.html')

@app.route("/delete/<string:id_data>",methods=['GET'])
def delete(id_data):
       with conn:
              cur=conn.cursor()
              cur.execute("delete from student where id=%s",(id_data))
              conn.commit()
       return redirect(url_for('showData'))

@app.route("/insert",methods=['POST'])
def insert():
       if request.method=="POST":
              fname=request.form['fname']
              lname=request.form['lname']
              phone=request.form['phone']
              with conn.cursor() as cursor:
                     sql="Insert into `student` (`fname`,`lname`,`phone`) values(%s,%s,%s)"
                     cursor.execute(sql,(fname,lname,phone))
                     conn.commit()
              return redirect(url_for('showData'))

@app.route("/update",methods=['POST'])
def update():
       if request.method=="POST":
              id_update=request.form['id']
              fname=request.form['fname']
              lname=request.form['lname']
              phone=request.form['phone']
              with conn.cursor() as cursor:
                     sql="update student set fname=%s,lname=%s,phone=%s where id=%s"
                     cursor.execute(sql,(fname,lname,phone,id_update))
                     conn.commit()
              return redirect(url_for('showData'))

if __name__ == "__main__":
       app.run(debug=True)
