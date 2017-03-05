from flask import Flask
from flask import render_template, request, redirect

from config import Config
from helper import get_subdomains, add_subdomain

app = Flask(__name__)
app.config['SERVER_NAME'] = '34.207.249.209'

@app.route("/")
def index():
    #return "Hello World!"

    subdomains = get_subdomains()

    return render_template("home.html", \
            ip = Config.IP,
            subdomains = subdomains)

@app.route("/subdomain", methods=["POST"])
def subdomain():

    subdomain_name = request.form.get("subdomain_name")
    print(subdomain_name)

    add_subdomain(subdomain_name) 

    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
