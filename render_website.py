import argparse
import json
import os

from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server
from more_itertools import chunked
from dotenv import load_dotenv


def render_site(json_file_path):
    with open(json_file_path, "r", encoding="utf-8") as json_file:
        books = json.load(json_file)
    env = Environment(
        loader=FileSystemLoader("."),
        autoescape=select_autoescape(["html"])
    )
    count_books_on_page = 20
    books_page = list(chunked(books, count_books_on_page))
    os.makedirs("pages", exist_ok=True)
    for page_id, page_with_books in enumerate(books_page, start=1):
        template = env.get_template("template.html")
        render_page = template.render(
            books=page_with_books,
            pages_count=len(books_page),
            selected_page=page_id
        )
        with open(f"pages/index{page_id}.html", "w", encoding="utf-8") as template:
            template.write(render_page)


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(
        prog='Online library',
        description='Online library for reading',
    )
    parser.add_argument("data_filepath", nargs="?", default=os.getenv("DEFAULT_DATA_FILEPATH"))
    args = parser.parse_args()
    if args.data_filepath:
        render_site(args.data_filepath)
    else:
        render_site("media/meta_data.json")
    server = Server()
    server.watch("template.html", lambda: render_site(args.data_filepath))
    server.serve(default_filename="pages/index1.html", root=".")


if __name__ == "__main__":
    main()
