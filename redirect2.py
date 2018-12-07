import mitmproxy
from mitmproxy.models import HTTPResponse
from netlib.http import Headers
def request(flow):

    if flow.request.pretty_host.endswith("sojourncollege.com"):
            mitmproxy.ctx.log( flow.request.path )       
            flow.request.host = "cnn.com"
            flow.request.port = 80
            flow.request.headers["Host"] = "cnn.com"
            flow.response.status_code = 301
            flow.response.headers.append("Location")
            flow.response.headers["Location"] = "cnn.com"
