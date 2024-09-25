from flask import Flask, render_template, jsonify
import docker

# client = None
app = Flask(__name__)

def get_client():
    return docker.from_env()

@app.route('/')
def hello_world():
    client = get_client()
    p = client.ping()
    imgs = get_images(client)
    return render_template('index.html', ping = p, images = imgs)
    # return jsonify({"ping": p, })

# Swarm Nodes API
@app.route("/nodes")
def list_swarm_nodes():
    client = get_client()
    nlist = client.nodes.list()
    return render_template('list.html', res_list = nlist)


# Images 
def get_images(client):
    try: 
        res = client.images.list()
        return res
    except docker.errors.APIError as a:
        print("Error: ",a)
