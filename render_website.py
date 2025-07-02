import json
import math
import os

from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server
from more_itertools import chunked


def render_site():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html'])
    )

    with open("media/meta_data.json", "r+", encoding="utf-8") as json_file:
        books = json.load(json_file)
    books = list(chunked(books, 20))
    os.makedirs("pages", exist_ok=True)
    for i, twenty_books in enumerate(books, 1):
        template = env.get_template('template.html')
        render_page = template.render(books=list(chunked(twenty_books, 2)), pages_count=len(books), selected_page=i)
        with open(f"pages/index{i}.html", "w+", encoding="utf-8") as template:
            template.write(render_page)
            template.close()


render_site()
server = Server()
server.watch('template.html', render_site)
server.serve(default_filename="pages/index1.html", root=".")
