from flask import Flask, jsonify
from flask_cors import CORS

app = Flask('server')
CORS(app)

# Example of an endpoint that returns test data
@app.route('/getinfo')
def getinfo():
    info = {"name":'breaking bias', "score":"awesome"}
    return jsonify(info)

if __name__ == '__main__':
    app.run()

# This is to test that CI/CD pipeline is working. Delete later.
def cicd_test():
    print("CI/CD is cooking")
    return None
