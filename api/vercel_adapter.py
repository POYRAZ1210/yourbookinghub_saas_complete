import io
from urllib.parse import urlencode

def vercel_wsgi(app, event, context):
    method = event.get("httpMethod", "GET")
    path = event.get("path", "/")
    headers = event.get("headers", {})
    query = event.get("queryStringParameters", {}) or {}
    body = event.get("body", "")
    
    environ = {
        "REQUEST_METHOD": method,
        "PATH_INFO": path,
        "QUERY_STRING": urlencode(query),
        "SERVER_NAME": "localhost",
        "SERVER_PORT": "80",
        "wsgi.version": (1, 0),
        "wsgi.url_scheme": "http",
        "wsgi.input": io.BytesIO(body.encode() if isinstance(body, str) else body),
        "wsgi.errors": io.StringIO(),
        "wsgi.multithread": False,
        "wsgi.multiprocess": False,
        "wsgi.run_once": False,
    }

    for k, v in headers.items():
        environ["HTTP_" + k.upper().replace("-", "_")] = v

    response_body = []
    status = []
    headers_out = []

    def start_response(status_code, headers_list):
        status.append(status_code)
        headers_out.extend(headers_list)

    result = app(environ, start_response)
    for data in result:
        response_body.append(data)
    body_str = b"".join(response_body).decode()

    return {
        "statusCode": int(status[0].split()[0]),
        "headers": dict(headers_out),
        "body": body_str
    }
