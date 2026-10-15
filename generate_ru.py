#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OwlMind landing — генератор статической русской версии (/ru/*).
Каждая страница дублируется в /ru/ с русским текстом, каноническим URL,
hreflang-ссылками и ссылочным переключателем языка (без клиентского i18n.js,
чтобы поисковики индексировали именно русский текст).

Запуск: python3 generate_ru.py
"""
import os
import re
from bs4 import BeautifulSoup, NavigableString

ROOT = os.path.dirname(os.path.abspath(__file__))
BASE = "https://owlmind.dev"

# все страницы сайта (относительный путь -> URL-путь без index.html)
PAGES = [
    ("index.html", ""),
    ("banking/index.html", "banking/"),
    ("casino/index.html", "casino/"),
    ("crypto/index.html", "crypto/"),
    ("pentest/index.html", "pentest/"),
    ("smart-contract-audit/index.html", "smart-contract-audit/"),
    ("blog/index.html", "blog/"),
    ("blog/casino-audit-prep/index.html", "blog/casino-audit-prep/"),
    ("blog/crypto-exchange-vulnerabilities/index.html", "blog/crypto-exchange-vulnerabilities/"),
    ("blog/payment-system-pentest/index.html", "blog/payment-system-pentest/"),
    ("blog/smart-contract-audit-guide/index.html", "blog/smart-contract-audit-guide/"),
    ("blog/sql-injection-core-banking/index.html", "blog/sql-injection-core-banking/"),
    ("blog/provably-fair-casino-rng/index.html", "blog/provably-fair-casino-rng/"),
    ("blog/withdrawal-race-conditions/index.html", "blog/withdrawal-race-conditions/"),
    ("blog/hardcoded-credentials-production/index.html", "blog/hardcoded-credentials-production/"),
    ("blog/idor-account-takeover/index.html", "blog/idor-account-takeover/"),
    ("blog/otp-2fa-bypass/index.html", "blog/otp-2fa-bypass/"),
    ("blog/smart-contract-reentrancy/index.html", "blog/smart-contract-reentrancy/"),
    ("blog/cors-financial-api/index.html", "blog/cors-financial-api/"),
    ("privacy.html", "privacy.html"),
]

# внутренние пути, которые НЕ должны получать префикс /ru/
SKIP_PREFIX = ("/style.css", "/js/", "/og-image", "/demo.mp4", "/robots.txt",
               "/sitemap.xml", "/security.txt", "/.well-known", "/favicon")


def en_url(path):
    return BASE + "/" + path


def ru_url(path):
    return BASE + "/ru/" + path


def first_text(el):
    """Вернуть первый прямой текстовый узел (NavigableString) элемента или None."""
    for c in el.contents:
        if isinstance(c, NavigableString):
            return c
    return None


def apply_ru_text(soup):
    """Подставить русский текст из data-ru во все элементы, кроме meta/title/script."""
    for el in soup.find_all(attrs={"data-ru": True}):
        if el.name in ("meta", "title", "script", "style", "link"):
            continue
        ru = el.get("data-ru")
        if not ru:
            continue
        txt_nodes = [c for c in el.contents if isinstance(c, NavigableString)]
        elem_nodes = [c for c in el.contents if not isinstance(c, NavigableString)]
        for c in txt_nodes:
            c.extract()
        if elem_nodes:
            elem_nodes[0].insert_before(NavigableString(ru))
        else:
            el.append(NavigableString(ru))


def set_meta_content(soup, key, keyval, content):
    """Найти <meta key="keyval"> и установить его content."""
    for m in soup.find_all("meta", attrs={key: keyval}):
        m["content"] = content


def add_hreflang(soup, path):
    """Добавить alternate-ссылки (en/ru/x-default) в <head>."""
    # удалить старые alternate, если есть
    for a in soup.find_all("link", rel="alternate"):
        a.decompose()
    head = soup.head
    if not head:
        return
    links = [
        ("en", en_url(path)),
        ("ru", ru_url(path)),
        ("x-default", en_url(path)),
    ]
    for hreflang, href in links:
        t = soup.new_tag("link", rel="alternate", hreflang=hreflang, href=href)
        head.append(t)


def add_hreflang_en(soup, path):
    """Для EN-страницы: добавить alternate на ru + x-default (en уже канонична)."""
    for a in soup.find_all("link", rel="alternate"):
        a.decompose()
    head = soup.head
    if not head:
        return
    for hreflang, href in (("ru", ru_url(path)), ("x-default", en_url(path))):
        t = soup.new_tag("link", rel="alternate", hreflang=hreflang, href=href)
        head.append(t)


def make_ru_lang_links(soup, path):
    """Заменить кнопки EN/RU на ссылки, ведущие между версиями."""
    for b in soup.find_all("button", attrs={"data-lang-toggle": True}):
        lang = b.get("data-lang")
        a = soup.new_tag("a")
        a["class"] = "lang-link"
        a["href"] = ru_url(path) if lang == "ru" else en_url(path)
        a["data-lang"] = lang
        a.string = lang.upper()
        b.replace_with(a)


def canonical_to(soup, url):
    # убрать старый canonical, поставить новый
    for c in soup.find_all("link", rel="canonical"):
        c.decompose()
    if soup.head:
        c = soup.new_tag("link", rel="canonical", href=url)
        soup.head.append(c)


def generate_ru_page(src_rel, path):
    src = os.path.join(ROOT, src_rel)
    with open(src, encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "lxml")

    # язык
    soup.html["lang"] = "ru"

    # title
    title = soup.find("title")
    if title and title.get("data-ru"):
        title.string = title["data-ru"]

    # meta description
    md = soup.find("meta", attrs={"name": "description"})
    if md and md.get("data-ru"):
        md["content"] = md["data-ru"]

    # og/twitter — русские значения
    if title:
        set_meta_content(soup, "property", "og:title", title.string)
        set_meta_content(soup, "name", "twitter:title", title.string)
    if md:
        set_meta_content(soup, "property", "og:description", md["content"])
        set_meta_content(soup, "name", "twitter:description", md["content"])

    # og:locale и og:url
    for m in soup.find_all("meta", attrs={"property": "og:locale"}):
        m["content"] = "ru_RU"
    set_meta_content(soup, "property", "og:url", ru_url(path))

    # русский текст в теле
    apply_ru_text(soup)

    # внутренние ссылки -> /ru/
    for a in soup.find_all("a", href=True):
        h = a["href"]
        if not h.startswith("/") or h.startswith("//"):
            continue
        if any(h.startswith(x) for x in SKIP_PREFIX):
            continue
        if h == "/":
            a["href"] = "/ru/"
        elif h.startswith("/ru"):
            continue
        else:
            a["href"] = "/ru" + h

    # убрать клиентский i18n (иначе Google проиндексирует EN-текст после рендера)
    for s in soup.find_all("script"):
        if s.get("src") and s["src"].endswith("/js/i18n.js"):
            s.decompose()

    # переключатель языка — ссылками
    make_ru_lang_links(soup, path)

    # canonical + hreflang
    canonical_to(soup, ru_url(path))
    add_hreflang(soup, path)

    # сохранить
    dst_rel = ("ru/" + src_rel) if src_rel != "index.html" else "ru/index.html"
    if src_rel == "privacy.html":
        dst_rel = "ru/privacy.html"
    dst = os.path.join(ROOT, dst_rel)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, "w", encoding="utf-8") as f:
        f.write(str(soup))
    return dst


def update_en_hreflang(src_rel, path):
    """Добавить hreflang-ссылки в оригинальные EN-страницы строковой вставкой
    (без bs4, чтобы не переформатировать файл)."""
    src = os.path.join(ROOT, src_rel)
    with open(src, encoding="utf-8") as f:
        html = f.read()
    if 'hreflang="ru"' in html:
        return
    links = (
        f'<link rel="alternate" hreflang="ru" href="{ru_url(path)}">\n'
        f'<link rel="alternate" hreflang="x-default" href="{en_url(path)}">'
    )
    html = html.replace("</head>", links + "\n</head>", 1)
    with open(src, "w", encoding="utf-8") as f:
        f.write(html)


def main():
    created = []
    for src_rel, path in PAGES:
        created.append(generate_ru_page(src_rel, path))
        update_en_hreflang(src_rel, path)
        print("OK  ", src_rel, "->", ru_url(path))
    print("\nГотово. Создано русских страниц:", len(created))


if __name__ == "__main__":
    main()
