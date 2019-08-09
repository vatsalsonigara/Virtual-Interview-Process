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

#add a user to database
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
        print(str(e))
        return json.dumps({'Error' : str(e)})
    print('Record inserted successfully') 
    return json.dumps({'Message' : 'Record inserted successfully'}) 

# get a user details from database
@app.route('/user/<username>')
def get_user_details(username):
    conn = mysql.connection
    cur =conn.cursor()
    try:
        cur.execute("Select * from users where username=%s",[username])
        json_data = jsonify(cur.fetchone())
        cur.close()
        return json_data
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


#add question to the database
@app.route('/questions',methods=['POST'])
def post_question():
    conn = mysql.connection
    cur =conn.cursor()
    data = request.get_json(force=True)
    try:
        cur.execute("INSERT into questions(company,problem_statement,test_cases,score,type,difficulty) VALUES(%s,%s,%s,%s,%s,%s)",[data['company'],data['problem_statement'],data['test_cases'],data['score'],data['type'],data['difficulty']])
        json_data = jsonify(cur.fetchone())
        conn.commit()
        cur.close()
        return json_data 
    except Exception as e:
        cur.close()
        return json.dumps({'Error' : str(e)}) 
    
#get question from database
@app.route('/questions/<int:question_id>')
def get_question(question_id):
    conn = mysql.connection
    cur =conn.cursor()
    try:
        cur.execute("Select * from questions where question_id=%s",[question_id])
        json_data = jsonify(cur.fetchone())
        cur.close()
        return json_data
    except Exception as e:
        cur.close()
        return json.dumps({'Error' : str(e)})

@app.route('/questions/<int:question_id>',methods=['DELETE'])
def delete_question(question_id):
    conn = mysql.connection
    cur =conn.cursor()
    try:
        cur.execute("Delete from questions where question_id=%s",[question_id])
        conn.commit()
        cur.close()
        return json.dumps({'Message' : 'Question deleted successfully'})
    except Exception as e:
        cur.close()
        return json.dumps({'Error' : str(e)})

#get company's question with limit and difficulty type
#limit gives the number of question
#difficulty gives the type of questions eg. medium
@app.route('/questions/<company_name>/<diff>/<int:limit>')
def get_company_questions(company_name,diff,limit):
    conn = mysql.connection
    cur =conn.cursor()
    try:
        cur.execute("Select * from questions where company=%s and difficulty=%s order by RAND() limit %s ",[company_name,diff,limit])
        json_data = jsonify(cur.fetchall())
        cur.close()
        return json_data
    except Exception as e:
        cur.close()
        return json.dumps({'Error' : str(e)})

#get all interviews of a user both completed and running
@app.route('/interviews/<username>')
def get_user_interviews(username):
    conn = mysql.connection
    cur =conn.cursor()
    try:
        cur.execute("Select * from interviews where username=%s",[username])
        json_data = jsonify(cur.fetchall())
        cur.close()
        return json_data
    except Exception as e:
        cur.close()
        return json.dumps({'Error' : str(e)})
    
@app.route('/interviews/<int:interview_id>')
def get_interview_by_id(interview_id):
    conn = mysql.connection
    cur =conn.cursor()
    try:
        cur.execute("Select * from interviews where interview_id=%s",[interview_id])
        json_data = jsonify(cur.fetchone())
        cur.close()
        return json_data
    except Exception as e:
        cur.close()
        return json.dumps({'Error' : str(e)})


#add an interview detail
@app.route('/interviews', methods=['POST'])
def add_interview():
    conn = mysql.connection
    cur =conn.cursor()
    data = request.get_json(force=True)
    try:
        cur.execute("INSERT into interviews(username,company,status,feedback,position,latest_round_id) VALUES(%s,%s,%s,%s,%s,%s)",[data['username'],data['company'],data['status'],data['feedback'],data['position'],data['latest_round_id']])
        conn.commit()
        cur.close()
        return json.dumps({'Message' : 'Record inserted successfully'}) 
    except Exception as e:
        cur.close()
        return json.dumps({'Error' : str(e)}) 

