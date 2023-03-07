from flask import Flask, request, render_template
from StringCounter import StringCounter

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        input_string = request.form['input_string']
        string_counter = StringCounter()
        count = string_counter.count(input_string)
        return render_template('result.html', count=count)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()