# -*- coding: utf-8 -*-

from cromlech.dawnlight import DawnlightPublisher
from cromlech.browser.interfaces import IView
from cromlech.dawnlight import ViewLookup, view_locator
from cromlech.webob.request import Request


def query_view(request, context, name=""):
    return IView.component(context, request, name=name)


view_lookup = ViewLookup(view_locator(query_view))
Publisher = DawnlightPublisher(view_lookup=view_lookup)


def demo1(environ, start_response):
    conn = environ["zodb.connection"].root().get_connection('demo1')
    root = conn.root()
    request = Request(environ)
    response = Publisher.publish(request, root, handle_errors=True)
    return response(environ, start_response)


def demo2(environ, start_response):
    conn = environ["zodb.connection"].root().get_connection('demo2')
    root = conn.root()
    request = Request(environ)
    response = Publisher.publish(request, root, handle_errors=True)
    return response(environ, start_response)
