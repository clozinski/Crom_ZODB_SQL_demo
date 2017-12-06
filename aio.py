# -*- coding: utf-8 -*-

import os
from loader import Configuration


with Configuration('config.json') as config:

    # We read the zodb conf and initialize it
    from cromlech.zodb import init_db_from_file
    with open(config['zodb']['config'], 'r') as fd:
        db = init_db_from_file(fd)


    # We create our ZODB connection manager
    import transaction
    from cromlech.zodb.controlled import Connection

    class ZODBApplication(object):

        def __init__(self, db):
            self.db = db

        async def handle(self, request):
            with Connection(self.db, transaction.manager) as conn:
                with transaction.manager as tm:
                    root = conn.get_connection('demo1').root()
                    text = 'Root contains : %s' % str(root)
                    return web.Response(text=text)

    # Let serve our async app
    from aiohttp import web
    handle = ZODBApplication(db).handle
    app = web.Application()
    app.router.add_get('/', handle)
    web.run_app(app)
