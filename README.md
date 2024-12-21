Gym Management System
Project Description
The Gym Management System is a web application built using Flask. It dynamically displays gym highlights, team members, facilities, and membership plans. The project demonstrates the use of Flask templates and routing to create an interactive and user-friendly website.

Purpose
This project aims to:

Provide a template for creating dynamic websites using Flask.
Showcase gym services, facilities, and membership plans in an organized and appealing way.
Demonstrate the integration of backend Python logic with frontend templates.
Features
Home Page: Displays gym highlights.
About Us Page: Lists team members and gym facilities.
Membership Page: Shows available membership plans with pricing.
How to Run the Project Locally
1. Prerequisites
Ensure you have the following installed:

latest python version
Flask (pip install flask)
2. Steps to Run
Clone the repository:

git clone https://github.com/suhaimakhan07/my-first-repo.git
cd gym-management-system
Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

pip install flask
Run the application:


python app.py
Open your browser and go to:


http://127.0.0.1:5000
Project Structure
gym-management-system/
├── app.py                 # Main application file
├── templates/             # HTML templates
│   ├── base.html          # Base layout
│   ├── home.html          # Home page
│   ├── about.html         # About Us page
│   └── membership.html    # Membership plans page
├── static/
│   └── style.css          # Styling for the application
└── README.md              # Project documentation
License
This project is licensed under the MIT License.
