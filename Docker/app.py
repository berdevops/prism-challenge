from flask import Flask
from redis import Redis
import os
app = Flask(__name__)
redis = Redis(host=os.environ.get('REDIS_HOST', 'redis'), port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    return 'Hello! This API increments the counter for each inbound HTTP GET request. GET resquests received = %s times.\n' % redis.get('hits')

@app.route('/health')
def heathCheck():
	return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)