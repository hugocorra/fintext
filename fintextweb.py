from bottle import TEMPLATE_PATH, jinja2_view, request, route, run, template
from parserlib import parser

import json

TEMPLATE_PATH[:] = ['templates']


@route('/')
@jinja2_view('index.html')
def index():
    return {'title': 'Hello world'}


@route('/retrieve', method='GET')
def retrieve():
    #from IPython import embed; embed()
    with open('database.json') as database:
        data = json.load(database)
        print('okokok')
        return {'status': 'OK', 'data': data}

    return {'status': 'error'} # TODO 404


@route('/post', method='POST')
def post():
    newdata = parser(request.json())

    try:
        with open('database.json') as database:
            data = json.load(database)

            if data is None:
                data = [newdata]
            else:
                data.append(newdata)
    except FileNotFoundError:
        data = [newdata]
        print('exception')
    finally:
        with open('database.json', 'w') as database:
            json.dump(data, database)

    return {'status': 'ok'}


run(host='localhost', port=8080, debug=True)
