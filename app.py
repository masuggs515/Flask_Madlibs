from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)



@app.route("/")
def questions():
    prompt = story.prompts

    return render_template("app.html", prompt=prompt)

@app.route("/story")
def make_story():

    story_text = story.generate(request.args)

    return render_template("story.html", text = story_text)