from flask_app import app
from vercel_adapter import vercel_wsgi

def handler(event, context):
    return vercel_wsgi(app, event, context)
