from flask import Flask, render_template, jsonify, flash
import docker
import docker.errors as de

# client = None
app = Flask(__name__)

def get_client():
    return docker.from_env()

@app.route('/')
def home():
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
    except de.APIError as e:
        flash("Error!")
        return render_template("404.html", error=e)

@app.route("/services/<string:id>/inspect")
def inspect_swarm_service(id):
    try:
        client = get_client()
        service = client.services.get(id)
        return render_template("services/inspect.html", service=service)
    
    except de.NotFound as nf:
        return render_template("404.html", error = nf)
    except de.APIError as ae:
        return render_template("404.html", error = ae)
    except de.InvalidVersion as iv:
        return render_template("404.html", error = iv)

# Swarm Nodes API
@app.route("/nodes")
def list_swarm_nodes():
    try:
        client = get_client()
        nlist = client.nodes.list()
        return render_template("nodes/list.html", res_list = nlist)

    except de.APIError as e:
        flash("Error!")
        return render_template("404.html", error=e)