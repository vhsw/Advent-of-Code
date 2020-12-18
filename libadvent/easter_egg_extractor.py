#!/usr/bin/env python3
"""easter egg extractor"""

from datetime import datetime
from os import environ

import click
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv(verbose=True)


def download(year, day):
    url = f"https://adventofcode.com/{year}/day/{day}"
    req = requests.get(url, cookies={"session": environ["SESSION"]})
    soup = BeautifulSoup(req.text, "lxml")
    for p in soup.select("p"):
        for span in p.select("span"):
            text = span.get("title")
            if text:
                span.replace_with(f"(egg: {text})")
                print(p.get_text())


@click.command()
@click.argument(
    "date",
    type=click.DateTime(),
    default=datetime.now().strftime("%Y-%m-%d"),
)
def main(date: datetime):
    download(date.year, date.day)


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter
