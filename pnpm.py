import requests
import configparser
import sys
import os
import argparse

config = configparser.ConfigParser()
parser = argparse.ArgumentParser()


parser.add_argument("-fws", action="extend", nargs="+", required=True)


with open(
    f"{os.path.dirname(os.path.realpath(__file__))}/pnpm.config", "r", encoding="utf-8"
) as file:
    config.read_file(file)


frameworks = vars(parser.parse_args()).get("fws")

selected_frameworks = filter(lambda item: item in config.sections(), frameworks)


def UseSections():
    sections = []

    return [
        sections,
        lambda section: sections.append(
            {"icon": section["icon"], "name": section["name"]}
        ),
    ]


def run(secs):
    try:
        get_package_info(*secs)
        print_to_polybar(*secs)
    except Exception:
        print(Exception)


def get_package_info(*sections):
    for section in sections:
        try:
            response = requests.get(
                f"https://registry.npmjs.org/{section.get('name')}/latest"
            )
            data = response.json()

            section["version"] = data.get("version")
        except Exception:
            print("Something went wrong")


def print_to_polybar(*sections):
    for section in sections:
        try:
            sys.stdout.write(f'{section.get("icon")} {section.get("version")}')
            sys.stdout.write("  ")
        except Exception:
            print(Exception)


secs, use_append = UseSections()

for section in list(selected_frameworks):
    use_append(config[section])


run(secs)
