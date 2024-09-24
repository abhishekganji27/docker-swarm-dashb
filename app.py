from flask import Flask, render_template, jsonify
import docker
# client = None
app = Flask(__name__)

@app.route('/')
def hello_world():
    client = docker.from_env()
    p = client.ping()
    imgs = get_images(client)
    return render_template('index.html', ping = p, images = imgs)
    # return jsonify({"ping": p, })

def get_images(client):
    try:
        res = client.images.list()
        return res
    except docker.errors.APIError as a:
        print("Error: ",a)

"""
Make an engine join a docker swarm that has already been created.
Params: 
1. remote_addrs(list[str]): IP address of one or more managers. 
2. join_token(str): Secret token to join the swarm.
3. advertise_addr(str): IP of node running this web application.

@app.route("/join-swarm")
def join_swarm(ra, jt, aa):
    try:
        response = client.swarm.join(remote_addrs=[str(ra)], join_token=jt, advertise_addr=aa)
        return response
    except docker.errors.APIError as e:
        print("An errored occured", e)
"""
if __name__ == "__main__":
    app.run(debug=True)