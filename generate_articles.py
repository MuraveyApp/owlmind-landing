#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Генератор статей блога OwlMind. Каждая статья сразу на EN+RU (data-атрибуты)."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
BASE = "https://owlmind.dev"

NAV = '''<nav>
<div class="nav-inner">
  <a href="/" class="logo"><i>Owl</i>Mind</a>
  <div class="nav-links">
    <a href="/#industries" class="hide-m" data-en="Industries" data-ru="Отрасли">Industries</a>
    <a href="/casino/" data-en="Casino" data-ru="Казино">Casino</a>
    <a href="/crypto/" data-en="Crypto" data-ru="Крипто">Crypto</a>
    <a href="/banking/" data-en="Banking" data-ru="Банки">Banking</a>
    <a href="/smart-contract-audit/" data-en="Smart Contract" data-ru="Смарт-контракты">Smart Contract</a>
    <a href="mailto:devowlmind@gmail.com?subject=Pentest" class="btn-nav" data-en="Contact Us" data-ru="Связаться">Contact Us</a>
    <div class="lang-toggle" role="group" aria-label="Language">
      <button type="button" data-lang="en" data-lang-toggle>EN</button>
      <button type="button" data-lang="ru" data-lang-toggle>RU</button>
    </div>
  </div>
</div>
</nav>'''

FOOTER = '''<footer>
<div class="footer-inner">
<div style="display:flex;align-items:center;gap:8px"><span style="font-weight:700;color:var(--dim2)">OwlMind Security</span></div>
<div class="footer-links">
<a data-en="Home" data-ru="Главная" href="/">Home</a>
<a data-en="Casino" data-ru="Казино" href="/casino/">Casino</a>
<a data-en="Crypto" data-ru="Крипто" href="/crypto/">Crypto</a>
<a data-en="Banking" data-ru="Банки" href="/banking/">Banking</a>
<a data-en="Smart Contract" data-ru="Смарт-контракты" href="/smart-contract-audit/">Smart Contract</a>
</div>
<p>© 2026 OwlMind Security. <span data-en="All rights reserved." data-ru="Все права защищены.">All rights reserved.</span></p>
</div>
</footer>
<script src="/js/i18n.js"></script>
</body>
</html>'''


def li(item, mark="✓"):
    return f'<li><span>{mark}</span> <span data-en="{item[0]}" data-ru="{item[1]}">{item[0]}</span></li>'


def render_article(a):
    sections = ""
    for s in a["sections"]:
        sections += f'<section>\n<h2 data-en="{s["h2_en"]}" data-ru="{s["h2_ru"]}">{s["h2_en"]}</h2>\n'
        for p in s.get("paras", []):
            sections += f'<p data-en="{p[0]}" data-ru="{p[1]}">{p[0]}</p>\n'
        if s.get("list"):
            mark = s.get("mark", "✓")
            sections += '<ul class="sub-list">\n'
            for it in s["list"]:
                sections += li(it, mark) + "\n"
            sections += "</ul>\n"
        if s.get("outcome"):
            sections += f'<div class="sub-outcome" data-en="{s["outcome"][0]}" data-ru="{s["outcome"][1]}">{s["outcome"][0]}</div>\n'
        sections += "</section>\n"

    faq = ""
    for q in a.get("faq", []):
        faq += f'<div class="faq-item"><h4 data-en="{q[0]}" data-ru="{q[1]}">{q[0]}</h4><p data-en="{q[2]}" data-ru="{q[3]}">{q[2]}</p></div>\n'
    if faq:
        sections += f'<section>\n<h2 data-en="FAQ" data-ru="Вопросы">FAQ</h2>\n{faq}</section>\n'

    cta_subject = a.get("cta_subject", "Consultation")
    cta = f'''<section class="s-border">
<div class="express-box">
<h3 data-en="{a["cta_en"]}" data-ru="{a["cta_ru"]}">{a["cta_en"]}</h3>
<div class="sub" data-en="{a["cta_sub_en"]}" data-ru="{a["cta_sub_ru"]}">{a["cta_sub_en"]}</div>
<a class="btn-hero primary" data-en="{a["cta_btn_en"]}" data-ru="{a["cta_btn_ru"]}" href="mailto:devowlmind@gmail.com?subject={cta_subject}" style="font-size:16px;padding:16px 40px;display:inline-block">{a["cta_btn_en"]}</a>
</div>
</section>'''

    url = f"{BASE}/blog/{a['slug']}/"
    html = f'''<!DOCTYPE html>
<html lang="en" class="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title data-en="{a["title_en"]}" data-ru="{a["title_ru"]}">{a["title_en"]}</title>
<meta name="description" data-en="{a["desc_en"]}" data-ru="{a["desc_ru"]}" content="{a["desc_en"]}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{a["title_en"]}">
<meta property="og:description" content="{a["og_desc"]}">
<meta property="og:type" content="article">
<meta property="og:url" content="{url}">
<meta property="og:image" content="https://owlmind.dev/og-image.png">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>&#129417;</text></svg>">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@600;700;800&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/style.css">
</head>
<body>

{NAV}
<div class="sub-hero">
<div class="hero-bg"></div>
<div class="hero-grid"></div>
<div class="hero-content">
<div class="breadcrumb"><a data-en="Home" data-ru="Главная" href="/">Home</a> &nbsp;/&nbsp; <span data-en="Blog" data-ru="Блог">Blog</span> &nbsp;/&nbsp; <span data-en="{a["bc_en"]}" data-ru="{a["bc_ru"]}">{a["bc_en"]}</span></div>
<h1><span data-en="{a["h1_en"]}" data-ru="{a["h1_ru"]}">{a["h1_en"]}</span></h1>
<p data-en="{a["hero_en"]}" data-ru="{a["hero_ru"]}">{a["hero_en"]}</p>
<div class="hero-btns"><a class="btn-hero primary" data-en="{a["cta_btn_en"]}" data-ru="{a["cta_btn_ru"]}" href="mailto:devowlmind@gmail.com?subject={cta_subject}">{a["cta_btn_en"]}</a></div>
</div>
</div>
<div class="sub-section">
{sections}{cta}
</div>
{FOOTER}'''
    return html


