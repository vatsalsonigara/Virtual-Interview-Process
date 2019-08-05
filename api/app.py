from flask import Flask,request,jsonify
from flask_mysqldb import MySQL
import yaml,json
import MySQLdb as mdb
app = Flask(__name__)

db = yaml.load(open('db.yaml'))

app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_username']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
app.config['MYSQL_CURSORCLASS']='DictCursor'

mysql = MySQL(app)


@app.route('/user', methods=['POST'])
def user():
    conn = mysql.connection
    cur =conn.cursor()
    data = request.get_json(force=True)
    try:
        cur.execute("INSERT into users(username,name,password,dob,college,email) VALUES(%s,%s,%s,%s,%s,%s)",[data['username'],data['name'],data['password'],data['dob'],data['college'],data['email']])
        mysql.connection.commit()
        cur.close()
    except Exception as e:
        cur.close()
        return json.dumps({'Error' : str(e)}) 
    return json.dumps({'Message' : 'Record inserted successfully'}) 

@app.route('/user/<username>')
def get_user_details(username):
    conn = mysql.connection
    cur =conn.cursor()
    try:
        cur.execute("Select * from users where username=%s",[username])
        data = jsonify(cur.fetchone())
        cur.close()
        return data
    except Exception as e:
        cur.close()
        return json.dumps({'Error' : str(e)})
    
@app.route('/user/<username>',methods=['DELETE'])
def delete_user(username):
    conn = mysql.connection
    cur =conn.cursor()
    try:
        cur.execute("Delete from users where username=%s",[username])
        conn.commit()
        cur.close()
        return json.dumps({'Message' : 'User deleted successfully'})
    except Exception as e:
        cur.close()
        return json.dumps({'Error' : str(e)})


if __name__=='__main__':
    app.run(debug=True)