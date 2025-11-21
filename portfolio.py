from flask import Flask, request

app = Flask(__name__)

home_page = """
<!DOCTYPE html>
<html>
<head>
    <title>My Portfolio</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f4f4;
            text-align: center;
            padding: 20px;
        }
        a, button {
            padding: 10px 20px;
            text-decoration: none;
            background: #000;
            color: #fff;
            border-radius: 5px;
        }
        ul {
            list-style: none;
        }
    </style>
</head>
<body>
    <h1>Hello, I'm <strong>Khalid Aziz Khan</strong></h1>
    <h3>Python Developer | Flask | HTML | CSS</h3>

    <h3>Skills:</h3>
    <ul>
        <li>Python</li>
        <li>Flask</li>
        <li>HTML & CSS</li>
        <li>React Native</li>
    </ul>

    <br>
    <a href="/contact">Contact Me</a>
</body>
</html>
"""

contact_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Contact Me</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #e3e3e3;
            text-align: center;
            padding: 20px;
        }
        input, textarea {
            width: 250px;
            padding: 10px;
            margin: 10px;
        }
        button {
            padding: 10px 20px;
            background: #000;
            color: #fff;
            border-radius: 5px;
        }
        a {
            display: inline-block;
            margin-top: 20px;
            color: #000;
        }
    </style>
</head>
<body>
    <h2>Contact Me</h2>

    <form method="POST">
        <input type="text" name="name" placeholder="Your Name" required><br>
        <input type="email" name="email" placeholder="Your Email" required><br>
        <textarea name="message" placeholder="Write message"></textarea><br>
        <button type="submit">Send</button>
    </form>

    <p>{message}</p>

    <a href="/">← Back to Home</a>
</body>
</html>
"""

@app.route("/")
def home():
    return home_page

@app.route("/contact", methods=["GET", "POST"])
def contact():
    msg = ""
    if request.method == "POST":
        name = request.form["name"]
        msg = f"Thank you {name}, your message has been submitted!"
    return contact_page.format(message=msg)

if __name__ == "__main__":
    app.run(debug=True)
