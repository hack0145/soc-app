#Steps to Get-start with

1)	Steps to Obtain a Webhook URL for Slack
a.	Create a Slack App:
	Navigate to Slack API Apps and click "Create an App".
	Provide a name for your app and select the Slack workspace where the app will be installed.
b.	Add Incoming Webhooks:
	In the app's settings, go to "Incoming Webhooks" and activate it by toggling the switch.
c.	Generate a Webhook URL:
	Scroll down to the Webhook URLs for Your Workspace section and click "Add New Webhook to Workspace".
	Select the channel where the app will post messages, then click "Allow".
d.	Copy the Webhook URL:
	Once created, a unique Webhook URL will appear. Copy and securely store it for integration.

2)	Starting mariadb on linux
sudo su
sudo systemctl start mariadb

3)	Creating a user in mariadb

mysql -u root -p 
CREATE USER 'flask'@'localhost' IDENTIFIED BY 'pass';

4)	Creating a Database 
mysql -u root -p 

CREATE DATABASE user_db;  //Create the database (if not already created)

USE user_db;    //Switch to the database

Create the 'users' table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each user
    username VARCHAR(50) NOT NULL,            -- Username (non-null)
    email VARCHAR(100) NOT NULL UNIQUE,       -- Email address (unique and non-null)
    password VARCHAR(255) NOT NULL,           -- Hashed password (non-null)
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP -- Timestamp for creation
);

5)	Granting permissions to the new username 
GRANT ALL PRIVILEGES ON user_db.* TO 'flask'@'localhost'; 
FLUSH PRIVILEGES;
6)	Create a seprate virtual environment to run the flask application
cd /path/to/your/project
python -m venv venv // creating 
source venv/bin/activate // activating the environment

//Downloading the required python modules
1)	pip install flask
2)	pip install flask-mysqldb
3)	pip install bcrypt
(or)
	pip install -r requirements.txt
sudo apt update && sudo apt install -y python3-dev default-libmysqlclient-dev build-essential pkg-config



7)	Executing the Flask application
cd /path/to/your/project
source venv/bin/activate
python3 app.py
capture the logs

8) Executing the bash script
   chmod +x bash.sh(filename)
   ./bash.sh

