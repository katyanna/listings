from flask import Flask, request, render_template
import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def get():
    items = request.args.getlist("food")
    return render_template("index.html", items = items)

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
