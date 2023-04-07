from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/poshyk', methods=['POST'])
def calculate():
    num1 = int(request.form['n1'])
    num2 = int(request.form['n2'])
    num3 = int(request.form['n3'])
    operation = request.form['operation']

    if operation == 'min':
        result = min(num1, num2, num3)
    elif operation == 'max':
        result = max(num1, num2, num3)
    elif operation == 'avg':
        result = (num1 + num2 + num3) / 3

    return render_template('home.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)