from flask import Flask,jsonify,request,json
from datetime import datetime
import logging
app = Flask(__name__)

ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Configure the logging
logging.basicConfig(filename="app.log",level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Create a logger
logger = logging.getLogger(__name__)


@app.route("/")
def hello():
    logger.info(f"{ts}, index endpoint was reached")
    return "Hello World!"

@app.route("/test")
def testing():
    logger.info(f"{ts}, test endpoint was reached")
    return "Hi, this is a test!"

@app.route("/status")
def status():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )
    
    logger.info(f"{ts}, health status endpoint was reached")
    return response

@app.route("/metrics")
def metrics():
    data = {"status":"success",
            "code":0,
            "data":{"UserCount":140,"UserCountActive":25}
            }

    logger.info(f"{ts}, metrics endpoint was reached")
    return jsonify(data) 



if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
