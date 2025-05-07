# Question-30
# Create chatbot using flask and langchain
    # Display has two inputs 
    # Query - takes Query
    # Result - returns result 
# MUst Have history


from flask import Flask, render_template, request, redirect, url_for, session
from dotenv import load_dotenv
import os
import requests

app = Flask(__name__)
app.secret_key = "your-secret-key"
MISTRAL_API_KEY = os.environ.get("MISTRAL_API_KEY")

def call_mistral_api(messages):
    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mistral-tiny",
        "messages": messages
    }
    response = requests.post("https://api.mistral.ai/v1/chat/completions", json=data, headers=headers)
    return response.json()["choices"][0]["message"]["content"]

@app.route("/")
def home():
    return redirect(url_for("new_chat"))

@app.route("/new")
def new_chat():
    if "chats" not in session:
        session["chats"] = []

    chat_id = len(session["chats"])
    session["chats"].append({
        "title": f"Chat {chat_id + 1}",
        "history": []
    })
    session.modified = True
    return redirect(url_for("chat", chat_id=chat_id))

@app.route("/chat/<int:chat_id>", methods=["GET", "POST"])
def chat(chat_id):
    chats = session.get("chats", [])

    if not (0 <= chat_id < len(chats)):
        return redirect(url_for("home"))

    if request.method == "POST":
        user_message = request.form["message"]
        chat = chats[chat_id]

        if len(chat["history"]) == 0:
            chat["title"] = user_message[:30]

        chat["history"].append({"role": "user", "content": user_message})
        response = call_mistral_api(chat["history"])
        chat["history"].append({"role": "assistant", "content": response})
        session.modified = True
        
        return redirect(url_for("chat", chat_id=chat_id))

    return render_template("index.html",chat_id=chat_id,history=chats[chat_id]["history"],chats=chats,theme=session.get("theme", "light"))

@app.route("/theme/<mode>")
def switch_theme(mode):
    if mode in ["dark", "light"]:
        session["theme"] = mode
    return redirect(request.referrer or url_for("home"))

@app.route("/clear")
def clear_all():
    session.clear()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run()