#add company round
@app.route('/rounds', methods=['POST'])
def add_company_round():
    conn = mysql.connection
    cur = conn.cursor()
    data = request.get_json(force=True)
    try:
        cur.execute("INSERT into rounds(company,position,difficulty,type,no_of_questions) VALUES(%s,%s,%s,%s,%s)",[data['company'],data['position'],data['difficulty'],data['type'],data['no_of_questions']])
        conn.commit()
        cur.close()
        return json.dumps({'Message' : 'Record inserted successfully'}) 
    except Exception as e:
        cur.close()
        return json.dumps({'Error' : str(e)}) 

#add round_details
@app.route('/round_details', methods=['POST'])
def add_round_details():
    conn = mysql.connection
    cur = conn.cursor()
    data = request.get_json(force=True)
    try:
        cur.execute("INSERT into rounds_details(username,status,start_time,duration,company,no_of_questions,total_score,type) VALUES(%s,%s,%s,%s,%s)",[data['username'],data['status'],data['start_time'],data['duration'],data['company'],data['no_of_questions'],data['total_score'],data['type']])
        conn.commit()
        cur.close()
        return json.dumps({'Message' : 'Record inserted successfully'}) 
    except Exception as e:
        cur.close()
        return json.dumps({'Error' : str(e)}) 


#get round_details
@app.route('/round_details/<int:round_id>')
def get_round_by_id(round_id):
    conn = mysql.connection
    cur =conn.cursor()
    try:
        cur.execute("Select * from round_details where round_id=%s",[round_id])
        json_data = jsonify(cur.fetchone())
        cur.close()
        return json_data
    except Exception as e:
        cur.close()
        return json.dumps({'Error' : str(e)})


#add round_questions
@app.route('/round_questions', methods=['POST'])
def add_round_questions():
    conn = mysql.connection
    cur = conn.cursor()
    data = request.get_json(force=True)
    try:
        cur.execute("INSERT into rounds_questions(round_id,question_id) VALUES(%s,%s)",[data['round_id'],data['question_id']])
        conn.commit()
        cur.close()
        return json.dumps({'Message' : 'Record inserted successfully'}) 
    except Exception as e:
        cur.close()
        return json.dumps({'Error' : str(e)}) 


#get round_questions
@app.route('/round_questions/<int:round_id>')
def get_round_questions(round_id):
    conn = mysql.connection
    cur =conn.cursor()
    try:
        cur.execute("Select * from round_questions where round_id=%s",[round_id])
        json_data = jsonify(cur.fetchall())
        cur.close()
        return json_data
    except Exception as e:
        cur.close()
        return json.dumps({'Error' : str(e)})

#add submission
@app.route('/submissions', methods=['POST'])
def add_submission():
    conn = mysql.connection
    cur = conn.cursor()
    data = request.get_json(force=True)
    try:
        cur.execute("INSERT into submissions(round_id,question_id,status,code,score,submission_time,language) VALUES(%s,%s,%s,%s,%s,%s,%s)",[data['round_id'],data['question_id'],data['status'],data['code'],data['score'],data['submission_time'],data['language']])
        conn.commit()
        cur.close()
        return json.dumps({'Message' : 'Record inserted successfully'}) 
    except Exception as e:
        cur.close()
        return json.dumps({'Error' : str(e)}) 


#get submission by submission id
@app.route('/round_questions/<int:submission_id>')
def get_submission_by_id(submission_id):
    conn = mysql.connection
    cur =conn.cursor()
    try:
        cur.execute("Select * from submissions where submissions=%s",[submission_id])
        json_data = jsonify(cur.fetchone())
        cur.close()
        return json_data
    except Exception as e:
        cur.close()
        return json.dumps({'Error' : str(e)})

    
#get submissions by round_id question_id 
@app.route('/round_questions/<int:round_id>/<int:question_id>')
def get_submissions_by_round(round_id,question_id):
    conn = mysql.connection
    cur =conn.cursor()
    try:
        cur.execute("Select * from submissions where round_id=%s and question_id=%s",[round_id,question_id])
        json_data = jsonify(cur.fetchall())
        cur.close()
        return json_data
    except Exception as e:
        cur.close()
        return json.dumps({'Error' : str(e)})
    

if __name__=='__main__':
    app.run(debug=True)