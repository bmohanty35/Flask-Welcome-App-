
#S-1: import the Flask
from flask import Flask, request

#S-2: Initialize the Flask object
app = Flask(__name__)

#S-3: Create a route 
@app.route("/upper")
def upper_name():
    name = request.args.get("name")
    return f"""
    <h1 style="color:blue;">HELLO {name.upper()} 👋</h1>
    """

@app.route("/greet")
def greet_user():
    import datetime
    name = request.args.get("name")
    hour = datetime.datetime.now().hour

    if hour < 12:
        greet = "Good Morning ☀️"
    elif hour < 18:
        greet = "Good Afternoon 🌤️"
    else:
        greet = "Good Evening 🌙"

    return f"""
    <h1>{greet}, {name.upper()}!</h1>
    <p>Hope you're having a great day 🚀</p>
    """

#S-4: Run the app
if __name__ == "__main__":
    app.run(debug=True)