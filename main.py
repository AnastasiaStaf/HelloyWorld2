from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Анастасия!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    
    words = "слово1 слово2 слово1 слово3 слово2 Вася слово1"
word_list = words.split()

from collections import defaultdict
word_count_dict = defaultdict(int)

for word in word_list:
    print(word, word_count_dict[word])
    word_count_dict[word] += 1
