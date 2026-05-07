# Employee Directory App (Team A - Python)

## Tech Stack
- Python
- Flask
- SQLite
- Selenium
- pytest

## Setup

```bash
sudo apt update
sudo apt install -y python3-venv chromium-browser chromium-driver

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt









📄 Employee Directory Application with Selenium Automation (AWS Deployment)

🧾 Project Overview
This project implements a simple Employee Directory Web Application that allows users to:
•	Add employee names 
•	View employee list 
The application is deployed on a Virtual Machine (AWS EC2) and accessed using a public IP address.
Automated testing is performed using Selenium, executed via command line (CLI).

🎯 Objectives
•	Develop a web application using Flask 
•	Deploy application on AWS EC2 
•	Access application via VM public IP (not localhost) 
•	Automate testing using Selenium 
•	Execute tests via CLI (pytest) 
•	Provide screenshots and documentation 

🧩 Application Features
✅ Functional Features
•	Add Employee (enter name + click button) 
•	Display Employee List 
✅ UI Components
•	Textbox → Enter employee name 
•	Button → Add Employee 
•	List → Display employees 
✅ API Endpoints
•	POST /employees → Add employee 
•	GET /employees → Retrieve employees 


✅ Database
•	SQLite 
•	Table: employees (id, name) 

🛠️ Technology Stack
•	Backend: Python, Flask 
•	Database: SQLite 
•	Testing: Selenium, pytest 
•	Cloud: AWS EC2 
•	Version Control: Git & GitHub 

🖥️ Project Setup (Local Environment)
Step 1: Create Project Structure
employee-directory-app/
│
├── app.py
├── requirements.txt
├── templates/index.html
└── tests/test_app.py

Step 2: Install Dependencies
pip install -r requirements.txt


Step 3: Run Application
python app.py
Access locally:
http://127.0.0.1:5000


Step 4: Verify Functionality
•	Enter employee name 
•	Click "Add Employee" 
•	Verify it appears in list 

🌐 GitHub Setup
Step 1: Initialize Repository
git init
git add .
git commit -m "Initial commit"

Step 2: Push to GitHub
git remote add origin https://github.com/<username>/employee-directory-app.git
git branch -M main
git push -u origin main

☁️ AWS EC2 Deployment
Step 1: Launch EC2 Instance
•	OS: Ubuntu 
•	Instance: t3.micro 
Step 2: Configure Security Group
Allow:
•	SSH (22) 
•	HTTP (80) 
•	Custom TCP (5000) 
 

Step 3: Connect to EC2
ssh -i key.pem ubuntu@<EC2-IP>

Step 4: Install Required Software
sudo apt update
sudo apt install python3-pip git -y
 

Step 5: Clone Repository
git clone https://github.com/<username>/employee-directory-app.git
cd employee-directory-app

Step 6: Install Dependencies
pip3 install -r requirements.txt

Step 7: Run Application
python3 app.py

Step 8: Access Application
http://<EC2-IP>:5000
 

🤖 Selenium Automation
Step 1: Install Browser & Driver
sudo apt install chromium-browser chromium-chromedriver -y

Step 2: Modify Test for Headless Mode
•	Add Chrome options (--headless) 

 

Step 3: Execute Tests
pytest

Expected Output
1 passed


📸 Screenshots
Screenshot 1:
•	Application running in browser 
•	URL: http://<EC2-IP>:5000 
Screenshot 2:
•	Terminal output of pytest 
•	Showing PASS 





🚫 Constraints Followed
•	❌ No localhost usage 
•	❌ No Nginx/IIS 
•	❌ No CI/CD 
•	❌ No authentication 
•	✅ Simple application maintained 

⚠️ Errors Faced & Solutions

❌ Error 1: Application not accessible via browser
Cause:
•	Port 5000 not open in Security Group 
Solution:
•	Added Custom TCP rule for port 5000 

❌ Error 2: Application running but not accessible
Cause:
Flask running on localhost:
app.run()
Fix:
app.run(host='0.0.0.0', port=5000)

❌ Error 3: Git push failed
Cause:
Remote already exists / authentication issue
Solution:
git remote remove origin
git remote add origin <repo-url>
git push -u origin main

❌ Error 4: Selenium test failed on EC2
Cause:
No GUI browser in server
Solution:
•	Installed Chromium 
•	Used headless mode 

❌ Error 5: ChromeDriver not found
Solution:
sudo apt install chromium-chromedriver -y

❌ Error 6: Module not found
Cause:
Dependencies not installed
Solution:
pip install -r requirements.txt

❌ Error 7: Connection refused (port issue)
Cause:
App not running / wrong port
Solution:
•	Restarted app 
•	Verified port 5000 

✅ Final Outcome
•	Application successfully deployed on AWS EC2 
•	Accessible via public IP 
•	Selenium tests executed via CLI 
•	All tests passed 
•	Screenshots captured as proof 

🎯 Conclusion
This project demonstrates:
•	Full-stack application development 
•	Cloud deployment on AWS 
•	Test automation using Selenium 
•	Real-world debugging and troubleshooting 

