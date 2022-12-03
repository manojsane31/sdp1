from flask import *
from pymongo import *
client = MongoClient('localhost', 27017)
db= client['fds']
fds= db.users
#create the object of Flask
app  = Flask(__name__)
#creating our routes
@app.route('/')
def Index():
    return render_template('index.html')
@app.route('/About')
def About_us():
    return render_template('About us.html')

@app.route('/onsubmit',methods=["GET","POST"])
def abc():
    username=request.form.get('uname')
    passw=request.form.get('psw')
    fds.insert_one({"username":username,"password":passw})
    x=fds.find_one({"username":username,"password":passw})
    if(x != None):
        fds.insert_one({"username":username,"password":passw})
        return render_template('Softwares.html')
    else:
          return render_template(login.html)

@app.route('/Softwares')
def Softwares():
    return render_template('Softwares.html')

@app.route("/login")
def login():
    return render_template("login.html")
@app.route('/onsubmit1',methods=["GET","POST"])
def abcd():
    username=request.form.get('username')
    passw=request.form.get('password')
    email=request.form.get('email')
    mobileno=request.form.get('mobileno')
    fds.insert_one({"username":username,"password":passw,"email":email,"mobileno":mobileno})
    return "Account Created " \
           "Username is "+username

@app.route("/Create")
def Create():
    return render_template("Create.html")


#run flask app
if __name__ == "__main__":
    app.run(debug=True)
