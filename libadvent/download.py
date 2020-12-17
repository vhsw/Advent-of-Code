#!/usr/bin/env python3
"""Download input data and create answer template"""

import re
from datetime import datetime
from os import environ, makedirs
from os.path import isfile

import click
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv(verbose=True)


@click.command()
@click.argument(
    "date",
    type=click.DateTime(),
    default=datetime.now().strftime("%Y-%m-%d"),
)
def download(date):
    directory = f"{date.year}/Day {date.day:02d}/"
    makedirs(directory, exist_ok=True)
    url = f"https://adventofcode.com/{date.year}/day/{date.day}"
    req = requests.get(url, cookies={"session": environ["SESSION"]})
    soup = BeautifulSoup(req.text, "lxml")
    title = soup.select_one("body > main > article > h2")
    if match := re.match(r"--- Day \d+: (.+) ---", title.get_text()):
        name = re.sub(r"\W+", "_", match.group(1).lower()).strip("_") + ".py"
        if not isfile(directory + name):
            with open(directory + name, "w") as fp:
                fp.write(
                    f""""Day {date.day:02d} answers"
INPUT = "{directory}input.txt"


def part1(data):
    "Part 1 answer"


def part2(data):
    "Part 2 answer"


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.read()
    print(f"Part 1: {{ part1(DATA) }}")
    print(f"Part 2: {{ part2(DATA) }}")
"""
                )

    with open(directory + "input.txt", "w") as fp:
        req = requests.get(url + "/input", cookies={"session": environ["SESSION"]})
        fp.write(req.text)


if __name__ == "__main__":
    download()  # pylint: disable=no-value-for-parameter
