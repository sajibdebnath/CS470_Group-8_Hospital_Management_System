# CS470_Group-8_Hospital_Management_System
Hospital Management System
Group Members:
1.	Name: Sajib Debnath, WIU ID: 923-60-2769, Email: s-debnath@wiu.edu
2.	Name: Md Zakir Hossain Zamil, WIU ID: 923-50-3436, Email: mzh-zamil@wiu.edu 
3.	Name: Clerique Ward, WIU ID: 923-663-392, Email: cts-ward@wiu.edu 

====================================
PROJECT OVERVIEW
====================================
This is a Hospital Management System (HMS) web application built using Flask and Oracle SQL. 
It is designed to manage patients, doctors, departments, appointments, rooms, and billing 
information efficiently. This system provides a user-friendly interface and performs full 
CRUD operations with Oracle database integration.

====================================
REQUIREMENTS
====================================
Before running the project, ensure the following dependencies and environment are set up:

Python Version: 3.9+
Oracle Database: 19c or compatible
Oracle DSN: (e.g., oracle2.wiu.edu:1521/orclpdb1)

Python Packages (from requirements.txt):
----------------------------------------
Flask==2.2
Flask-SQLAlchemy==3.0.3
Jinja2==3.1.2
MarkupSafe==2.1.2
SQLAlchemy==2.0.3
Werkzeug==2.2.3
click==8.1.3
colorama==0.4.6
cx-Oracle==8.3.0
greenlet==2.0.2
importlib-metadata==6.0.0
itsdangerous==2.1.2
pip==23.0
setuptools==67.3.1
typing-extensions==4.5.0
zipp==3.13.0

Install all dependencies with:
----------------------------------------
pip install -r requirements.txt

====================================
SETUP INSTRUCTIONS
====================================

1. Configure Oracle Database
----------------------------
- Execute all SQL scripts in 'SQL G8.sql' to create tables.
- Ensure your Oracle DB credentials and DSN are correctly set in hosp_class.py:
  Example:
  app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle+oracledb://username:password@host:port/?service_name=orclpdb1'

2. Run the Flask Application
----------------------------
- Make sure your Oracle database server is running.
- Open terminal and navigate to the project folder.
- Run the following command:
  python app.py

3. Access the Application
----------------------------
- Open your browser and visit:
  http://127.0.0.1:5000/

====================================
MODULES OVERVIEW
====================================
- /patient: Add/Edit/Delete/Search patient records
- /doctor: Manage doctor information
- /department: Department creation and updates
- /appointment: Schedule patient appointments
- /room: Assign and update room details
- /billing: Manage patient billing and payment status

====================================
NOTE
====================================
- Ensure Oracle listener is active and reachable.
- Verify connection configuration if encountering connection errors.
- All templates use Bootstrap and are pre-designed for usability.
- Images like 'Home page.png' and 'ERD G8.png' are useful for documentation.

Thank you for using this Hospital Management System!
