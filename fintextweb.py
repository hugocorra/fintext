from bottle import TEMPLATE_PATH, jinja2_view, request, route, run, template

TEMPLATE_PATH[:] = ['templates']


@route('/')
@jinja2_view('index.html')
def index():
    return {'title': 'Hello world'}


@route('/post', method='POST')
def post():
    print('post')
    return {'status': 'ok'}


run(host='localhost', port=8080, debug=True)