ARTICLES = [
    {
        "slug": "sql-injection-core-banking",
        "title_en": "SQL Injection in Core Banking — How It Happens and How to Find It — OwlMind Security",
        "title_ru": "SQL-инъекция в ядре банка — как это происходит и как её найти — OwlMind Security",
        "desc_en": "How SQL injection reaches a core banking system, why scanners miss it, and the fix that closes it. Real findings, anonymised, from a CIS bank engagement.",
        "desc_ru": "Как SQL-инъекция добирается до ядра банка, почему её пропускают сканеры и как её закрыть. Обезличенные находки из проверки банка в СНГ.",
        "og_desc": "How SQL injection reaches a core banking system — and why scanners miss it.",
        "bc_en": "SQL Injection in Banking", "bc_ru": "SQL-инъекция в банке",
        "h1_en": "SQL Injection in Core Banking", "h1_ru": "SQL-инъекция в ядре банка",
        "hero_en": "One unsanitised parameter on an internal portal, and an attacker is reading customer accounts. Here is the real path a banking SQLi takes.",
        "hero_ru": "Один неочищенный параметр на внутреннем портале — и злоумышленник читает счета клиентов. Вот реальный путь банковской SQL-инъекции.",
        "cta_en": "Find the Injection Before an Attacker Does", "cta_ru": "Найдите инъекцию раньше злоумышленника",
        "cta_sub_en": "Send us your banking scope — proposal within 48 hours.", "cta_sub_ru": "Пришлите контур банка — предложение в течение 48 часов.",
        "cta_btn_en": "Request a Banking Audit", "cta_btn_ru": "Заказать аудит банка",
        "cta_subject": "Banking%20Audit",
        "sections": [
            {"h2_en": "The Real Path of a Banking SQLi", "h2_ru": "Реальный путь банковской SQL-инъекции",
             "paras": [
                ("A core banking injection rarely starts on the public site. It starts one or two hops inside: an admin portal, a support panel, a legacy web service that talks to the database with a concatenated query. The perimeter looks clean, so the query was never reviewed.",
                 "Инъекция в ядре банка редко начинается на публичном сайте. Она начинается на один-два шага глубже: админ-портал, панель поддержки, устаревший веб-сервис, который склеивает запрос к базе. Периметр выглядит чистым, поэтому запрос никто не проверял."),
                ("Once the first union or error-based response works, the attacker maps the schema and escalates to reading account balances, transaction logs and card tables — often with the database account that has the broadest rights, because it was convenient at the time.",
                 "Как только срабатывает первый union или вывод через ошибку, злоумышленник рисует схему и доходит до чтения остатков, истории проводок и карточных таблиц — часто под учёткой базы с самыми широкими правами, потому что так было удобно."),
             ],
             "list": [
                ("Internal and support panels are the weakest link", "Внутренние панели и панели поддержки — слабейшее звено"),
                ("Legacy web services concatenate queries directly", "Устаревшие веб-сервисы склеивают запросы напрямую"),
                ("Database accounts run with far too many privileges", "Учётки базы работают со слишком широкими правами"),
                ("Error messages leak schema and column names", "Сообщения об ошибках выдают схему и имена колонок"),
             ]},
            {"h2_en": "Why Scanners Miss It", "h2_ru": "Почему сканеры это пропускают",
             "paras": [
                ("An automated scanner sees a parameter, sends a quote, checks for a signature, and moves on. A banking SQLi often hides behind multi-step flows, custom encoding, or a WAF that the app itself bypasses on internal calls. You need a human who follows the money and the login walls to the actual query.",
                 "Сканер видит параметр, шлёт кавычку, проверяет сигнатуру и идёт дальше. Банковская инъекция часто прячется за многошаговыми сценариями, своей кодировкой или за WAF, который само приложение обходит на внутренних вызовах. Нужен человек, который идёт за деньгами и за стенами входа до реального запроса."),
             ]},
            {"h2_en": "How to Close It", "h2_ru": "Как это закрыть",
             "list": [
                ("Parameterised queries everywhere — no string-built SQL", "Параметризованные запросы везде — никакой SQL из строк"),
                ("Least-privilege database accounts per service", "Для каждого сервиса — учётка базы с минимальными правами"),
                ("Suppress verbose errors in production", "Глушить подробные ошибки в проде"),
                ("Audit the internal surface, not just the public site", "Аудировать внутренний контур, а не только публичный сайт"),
             ],
             "mark": "1",
             "outcome": ("A fixed core means customer accounts stay private, and a regulator question gets a concrete answer instead of a panic.",
                         "Закрытое ядро — это приватные счета клиентов и конкретный ответ регулятору вместо паники.")},
        ],
        "faq": [
            ("Do you need production access to find a banking SQLi?", "Нужен ли доступ в прод, чтобы найти SQL-инъекцию?",
             "Most findings reproduce on a staging or UAT environment that mirrors the portal and database. Live verification, when required, runs in an agreed window.",
             "Большинство находок воспроизводится на staging или UAT с тем же порталом и базой. Проверка на проде — только в согласованное окно."),
            ("Is this legal to test?", "Законно ли это тестировать?",
             "Yes — under an NDA and a signed scope. We test only systems you own or are authorised to assess.",
             "Да — под NDA и подписанный объём. Проверяем только системы, которыми вы владеете или на которые есть разрешение."),
        ],
    },
    {
        "slug": "provably-fair-casino-rng",
        "title_en": "Provably Fair Is Not Always Fair — Server-Seed Leaks in Casinos — OwlMind Security",
        "title_ru": "Provably fair не всегда честен — утечки server seed в казино — OwlMind Security",
        "desc_en": "How a crash-game server seed leaks before the round, why provably-fair maths does not save you, and how to check your RNG pipeline.",
        "desc_ru": "Как server seed краш-игры утекает до раунда, почему математика provably fair не спасает и как проверить контур случайности.",
        "og_desc": "How a crash-game server seed leaks before the round — and breaks fairness.",
        "bc_en": "Provably Fair RNG", "bc_ru": "Provably fair и RNG",
        "h1_en": "Provably Fair Is Not Always Fair", "h1_ru": "Provably fair не всегда честен",
        "hero_en": "The maths can be sound while the game is still rigged — because the seed leaks before the round. Here is the most common fairness break in crash games.",
        "hero_ru": "Математика может быть верной, а игра всё равно подстроенной — потому что seed утекает до раунда. Вот самый частый разлом честности в краш-играх.",
        "cta_en": "Prove Your Games Are Fair", "cta_ru": "Докажите честность своих игр",
        "cta_sub_en": "Send us your game scope — fairness audit proposal within 48 hours.", "cta_sub_ru": "Пришлите контур игр — предложение по аудиту честности за 48 часов.",
        "cta_btn_en": "Request a Fairness Audit", "cta_btn_ru": "Заказать аудит честности",
        "cta_subject": "Casino%20Audit",
        "sections": [
            {"h2_en": "How Fairness Breaks", "h2_ru": "Как ломается честность",
             "paras": [
                ("Provably fair works because the server commits to a hash of the seed before the round, then reveals it after. The moment the raw seed is disclosed early — in a debug endpoint, a WebSocket message, a log, an API response — a player can predict the crash point and always cash out at the top.",
                 "Provably fair работает, потому что сервер до раунда фиксирует хэш seed, а после — раскрывает его. Как только сырой seed утекает раньше — в отладочном эндпоинте, сообщении вебсокета, логе, ответе API — игрок предсказывает точку краша и всегда забирает на пике."),
                ("We have seen the seed arrive in the round payload itself, alongside the hash that was supposed to hide it. The audit that catches this looks at the whole real-time channel, not just the game maths.",
                 "Мы видели, как seed приходит в самом теле раунда — рядом с хэшем, который должен был его прятать. Аудит, который это ловит, смотрит на весь реалтайм-канал, а не только на математику игры."),
             ],
             "list": [
                ("Raw server seed disclosed before the round ends", "Сырой server seed раскрыт до конца раунда"),
                ("Seed leaked in WebSocket frames or debug endpoints", "Seed утёк в кадрах вебсокета или отладочных эндпоинтах"),
                ("Hash commitment missing or made after the fact", "Фиксация хэша отсутствует или сделана постфактум"),
                ("Predictable or reused seeds across rounds", "Предсказуемые или повторяющиеся seed между раундами"),
             ]},
            {"h2_en": "What This Costs a Casino", "h2_ru": "Во что это обходится казино",
             "paras": [
                ("A predictable crash point means a smart player withdraws every time. Regulators, game providers and affiliate networks all audit fairness before they trust you — and a broken provably-fair chain is a licence risk, not a bug.",
                 "Предсказуемая точка краша — это умный игрок, который выводит каждый раз. Регуляторы, провайдеры игр и партнёрские сети проверяют честность, прежде чем вам довериться, — а сломанная цепочка provably fair это риск лицензии, а не баг."),
             ]},
            {"h2_en": "How We Check an RNG Pipeline", "h2_ru": "Как мы проверяем контур случайности",
             "list": [
                ("Map the full round flow: bet → seed → result → payout", "Картируем весь цикл раунда: ставка → seed → результат → выплата"),
                ("Watch the live WebSocket channel for early seed or result", "Смотрим живой канал вебсокета на ранний seed или результат"),
                ("Verify the hash commitment is made before the bet closes", "Проверяем, что фиксация хэша сделана до закрытия ставки"),
                ("Test seed generation for predictability and reuse", "Тестируем генерацию seed на предсказуемость и повторное использование"),
             ],
             "mark": "1",
             "outcome": ("A fairness report you can show regulators and game providers — your games stay provably fair, your funds stay where they belong.",
                         "Отчёт о честности, который можно показать регуляторам и провайдерам игр — игры остаются provably fair, а деньги на месте.")},
        ],
        "faq": [
            ("Do you test live games?", "Вы тестируете живые игры?",
             "We test the fairness pipeline end to end in staging and, where agreed, on live with isolated fixtures — never against real player balances.",
             "Проверяем контур честности целиком на staging и, по согласованию, на проде на изолированных данных — никогда против балансов реальных игроков."),
            ("Which games do you cover?", "Какие игры вы покрываете?",
             "Crash games, slots, roulette, card games, and any custom RNG — including the game-provider integrations behind them.",
             "Краш-игры, слоты, рулетку, карточные игры и любой свой RNG — включая интеграции провайдеров за ними."),
        ],
    },
    {
        "slug": "withdrawal-race-conditions",
        "title_en": "Withdrawal Race Conditions — Double-Spend on Cashout — OwlMind Security",
        "title_ru": "Гонка на выводе средств — двойная трата при кэшауте — OwlMind Security",
        "desc_en": "How a race condition lets two parallel withdrawals drain one balance, why it happens in exchanges and casinos, and how to close the window.",
        "desc_ru": "Как гонка позволяет двум параллельным выводам обнулить один баланс, почему это бывает на биржах и в казино и как закрыть окно.",
        "og_desc": "How two parallel withdrawals drain one balance — and how to close the race.",
        "bc_en": "Withdrawal Race Conditions", "bc_ru": "Гонки на выводе",
        "h1_en": "Withdrawal Race Conditions", "h1_ru": "Гонка на выводе средств",
        "hero_en": "Two requests, one balance, a window of microseconds. When the balance check and the debit are not atomic, money leaves twice.",
        "hero_ru": "Два запроса, один баланс, окно в микросекунды. Когда проверка баланса и списание не атомарны, деньги уходят дважды.",
        "cta_en": "Close the Race Before It Drains You", "cta_ru": "Закройте гонку раньше, чем она вас обнулит",
        "cta_sub_en": "Send us your withdrawal flow — race-condition assessment within 48 hours.", "cta_sub_ru": "Пришлите контур вывода — оценка гонок в течение 48 часов.",
        "cta_btn_en": "Request a Race Audit", "cta_btn_ru": "Заказать аудит гонок",
        "cta_subject": "Race%20Audit",
        "sections": [
            {"h2_en": "The Mechanics of the Race", "h2_ru": "Механика гонки",
             "paras": [
                ("A withdrawal is a read-then-write: check the balance, then debit it. If those two steps are separate and the request is fast enough, two parallel requests both read the same balance before either debits. Both are approved, and the account goes negative — or a float account pays twice.",
                 "Вывод — это прочитать и записать: проверить баланс, затем списать. Если эти два шага разделены, а запрос достаточно быстрый, два параллельных запроса оба читают один баланс раньше любого списания. Оба одобряются — счёт уходит в минус или расчётный счёт платит дважды."),
                ("On a crypto exchange or a casino cashout this is direct money loss, and it is only visible when someone deliberately fires the same withdrawal in parallel. Normal testing never does that.",
                 "На криптобирже или кэшауте казино это прямая потеря денег, и видно её только когда кто-то намеренно шлёт один и тот же вывод параллельно. Обычное тестирование так не делает."),
             ],
             "list": [
                ("Balance check and debit are separate operations", "Проверка баланса и списание — отдельные операции"),
                ("No idempotency key on the withdrawal request", "Нет ключа идемпотентности на запросе вывода"),
                ("Parallel requests both pass the balance check", "Параллельные запросы оба проходят проверку баланса"),
                ("Race window widens under load or slow database", "Окно гонки шире под нагрузкой или при медленной базе"),
             ]},
            {"h2_en": "Where We See It Most", "h2_ru": "Где это встречается чаще всего",
             "paras": [
                ("Withdrawal, cashout, redeem, refund, bonus claim — any flow that moves value in a read-then-write pattern. Exchanges and casinos are the most exposed because the flows are public and the incentive to try is high.",
                 "Вывод, кэшаут, погашение, возврат, бонус — любой поток, который двигает ценность по схеме «прочитал — записал». Биржи и казино уязвимее всего, потому что потоки публичные, а стимул попробовать высокий."),
             ]},
            {"h2_en": "How to Close It", "h2_ru": "Как это закрыть",
             "list": [
                ("Make check-and-debit atomic in one transaction", "Сделать проверку и списание атомарными в одной транзакции"),
                ("Add an idempotency key and reject duplicates", "Добавить ключ идемпотентности и отклонять дубли"),
                ("Lock the balance row during the withdrawal", "Блокировать строку баланса на время вывода"),
                ("Re-test with single-packet parallel requests", "Перепроверить однопакетными параллельными запросами"),
             ],
             "mark": "1",
             "outcome": ("A cashout flow that cannot be double-spent — and proof of it for your partners and auditors.",
                         "Поток кэшаута, который нельзя удвоить — и доказательство этого для партнёров и аудиторов.")},
        ],
        "faq": [
            ("How do you prove a race exists?", "Как вы доказываете, что гонка есть?",
             "We fire the same withdrawal with HTTP/2 single-packet parallelism and show both requests approved against one balance — with a negative control that a normal serial withdrawal is rejected correctly.",
             "Шлём один и тот же вывод однопакетным параллелизмом HTTP/2 и показываем, что оба запроса одобрены против одного баланса — с отрицательным контролем, где обычный последовательный вывод корректно отклоняется."),
            ("Do you move real funds to test it?", "Вы двигаете реальные средства для проверки?",
             "No. Tests run on isolated fixtures and test accounts, never on customer balances.",
             "Нет. Проверки идут на изолированных данных и тестовых счетах, никогда на балансах клиентов."),
        ],
    },
    {
        "slug": "hardcoded-credentials-production",
        "title_en": "Hardcoded Credentials in Production — The Demo Login That Never Died — OwlMind Security",
        "title_ru": "Захардкоженные креды в проде — демо-логин, который не умер — OwlMind Security",
        "desc_en": "How a demo or default login reaches production, why it is the fastest path to full compromise, and how to hunt every hardcoded secret.",
        "desc_ru": "Как демо-логин по умолчанию попадает в прод, почему это самый быстрый путь к полной компрометации и как вычистить все захардкоженные секреты.",
        "og_desc": "How a demo login reaches production — and becomes the fastest path to compromise.",
        "bc_en": "Hardcoded Credentials", "bc_ru": "Захардкоженные креды",
        "h1_en": "Hardcoded Credentials in Production", "h1_ru": "Захардкоженные креды в проде",
        "hero_en": "A demo login shipped with a casino lobby, an AES key left in a mobile bundle, a database password in a config. Hardcoded secrets are the shortest route to a breach.",
        "hero_ru": "Демо-логин, уехавший вместе с лобби казино, AES-ключ в мобильном бандле, пароль от базы в конфиге. Захардкоженные секреты — кратчайший путь к взлому.",
        "cta_en": "Hunt Every Hardcoded Secret", "cta_ru": "Вычистите все захардкоженные секреты",
        "cta_sub_en": "Send us your code and configs — secret scan within 48 hours.", "cta_sub_ru": "Пришлите код и конфиги — поиск секретов в течение 48 часов.",
        "cta_btn_en": "Request a Secret Hunt", "cta_btn_ru": "Заказать поиск секретов",
        "cta_subject": "Source%20Audit",
        "sections": [
            {"h2_en": "Why Hardcoded Secrets Are So Dangerous", "h2_ru": "Почему захардкоженные секреты так опасны",
             "paras": [
                ("A hardcoded credential needs no vulnerability to exploit — the attacker just logs in. It is the one finding that skips the entire kill chain and drops straight into an authenticated session: a production lobby with a demo admin, a bundle with a decryptable AES key, a config with a database password.",
                 "Захардкоженный кред не нуждается в уязвимости — злоумышленник просто заходит. Это находка, которая пропускает всю цепочку атаки и сразу даёт авторизованную сессию: прод-лобби с демо-админом, бандл с расшифровываемым AES-ключом, конфиг с паролем от базы."),
                ("We have found a live casino lobby opened by a demo login with a seven-figure test balance — the kind of thing that takes one leaked string to turn into a headline.",
                 "Мы находили живое лобби казино, открывающееся демо-логином с семизначным тестовым балансом — та вещь, которой достаточно одной утёкшей строки, чтобы стать заголовком."),
             ],
             "list": [
                ("Demo and default logins left enabled in production", "Демо-логины и логины по умолчанию остались в проде"),
                ("API keys and tokens in client bundles and apps", "API-ключи и токены в клиентских бандлах и приложениях"),
                ("Database and service passwords in configs and env files", "Пароли баз и сервисов в конфигах и env-файлах"),
                ("Encryption keys that ship inside the app they protect", "Ключи шифрования, поставляемые внутри приложения, которое защищают"),
             ]},
            {"h2_en": "Why Reviews Miss Them", "h2_ru": "Почему ревью их пропускает",
             "paras": [
                ("Secrets hide in git history, in minified bundles, in an old config nobody reads. A grep for 'password' finds the obvious ones; the real ones are obfuscated, split across files, or tucked into a binary you never decompile.",
                 "Секреты прячутся в истории git, в минифицированных бандлах, в старом конфиге, который никто не читает. Grep по слову «password» находит очевидное; настоящие обфусцированы, разбиты по файлам или зашиты в бинарник, который вы никогда не декомпилируете."),
             ]},
            {"h2_en": "How We Hunt Them", "h2_ru": "Как мы их ищем",
             "list": [
                ("Scan source, configs, git history and CI artifacts", "Сканируем исходники, конфиги, историю git и артефакты CI"),
                ("Decompile mobile apps and client bundles", "Декомпилируем мобильные приложения и клиентские бандлы"),
                ("Verify each secret against the live system", "Проверяем каждый секрет на живой системе"),
                ("Map what each leaked credential actually unlocks", "Картируем, что реально открывает каждый утёкший кред"),
             ],
             "mark": "1",
             "outcome": ("Every hardcoded secret found, verified and rotated — with a process so they never ship again.",
                         "Каждый захардкоженный секрет найден, проверен и ротирован — с процессом, чтобы они больше не попадали в релиз.")},
        ],
        "faq": [
            ("Do you scan or actually verify the secrets?", "Вы сканируете или реально проверяете секреты?",
             "Both. We scan the full surface, then verify each candidate against the live system so the report contains only working credentials, not noise.",
             "И то и другое. Сканируем всю поверхность, затем проверяем каждый кандидат на живой системе — в отчёте только рабочие креды, без шума."),
            ("Will you see our production secrets?", "Вы увидите наши прод-секреты?",
             "Only the ones you authorise us to assess, under NDA. Findings are reported as what was exposed, with rotation steps — never stored beyond the report.",
             "Только те, что вы разрешили проверять, под NDA. В отчёте — что было раскрыто и шаги ротации, без хранения за пределами отчёта."),
        ],
    },
    {
        "slug": "idor-account-takeover",
        "title_en": "IDOR — The Object Reference That Gives Away Accounts — OwlMind Security",
        "title_ru": "IDOR — ссылка на объект, отдающая чужие аккаунты — OwlMind Security",
        "desc_en": "How a predictable object ID lets one user read another's data, why IDOR is the most common access-control miss, and how to test it properly.",
        "desc_ru": "Как предсказуемый идентификатор объекта даёт одному пользователю читать данные другого, почему IDOR — самая частая ошибка контроля доступа и как её правильно тестировать.",
        "og_desc": "How a predictable object ID lets one user read another's data.",
        "bc_en": "IDOR", "bc_ru": "IDOR",
        "h1_en": "IDOR and Account Takeover", "h1_ru": "IDOR и перехват аккаунта",
        "hero_en": "Change the id in the URL, keep the same session — and the API hands over someone else's account. IDOR is small to exploit and devastating in impact.",
        "hero_ru": "Меняешь id в адресе, оставляешь ту же сессию — и API отдаёт чужой аккаунт. IDOR прост в эксплуатации и разрушителен по последствиям.",
        "cta_en": "Find the References That Leak", "cta_ru": "Найдите ссылки, которые утекают",
        "cta_sub_en": "Send us your API scope — IDOR assessment within 48 hours.", "cta_sub_ru": "Пришлите контур API — проверка IDOR в течение 48 часов.",
        "cta_btn_en": "Request an IDOR Audit", "cta_btn_ru": "Заказать проверку IDOR",
        "cta_subject": "IDOR%20Audit",
        "sections": [
            {"h2_en": "What IDOR Actually Is", "h2_ru": "Что такое IDOR на самом деле",
             "paras": [
                ("IDOR — insecure direct object reference — is the app trusting the identifier but not checking who is asking. You change /statement/12345 to /statement/12346, and if the server only checks that you are logged in, not that 12346 belongs to you, it returns a stranger's statement, card or passport scan.",
                 "IDOR — это когда приложение доверяет идентификатору, но не проверяет, кто спрашивает. Меняешь /statement/12345 на /statement/12346, и если сервер проверяет только факт входа, а не принадлежность 12346 тебе, — получаешь чужую выписку, карту или скан паспорта."),
                ("It is the most common access-control miss because it survives frameworks: the route is wired, the auth middleware runs, and only the object-level check is missing.",
                 "Это самая частая ошибка контроля доступа, потому что переживает фреймворки: маршрут есть, middleware авторизации срабатывает, не хватает только проверки на уровне объекта."),
             ],
             "list": [
                ("Object ids are predictable and sequential", "Идентификаторы объектов предсказуемы и последовательны"),
                ("Auth checks 'logged in' but not 'owns this object'", "Проверка «вошёл ли», но не «владеет ли этим объектом»"),
                ("Works across users, roles, and tenants", "Работает между пользователями, ролями и арендаторами"),
                ("Impacts statements, cards, KYC and admin actions", "Бьёт по выпискам, картам, KYC и админ-действиям"),
             ]},
            {"h2_en": "From IDOR to Full Account Takeover", "h2_ru": "От IDOR до полного захвата аккаунта",
             "paras": [
                ("A single IDOR on account statements is a data leak. The same pattern on a password-reset or email-change endpoint is full takeover: read the token, or set the contact details, and the account is yours. The fix is the same — the impact is not.",
                 "Один IDOR на выписках — это утечка данных. Тот же паттерн на сбросе пароля или смене почты — полный захват: прочитал токен или поменял контакт — аккаунт твой. Исправление одно, а последствия разные."),
             ]},
            {"h2_en": "How We Test It", "h2_ru": "Как мы это тестируем",
             "list": [
                ("Map every endpoint that takes an object reference", "Картируем каждый эндпоинт с идентификатором объекта"),
                ("Test with two accounts and every role boundary", "Тестируем двумя аккаунтами и на каждой границе ролей"),
                ("Check horizontal and vertical access, not just one", "Проверяем горизонтальный и вертикальный доступ"),
                ("Prove each leak with a real request and negative control", "Доказываем каждую утечку реальным запросом и отрицательным контролем"),
             ],
             "mark": "1",
             "outcome": ("Object-level authorization enforced everywhere — one user's data stays one user's data.",
                         "Проверка прав на уровне объекта везде — данные одного пользователя остаются только его.")},
        ],
        "faq": [
            ("Is IDOR the same as broken access control?", "IDOR — это то же, что сломанный контроль доступа?",
             "IDOR is one specific, common form of it: the object reference is trusted while the ownership check is missing.",
             "IDOR — это одна конкретная и частая его форма: идентификатору доверяют, а проверку владения пропустили."),
            ("Do you need two real accounts to test it?", "Нужны ли два реальных аккаунта для проверки?",
             "Yes — we test across real or isolated accounts to show exactly what one user can see of another.",
             "Да — проверяем на реальных или изолированных аккаунтах, чтобы показать, что именно один пользователь видит у другого."),
        ],
    },
    {
        "slug": "otp-2fa-bypass",
        "title_en": "OTP and 2FA Bypass — When the Second Factor Is Just Decoration — OwlMind Security",
        "title_ru": "Обход OTP и 2FA — когда второй фактор просто декорация — OwlMind Security",
        "desc_en": "How one-time codes get bypassed: reuse, missing rate limits, race on verification, and fallback paths that skip 2FA entirely.",
        "desc_ru": "Как обходят одноразовые коды: повторное использование, нет лимита попыток, гонка на проверке и запасные пути, которые вовсе пропускают 2FA.",
        "og_desc": "How OTP codes get bypassed — reuse, rate limits, races and fallback paths.",
        "bc_en": "OTP and 2FA Bypass", "bc_ru": "Обход OTP и 2FA",
        "h1_en": "OTP and 2FA Bypass", "h1_ru": "Обход OTP и 2FA",
        "hero_en": "The second factor only protects you if the code is single-use, rate-limited and non-negotiable. Break one assumption and the account is wide open.",
        "hero_ru": "Второй фактор защищает, только если код одноразовый, ограничен по попыткам и не обходится. Сломай одно допущение — и аккаунт открыт.",
        "cta_en": "Test the Second Factor Properly", "cta_ru": "Проверьте второй фактор как следует",
        "cta_sub_en": "Send us your auth flow — 2FA bypass assessment within 48 hours.", "cta_sub_ru": "Пришлите контур входа — проверка обхода 2FA за 48 часов.",
        "cta_btn_en": "Request a 2FA Audit", "cta_btn_ru": "Заказать аудит 2FA",
        "cta_subject": "2FA%20Audit",
        "sections": [
            {"h2_en": "The Ways a Code Gets Bypassed", "h2_ru": "Способы обхода кода",
             "paras": [
                ("The code is not single-use and can be replayed. The verify endpoint has no rate limit, so it is brute-forced. Verification races with resend, so one code is reused across attempts. Or a fallback path — an API version, a legacy login, a support reset — skips the code entirely.",
                 "Код не одноразовый, и его можно повторить. На проверке нет лимита, и её перебирают. Проверка гоняется с повторной отправкой, и один код используется на несколько попыток. Или запасной путь — старая версия API, устаревший вход, сброс через поддержку — вовсе пропускает код."),
                ("Two-factor is a chain, and the attacker only needs the weakest link. The link is almost never the crypto — it is the resend, the retry counter, or the fallback.",
                 "Двухфакторка — это цепочка, и атакующему нужен только слабейший узел. Этот узел почти никогда не криптография — это повторная отправка, счётчик попыток или запасной путь."),
             ],
             "list": [
                ("Codes reusable after a successful or failed login", "Коды пригодны повторно после успешного или неудачного входа"),
                ("No rate limit or lockout on the verify endpoint", "Нет лимита и блокировки на проверке"),
                ("Race between resend and verify reuses one code", "Гонка между повторной отправкой и проверкой использует один код"),
                ("Legacy or fallback login skips the code entirely", "Устаревший или запасной вход пропускает код целиком"),
             ]},
            {"h2_en": "Why This Matters for Banks and Exchanges", "h2_ru": "Почему это важно для банков и бирж",
             "paras": [
                ("OTP is often the last gate before money moves: a transfer, a withdrawal, a card confirmation. If the code is bypassable, the attacker is not reading data — they are moving funds. That turns a convenience flaw into a financial one.",
                 "OTP — часто последние ворота перед движением денег: перевод, вывод, подтверждение карты. Если код обходится, атакующий не читает данные — он двигает средства. Это превращает бытовую дыру в финансовую."),
             ]},
            {"h2_en": "How We Test It", "h2_ru": "Как мы это проверяем",
             "list": [
                ("Map every step that mints or verifies a code", "Картируем каждый шаг, где код создаётся или проверяется"),
                ("Test reuse, rate limits, resend races and fallbacks", "Проверяем повтор, лимиты, гонки отправки и запасные пути"),
                ("Confirm the code is single-use and time-boxed", "Подтверждаем, что код одноразовый и ограничен по времени"),
                ("Show a working bypass with a negative control", "Показываем рабочий обход с отрицательным контролем"),
             ],
             "mark": "1",
             "outcome": ("A second factor that actually requires a second factor — on every path, with no fallback that skips it.",
                         "Второй фактор, который реально требует второй фактор — на каждом пути, без запасных ходов мимо.")},
        ],
        "faq": [
            ("Is SMS OTP weaker than an app code?", "SMS-код слабее кода из приложения?",
             "It can be — SIM swap and SMS interception add risk. The bigger issue is almost always the verification logic, not the channel.",
             "Может быть — подмена SIM и перехват SMS добавляют риск. Но главная проблема почти всегда в логике проверки, а не в канале."),
            ("Do you test against live accounts?", "Вы тестируете на живых аккаунтах?",
             "On isolated accounts and agreed test numbers only — never against real customer accounts.",
             "Только на изолированных аккаунтах и согласованных тестовых номерах — никогда против реальных клиентов."),
        ],
    },
    {
        "slug": "smart-contract-reentrancy",
        "title_en": "Reentrancy in Smart Contracts — The Bug That Drains a Pool — OwlMind Security",
        "title_ru": "Реентранси в смарт-контрактах — баг, который опустошает пул — OwlMind Security",
        "desc_en": "How reentrancy lets a contract drain a pool, the fix that prevents it, and what a real smart-contract audit covers beyond the obvious.",
        "desc_ru": "Как реентранси позволяет контракту опустошить пул, исправление, которое это предотвращает, и что реально покрывает аудит смарт-контракта.",
        "og_desc": "How reentrancy drains a pool — and the fix that prevents it.",
        "bc_en": "Smart Contract Reentrancy", "bc_ru": "Реентранси в смарт-контрактах",
        "h1_en": "Reentrancy in Smart Contracts", "h1_ru": "Реентранси в смарт-контрактах",
        "hero_en": "A contract sends funds, then updates its balance. Between those two steps, the attacker calls back in — and withdraws again. That is reentrancy.",
        "hero_ru": "Контракт отправляет средства, затем обновляет баланс. Между этими шагами атакующий вызывает его снова — и выводит ещё раз. Это реентранси.",
        "cta_en": "Audit Your Contract Before It Ships", "cta_ru": "Проверьте контракт до релиза",
        "cta_sub_en": "Send us your contract — audit proposal within 48 hours.", "cta_sub_ru": "Пришлите контракт — предложение по аудиту за 48 часов.",
        "cta_btn_en": "Request a Smart Contract Audit", "cta_btn_ru": "Заказать аудит смарт-контракта",
        "cta_subject": "Smart%20Contract%20Audit",
        "sections": [
            {"h2_en": "How Reentrancy Works", "h2_ru": "Как работает реентранси",
             "paras": [
                ("Reentrancy happens when a contract makes an external call before updating its own state. The called contract — which the attacker controls — calls back into the original function while the balance still shows the old value. The withdraw runs twice on one balance.",
                 "Реентранси возникает, когда контракт делает внешний вызов до обновления своего состояния. Вызываемый контракт — который контролирует атакующий — зовёт исходную функцию снова, пока баланс всё ещё показывает старое значение. Вывод срабатывает дважды на один баланс."),
                ("The classic case is a pool or vault with a naive withdraw. It is the bug behind several famous nine-figure exploits, and it is still shipped because the pattern looks correct on first read.",
                 "Классика — пул или хранилище с наивным выводом. Это баг, стоящий за несколькими известными девятизначными взломами, и его до сих пор релизят, потому что на первый взгляд паттерн выглядит правильным."),
             ],
             "list": [
                ("External call made before state is updated", "Внешний вызов сделан до обновления состояния"),
                ("Attacker contract re-enters during the call", "Контракт атакующего повторно входит во время вызова"),
                ("Balance or allowance read from stale state", "Баланс или лимит читаются из устаревшего состояния"),
                ("Funds drained repeatedly in one transaction", "Средства выводятся многократно в одной транзакции"),
             ]},
            {"h2_en": "The Fix", "h2_ru": "Исправление",
             "paras": [
                ("Update state before any external call, or guard the entry with a reentrancy lock, or use the checks-effects-interactions pattern. The key is one rule: internal state must be consistent before you hand control to an untrusted address.",
                 "Обновляйте состояние до внешнего вызова, защищайте вход замком реентранси или используйте паттерн «проверки — эффекты — взаимодействия». Правило одно: внутреннее состояние должно быть согласовано до передачи контроля недоверенному адресу."),
             ]},
            {"h2_en": "What an Audit Actually Covers", "h2_ru": "Что реально покрывает аудит",
             "list": [
                ("Reentrancy, overflow/underflow, access control", "Реентранси, переполнение, контроль доступа"),
                ("Oracle and price manipulation", "Манипуляции оракулом и ценой"),
                ("Upgradeable-proxy and admin-key risks", "Риски обновляемых прокси и админ-ключей"),
                ("Signature replay, flash-loan and cross-chain vectors", "Повтор подписи, флеш-займы и межсетевые векторы"),
             ],
             "mark": "1",
             "outcome": ("A technical report with a working proof-of-concept for every critical finding and a code-level fix — the evidence investors and listing partners ask for.",
                         "Технический отчёт с рабочим доказательством каждой критической находки и исправлением на уровне кода — то, что просят инвесторы и биржи листинга.")},
        ],
        "faq": [
            ("How long does a smart contract audit take?", "Сколько длится аудит смарт-контракта?",
             "One to two weeks for a single contract, three to five for a full protocol with tests and a re-audit of fixes.",
             "Одна-две недели на один контракт, три-пять на полный протокол с тестами и перепроверкой исправлений."),
            ("Do you re-audit after fixes?", "Вы перепроверяете после исправлений?",
             "Yes — every audit includes 30 days of support and a free re-scan of fixed items.",
             "Да — каждый аудит включает 30 дней поддержки и бесплатную перепроверку закрытого."),
        ],
    },
    {
        "slug": "cors-financial-api",
        "title_en": "CORS Misconfiguration on Financial APIs — Cross-Origin Reads of User Data — OwlMind Security",
        "title_ru": "CORS на финансовых API — чтение пользовательских данных из чужого источника — OwlMind Security",
        "desc_en": "How a permissive CORS policy lets any site read a user's financial data, and how to distinguish the real risk from harmless misconfiguration.",
        "desc_ru": "Как излишне доверчивый CORS позволяет любому сайту читать финансовые данные пользователя и как отличить реальный риск от безобидной ошибки.",
        "og_desc": "How a permissive CORS policy lets any site read a user's financial data.",
        "bc_en": "CORS on Financial APIs", "bc_ru": "CORS на финансовых API",
        "h1_en": "CORS Misconfiguration on Financial APIs", "h1_ru": "CORS на финансовых API",
        "hero_en": "If the server reflects any origin and sends credentials, any website a user visits can read their balance and transactions. That is the CORS risk.",
        "hero_ru": "Если сервер отражает любой источник и шлёт куки, любой сайт, который посетит пользователь, прочитает его баланс и транзакции. Это риск CORS.",
        "cta_en": "Tighten Your Cross-Origin Policy", "cta_ru": "Ужесточите политику источников",
        "cta_sub_en": "Send us your API scope — CORS assessment within 48 hours.", "cta_sub_ru": "Пришлите контур API — проверка CORS за 48 часов.",
        "cta_btn_en": "Request a CORS Audit", "cta_btn_ru": "Заказать проверку CORS",
        "cta_subject": "CORS%20Audit",
        "sections": [
            {"h2_en": "When CORS Becomes a Breach", "h2_ru": "Когда CORS становится взломом",
             "paras": [
                ("CORS is only dangerous when three things align: the server reflects the attacker's origin, it sends credentials with the response, and the endpoint returns user data. Then any page the user opens can read their authenticated data across origins.",
                 "CORS опасен только когда сходится три вещи: сервер отражает источник атакующего, шлёт куки с ответом, а эндпоинт отдаёт пользовательские данные. Тогда любая открытая пользователем страница читает его авторизованные данные из чужого источника."),
                ("A wildcard without credentials is usually harmless. A reflected origin with credentials on a balance endpoint is a silent data thief. The difference matters, and scanners get it wrong in both directions.",
                 "Звёздочка без кук обычно безобидна. Отражённый источник с куками на эндпоинте баланса — тихий вор данных. Разница важна, и сканеры ошибаются в обе стороны."),
             ],
             "list": [
                ("Origin reflected instead of allow-listed", "Источник отражается вместо белого списка"),
                ("Credentials sent with the cross-origin response", "Куки отправляются с кросс-доменным ответом"),
                ("Endpoint returns balances, statements or PII", "Эндпоинт отдаёт балансы, выписки или личные данные"),
                ("Wildcard with credentials, or null origin accepted", "Звёздочка с куками или принятый пустой источник"),
             ]},
            {"h2_en": "Why the Fix Is a Policy, Not a Line", "h2_ru": "Почему исправление — это политика, а не строка",
             "paras": [
                ("The fix is an allow-list of the exact origins that need access, credentials only where required, and no reflection. But the hard part is knowing every origin that legitimately calls the API — which is exactly the map an assessment produces.",
                 "Исправление — белый список точных источников, куки только где нужно и никакого отражения. Но сложность в том, чтобы знать каждый источник, который легитимно зовёт API, — именно такую карту и даёт оценка."),
             ]},
            {"h2_en": "How We Verify It", "h2_ru": "Как мы это проверяем",
             "list": [
                ("Probe every data endpoint with attacker origins", "Проверяем каждый эндпоинт с источниками атакующего"),
                ("Confirm credentials are actually sent", "Подтверждаем, что куки реально отправляются"),
                ("Show a real cross-origin read with a negative control", "Показываем реальное кросс-доменное чтение с отрицательным контролем"),
                ("Distinguish true risk from benign wildcard", "Отличаем настоящий риск от безобидной звёздочки"),
             ],
             "mark": "1",
             "outcome": ("A CORS policy that allows exactly the origins you trust — and proof no other site can read your users' data.",
                         "Политика CORS, допускающая только доверенные источники, — и доказательство, что чужой сайт не прочитает данные ваших пользователей.")},
        ],
        "faq": [
            ("Is every CORS finding a vulnerability?", "Каждая ли находка CORS — уязвимость?",
             "No. Many are benign. We verify each one against a real cross-origin request and report only what actually leaks data.",
             "Нет, многие безобидны. Проверяем каждую реальным кросс-доменным запросом и отчитываемся только о том, что реально утекает."),
            ("Do you need a browser to prove it?", "Нужен ли браузер для доказательства?",
             "A crafted page in a browser is the cleanest proof, so yes — we demonstrate the read exactly as an attacker's site would.",
             "Страница в браузере — самое чистое доказательство, поэтому да — показываем чтение ровно так, как сделал бы сайт атакующего."),
        ],
    },
]


def main():
    made = 0
    for a in ARTICLES:
        dst_dir = os.path.join(ROOT, "blog", a["slug"])
        os.makedirs(dst_dir, exist_ok=True)
        html = render_article(a)
        with open(os.path.join(dst_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(html)
        print("OK  ", a["slug"])
        made += 1
    print(f"\nГотово статей: {made}")


if __name__ == "__main__":
    main()
