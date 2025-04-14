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

@app.route("/updatefortoday",methods=['GET','POST'])
def update_for_today():
    if request.method =='POST':
        content = request.form.get('content')
        if content:
            with open(Notepad_path,'at') as f:
                f.write(content + '\n')
            return "updated successfully"
        return "No content Provided"
    return render_template("index.html")
        
@app.route("/share",methods=["GET"])
def share_content():
    if os.path.exists(Notepad_path):
        with open(Notepad_path,'rt') as f:
            content = f.read()
    else:
        content = "Nothing to share"
    return render_template('shared.html',text=content) 
        
@app.route("/clearnotepadtxt", methods=['GET'])
def clean_notepad():
    with open(Notepad_path,'w') as f:
        f.write('')
    return "Notepad Cleared Successfully."
    
    
if __name__ == '__main__':
    os.makedirs('data', exist_ok=True)
    app.run()
