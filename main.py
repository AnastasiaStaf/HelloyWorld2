from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Анастасия!"

 >>> st='01000E69B7D101000E69B7D101000E69B7D1'
>>> nl=''
>>> i=0
>>> while st.count(nl+st[i])>=3:
...  nl+=st[i]
...  i+=1
... 
>>> nl
'01000E69B7D1'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    

