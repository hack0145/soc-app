from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_mysqldb import MySQL
import bcrypt
import logging

app = Flask(__name__)

# MariaDB Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'flask'
app.config['MYSQL_PASSWORD'] = 'pass'
app.config['MYSQL_DB'] = 'user_db'

mysql = MySQL(app)

# Logging configuration
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s'
)

# Route for the home page (index.html)
@app.route('/')
@app.route('/index.html')
def home():
    return render_template('index.html')

# Route for the signup page (signup.html)
@app.route('/signup.html', methods=['GET'])
def signup_page():
    return render_template('./signup.html')

# Signup functionality (POST request)
@app.route('/signup', methods=['POST'])
def signup():
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        if not all([name, email, password]):
            logging.warning("Incomplete signup data provided")
            return jsonify({'message': 'All fields are required'}), 400

        # Hash the password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Insert user data into the database
        cursor = mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
            (name, email, hashed_password.decode('utf-8'))
        )
        mysql.connection.commit()
        cursor.close()

        logging.info(f"User signed up successfully: {email}")
        return jsonify({'message': 'Signup successful'}), 201

    except Exception as e:
        logging.error(f"Error during signup: {str(e)}")
        return jsonify({'message': 'Something went wrong, please try again later'}), 500

# Signin functionality (POST request)
@app.route('/signin', methods=['POST'])
def signin():
    try:
        data = request.json
        email = data.get('email')
        password = data.get('password')

        if not all([email, password]):
            logging.warning("Incomplete signin data provided")
            return jsonify({'message': 'Email and password are required'}), 400

        # Fetch user data from the database
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT username, password FROM users WHERE email = %s", [email])
        result = cursor.fetchone()
        cursor.close()

        if not result:
            logging.warning(f"Login attempt for non-existent email: {email}")
            return jsonify({'message': 'Incorrect email or password'}), 401

        username, hashed_password = result
        logging.info(f"Fetched user data for {email}: {result}")

        # Verify password
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
            logging.info(f"User logged in successfully: {email}")
            return jsonify({'message': 'Login successful', 'name': username}), 200
        else:
            logging.warning(f"Incorrect password for email: {email}")
            return jsonify({'message': 'Incorrect email or password'}), 401

    except Exception as e:
        logging.error(f"Error during signin: {str(e)}")
        return jsonify({'message': 'Something went wrong, please try again later'}), 500

@app.route('/home.html', methods=['GET'])
def home_page():
    return render_template('home.html')

# Serve static files (CSS, JS, images)
@app.route('/static/<path:filename>')
def static_files(filename):
    try:
        return send_from_directory('static', filename)
    except Exception as e:
        logging.error(f"Error serving static file: {filename} - {str(e)}")
        return "File not found", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

