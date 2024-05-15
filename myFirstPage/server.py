from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        path = request.form.get('path')  
        href = "../static/css/styles.css"  
        if os.path.exists(path):
            files = os.listdir(path)
            output = "<br>".join(files)
            return render_template('index.html', output=output, href=href)
        else:
            return render_template('index.html', output=['Uknown element'], href=href)
    else:
        href = "../static/css/styles.css"
        link = request.headers.get('Link')
        return render_template('index.html', href=link if link else href)

if __name__ == "__main__":
    app.run(debug=True)
