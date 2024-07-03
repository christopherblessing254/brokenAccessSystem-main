
import email
from flask import *
import pymysql

# create a Flask app
app = Flask(__name__)

app.secret_key = 'gdodiuwe7ysf457ew7hdflio'

@app.route('/')
def home():
    # here we check wether we have anyone  logged in 
    if 'userrole' in session:
        return render_template('index.html')
    else:
        return redirect('/signin')

@app.route('/signin', methods=['POST','GET'])
def signin():
    if request.method == 'POST':
        # get the form data
        email = request.form['email']
        password = request.form['password']
        # check if the user exists
        connection= pymysql.connect(host='localhost', user='root', passwd='',database='cybertestsystem')   

        cursor = connection.cursor()

        sql ='select * from users where email =%s and password = %s'

        cursor.execute(sql, (email, password))

        if cursor.rowcount == 0:
            return render_template('signin.html', error = 'Invalid email or password')
        else:
            # get the user role
            user = cursor.fetchone()
            # capture the  role
            role = user[3]
            # store the role in a session
            session['userrole'] = role

            return redirect('/')
    else:
        return render_template('signin.html')
    
@app.route('/signout')
def signout():
    return redirect('/signin')


app.run(debug=True)