from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello():
    user_data = request.form.get('text')
    if user_data:
        return count_words_in_string(user_data)
    return '''<html>
    <body>
    <form>
    <input name='text'>
    <input type='submit'>
    </form>
    </body>
    </html>'''


def count_words_in_string(s):
    return len(s.split())

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

