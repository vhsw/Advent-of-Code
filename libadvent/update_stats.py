#!/usr/bin/env python3
"""Update stats section in README.md"""

import re
from os import environ

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv(verbose=True)


def update_stats():
    url = "https://adventofcode.com/2020/events"
    req = requests.get(url, cookies={"session": environ["SESSION"]})
    soup = BeautifulSoup(req.text, "lxml")
    stats = soup.select('body > main > article > div[class="eventlist-event"]')
    text = "## Stats\n\n"
    total = 0
    for s in stats:
        line = s.get_text()
        year, stars = re.match(r"\[(\d{4})\] +(\d+)", line).groups()
        if not stars:
            stars = 0
        stars = int(stars)
        total += stars
        badge = ":star:"
        if stars == 50:
            badge = ":star2:"
        text += f"- {year}: {stars:02d} {badge}\n"

    text += f"\nTotal stars: {total} :star:\n"
    with open("README.md") as fp:
        data = fp.read()
        head, _ = data.rsplit("## Stats", 1)
    with open("README.md", "w") as fp:
        fp.write(head + text)


if __name__ == "__main__":
    update_stats()
