from flask import Flask,request,jsonify
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
    
if __name__=='__main__':
    app.run(debug=True,port=8000)