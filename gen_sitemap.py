#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Генератор sitemap.xml с hreflang (EN + RU) по списку страниц из generate_ru."""
import os
from generate_ru import PAGES, BASE

ROOT = os.path.dirname(os.path.abspath(__file__))
LAST = "2026-10-16"


def en(path):
    return BASE + "/" + path


def ru(path):
    return BASE + "/ru/" + path


def main():
    urls = []
    for _, path in PAGES:
        e, r = en(path), ru(path)
        block = (
            "  <url>\n"
            f"    <loc>{e}</loc>\n"
            f"    <lastmod>{LAST}</lastmod>\n"
            f'    <xhtml:link rel="alternate" hreflang="en" href="{e}"/>\n'
            f'    <xhtml:link rel="alternate" hreflang="ru" href="{r}"/>\n'
            f'    <xhtml:link rel="alternate" hreflang="x-default" href="{e}"/>\n'
            "  </url>\n"
        )
        urls.append(block)

    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
        'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        + "".join(urls)
        + "</urlset>\n"
    )

    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(xml)
    print(f"Готово. Страниц в sitemap: {len(urls)}")


if __name__ == "__main__":
    main()
