from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get('/')
def show():
    '''display madlib form on homepage'''
    return render_template('questions.html', prompts=silly_story.prompts)
#1st route will homepage
# will be home for our form (questions.html) that accepts inputs
# need to feed 'prompts' into the template - silly_story.prompts
# return prompts for form


@app.get('/results')
def results():
    '''display results '''
    text = silly_story.get_result_text(request.args)
    return render_template('results.html', story=text)
#2nd route will be to /results
#will be a GET, so need @app.get('/results')
# needed input info will be found in request.args (dictionary-like obj)
# return Story instance method with data from request.args
# will feed Story into results.html