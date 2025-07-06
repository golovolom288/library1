import json
import os

from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server
from more_itertools import chunked


def render_site():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html'])
    )
    count_books_on_page = 20
    with open("media/meta_data.json", "r+", encoding="utf-8") as json_file:
        books = json.load(json_file)
    books = list(chunked(books, count_books_on_page))
    os.makedirs("pages", exist_ok=True)
    for page_id, page_with_books in enumerate(books, 1):
        template = env.get_template('template.html')
        render_page = template.render(books=list(chunked(page_with_books, 2)), pages_count=len(books), selected_page=page_id)
        with open(f"pages/index{page_id}.html", "w+", encoding="utf-8") as template:
            template.write(render_page)
            template.close()


def main():
    render_site()
    server = Server()
    server.watch('template.html', render_site)
    server.serve(default_filename="pages/index1.html", root=".")


if __name__ == "__main__":
    main()
