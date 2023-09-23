from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

# Configure the database connection
db_host = 'puckplanner.cqckq1f04hpm.us-east-2.rds.amazonaws.com'
db_user = 'puckplanner'
db_password = 'Ollie4240!'
db_name = 'puckplanner'

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def login():
    return render_template('Login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/venues')
def venues():
    return render_template('venues.html')

@app.route('/teams')
def teams():
    return render_template('teams.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/schedule')
def schedule():
    return render_template('schedule.html')

@app.route('/preferences')
def preferences():
    return render_template('preferences.html')

@app.route('/gamespecs')
def gamespecs():
    return render_template('gamespecs.html')

@app.route('/forgotpassword')
def forgotpassword():
    return render_template('forgotpassword.html')

@app.route('/divisions')
def divisions():
    return render_template('divisions.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/register')
def register():
    return render_template('register.html')

# Establish a connection to the database
def get_db_connection():
    return pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name)

# Define an endpoint to handle GET requests
@app.route('/get_data', methods=['GET'])
def get_data():
    # Connect to the database
    connection = get_db_connection()

    # Define your SQL query to retrieve data
    query = "SELECT * FROM your_table"

    # Execute the query
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()

    # Close the database connection
    connection.close()

    # Convert the result to a JSON response
    response = jsonify(result)
    return response

if __name__ == '__main__':
    app.run(debug=True)
