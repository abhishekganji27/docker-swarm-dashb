from flask import Flask, render_template, jsonify, flash
import docker
import docker.errors as de

# client = None
app = Flask(__name__)

def get_client():
    return docker.from_env()

@app.route('/')
def hello_world():
    client = get_client()
    p = client.ping()
    return render_template('index.html', ping = p)

# Swarm Services
@app.route("/services")
def list_swarm_services():
    try:
        client = get_client()
        slist = client.services.list()
        return render_template("services/list.html", res_list = slist)
    except de.APIError as a:
        flash("Error!")
        return render_template("404.html", error=e)

# Swarm Nodes API
@app.route("/nodes")
def list_swarm_nodes():
    try:
        client = get_client()
        nlist = client.nodes.list()
        return render_template("list.html", res_list = nlist)

    except de.APIError as a:
        flash("Error!")
        return render_template("404.html", error=e)