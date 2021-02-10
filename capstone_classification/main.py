from flask import Flask, render_template, request

index = 0

app = Flask(__name__, static_url_path='/static/')
@app.route('/')
def home():
    global index
    index += 1
    print(index)
    return render_template('home.html')

app.run(debug=True)