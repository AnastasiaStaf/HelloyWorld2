from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Анастасия!"

<div class="form-data">
        Name:<span id="name"></span>
        Age:<span id="age"></span>
    </div>
    <form action="/" name="form">

        <input type="text" name="name">

        <input type="text" name="age">

        <input type="submit" value="Submit">

    </form>

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    

