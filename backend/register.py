from flask import Flask,request,jsonify,session
import requests
import json
app = Flask(__name__)

@app.route('/user/register',methods=["POST"])
def register():
    print("test")
    json_data = {
        'username':request.form.get('username'),
        'password':request.form.get('password'),
        'dob':request.form.get('dob'),
        'college':request.form.get('college'),
        'name':request.form.get('name'),
        'email':request.form.get('email')

        }
    json_data=json.dumps(json_data)    
    
    response=requests.post('http://localhost:5000/user',data=json_data)
    print(response)
    return "Success"
    

@app.route('/user/login',methods=["POST"])
def login():
    print("test")
    json_data = {
        'username':request.form.get('username'),
        'password':request.form.get('password')
        }    
    print(json_data)
    response=requests.get('http://localhost:5000/user/'+json_data['username'])
    user_details=json.loads(response.content.decode())
    print(response)
    print(user_details)
    if user_details is None:
        return "User does not exist!!"
    elif user_details['password']!=json_data['password']:
        return "Incorrect Password!!"
    return "Successful login"
if __name__=='__main__':
    app.run(debug=True,port=8000)