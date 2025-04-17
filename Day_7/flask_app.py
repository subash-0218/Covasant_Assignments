# ######################DAY 7& DAY-Weekend####################
# flask
# Question-16:
# Sharing of content 
# @app.route("/updatefortoday", methods=['GET','POST'])#http://localhost:5000/updatefortoday
# @app.route("/share", methods=['GET'])#http://localhost:5000/share
# @app.route("/clearnotepadtxt", methods=['GET'])#http://localhost:5000/clearnotepadtxt


from flask import Flask
from flask import render_template,request
import os

app = Flask(__name__)
Notepad_path = 'data/notepad.txt'

@app.route("/")
def home():
    return """
    <html>
        <head><title>Online Notepad</title></head>
        <body>
            <h1>Welcome to Online Notepad:)</h1>
        </body>
    </html>
    """

@app.route("/updatefortoday",methods=['GET','POST'])
def update_for_today():
    if request.method =='POST':
        content = request.form.get('content')
        if content:
            with open(Notepad_path,'wt') as f:
                f.write(content + '\n')
        return  """<html>
                    <head><title>Online Notepad</title></head>
                    <body>
                        <h1>Online Notepad Updated Successfully:)</h1>
                    </body>
                    <a href="/updatefortoday">Back to Online Notepad.</a><br/>
                    </html>
                """
    existing_content = ""
    if os.path.exists(Notepad_path):
        with open(Notepad_path, 'rt') as f:
            existing_content = f.read()

    return render_template("index.html", existing_content=existing_content)
    
        
@app.route("/share",methods=["GET"])
def share_content():
    if os.path.exists(Notepad_path):
        with open(Notepad_path,'rt') as f:
            content = f.read()
        print(type(content))
    else:
        content = "Nothing to share"
    return render_template('shared.html',text=content) 
    
    
@app.route("/clearnotepadtxt", methods=['GET'])
def clean_notepad():
    with open(Notepad_path,'w') as f:
        f.write('')
    return """
     <html>
        <head><title>Online Notepad</title></head>
        <body>
            <h1>Notepad Cleared Successfully:)</h1>
        </body>
        <a href="/updatefortoday">Back to Notepad</a><br/>
    </html>
    """
    
    
if __name__ == '__main__':
    os.makedirs('data', exist_ok=True)
    app.run()
