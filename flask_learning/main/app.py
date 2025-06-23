from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates\\')


class User:
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def greet(self):
        return f"Hello {self.name}, you entered: {self.data}"


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/about")
def about():
    return "<p>This site!</p>"


@app.route("/user", methods=["GET"])
def user():
    username = request.args.get('username')
    data = request.args.get('data')

    if username and data:
        user_obj = User(username, data)
        return user_obj.greet()

    return "<p>Missing username or data!</p>"


if __name__ == "__main__":
    app.run(debug=True)
