from flask import Flask, render_template

app = Flask(__name__)

# Data for dynamic rendering
gym_highlights = [
    "State-of-the-art equipment",
    "Professional trainers",
    "Flexible timings",
    "Customized fitness plans",
]
team_members = ["John Doe", "Jane Smith", "Emily Clark", "Mark Lee"]
facilities = ["Cardio Zone", "Weight Training", "Yoga Studio", "Swimming Pool"]
membership_plans = [
    {"name": "Basic Plan", "price": "$20/month"},
    {"name": "Standard Plan", "price": "$40/month"},
    {"name": "Premium Plan", "price": "$60/month"},
]

@app.route("/")
def home():
    return render_template("home.html", highlights=gym_highlights)

@app.route("/about")
def about():
    return render_template("about.html", team=team_members, facilities=facilities)

@app.route("/membership")
def membership():
    return render_template("membership.html", plans=membership_plans)

if __name__ == "__main__":
    app.run(debug=True)

