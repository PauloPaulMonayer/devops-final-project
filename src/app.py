from flask import Flask, jsonify
from prometheus_client import Counter, Histogram, make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware

app = Flask(__name__)

# Metrics
REQUEST_COUNT = Counter('app_request_count', 'Total HTTP requests')
REQUEST_LATENCY = Histogram('app_request_latency_seconds', 'Latency of HTTP requests')

@app.before_request
def before_request():
    REQUEST_COUNT.inc()

@app.route('/')
def index():
    return jsonify(message="Hello, DevOps CI/CD!")

# נקודת בדיקה ל-CI/CD (commented out)
# @app.route('/cicd-test')
# def cicd_test():
#     return "CI/CD Pipeline Working!", 200

# Prometheus WSGI app
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
