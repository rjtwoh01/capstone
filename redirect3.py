import mitmproxy
from mitmproxy.models import HTTPResponse
from netlib.http import Headers
from libmproxy.flow import Response
from netlib.odict import ODictCaseless

def request(flow):

    if flow.request.pretty_host.endswith("sojourncollege.com"):
        resp = Response(flow.request,
                        [1,1],
                        302, "OK",
                        ODictCaseless([["Content-Type","text/html"]]),
                        "helloworld",
                        None)
        flow.request.reply(resp)
    if flow.request.host.endswith("sojourncollege.com"):
        flow.request.host = "mitmproxy.org"
        flow.request.headers["Host"] = ["mitmproxy.org"]