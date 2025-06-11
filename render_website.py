from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
from flask import render_template
from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html'])
)
template = env.get_template('template.html')

with open("media/meta_data.json", "r+", encoding="utf-8") as json_file:
    books = json.load(json_file)

render_page = template.render(books=books)

with open("index.html", "w+", encoding="utf-8") as template:
    template.write(render_page)


server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
