import os
from shutil import rmtree

from jinja2 import Template

script_dir = os.path.dirname(os.path.abspath(__file__))

template_dir = f"{script_dir}/templates"
out_dir = f"{script_dir}/../out"


def create_empty_output_folder():
    output_path = f"{script_dir}/../out"
    if os.path.exists(output_path):
        rmtree(output_path)
    os.makedirs(output_path)


def generate_index():
    with open(f"{template_dir}/index.html") as index_file:
        index_template = Template(index_file.read())
        file = open(f"{out_dir}/index.html", "w")
        file.write(index_template.render(headline="1wp"))


if __name__ == "__main__":
    print("Start generating the files for pages")

    create_empty_output_folder()
    generate_index()

    print("Finish generating the files")
