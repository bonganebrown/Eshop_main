from my_django_app.wsgi import application

def handler(event, context):
    return serverless_wsgi.handle_request(application, event, context)
