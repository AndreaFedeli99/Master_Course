import re

HEADER_PATTERN = r'^(#{1,6})\s+(.+)$'
BR_PATTERN = r'^-{3}$'
PARAGRAPH_PATTERN = r'(^[^<\s](.+))'

ORDERED_LIST_PATTERN = r'(^\s*[123456789]+.\s+(.*)\n)+'
ORDERED_LIST_ITEM = r'(^\s*\d.\s+(.*))+'

UNORDERED_LIST_PATTERN = r'(^\s*\*\s+(.*)\n)+'
UNORDERED_LIST_ITEM = r'(^\s*\*\s+(.*))+'

ITALIC_PATTERN = r'_(.+)_'
BOLD_PATTERN = r'\*\*(.+)\*\*'
CONSOLE_PATTERN = r'`(.+)`'

def translate_headers(p, s):
    m = p.search(s)
    while m is not None:
        added_string = f"<h{len(m.group(1))}>{m.group(2)}</h{len(m.group(1))}>"
        s = s[:m.start()] + added_string + s[m.end():]
        m = p.search(s)
    return s

def translate_br(p, s):
    return p.sub(r"</ br>", s)

def translate_unordered_list(p, s):
    m = p.search(s)
    while m is not None:
        added_string = "<ul>\n" + m.group()[:-1] + "\n</ul>\n"
        added_string = re.sub(UNORDERED_LIST_ITEM, r"\t<li>\2</li>", added_string, flags=re.MULTILINE)
        s = s[:m.start()] + added_string + s[m.end():]
        m = p.search(s)
    return s

def translate_ordered_list(p, s):
    m = p.search(s)
    while m is not None:
        added_string = "<ol>\n" + m.group()[:-1] + "\n</ol>\n"
        added_string = re.sub(ORDERED_LIST_ITEM, r"\t<li>\2</li>", added_string, flags=re.MULTILINE)
        s = s[:m.start()] + added_string + s[m.end():]
        m = p.search(s)
    return s

def translate_italic(p, s):
    return p.sub(r"<em>\1</em>", s)

def translate_bold(p, s):
    return p.sub(r"<strong>\1</strong>", s)

def translate_console(p, s):
    return p.sub(r"<code>\1</code>", s)

patterns = {
    HEADER_PATTERN: translate_headers,
    BR_PATTERN: translate_br,
    UNORDERED_LIST_PATTERN: translate_unordered_list,
    ORDERED_LIST_PATTERN: translate_ordered_list,
    ITALIC_PATTERN: translate_italic,
    BOLD_PATTERN: translate_bold,
    CONSOLE_PATTERN: translate_console
}

def translate(fn):
    html_string = ""
    with open(fn) as f:
        html_string = f.read()
    for p,t in patterns.items():
        pattern = re.compile(p, re.MULTILINE)
        html_string = t(pattern, html_string)
    html_string = re.sub(PARAGRAPH_PATTERN, r"<p>\1</p>", html_string, flags=re.MULTILINE)
    return f"<html>\n{html_string}\n</html>"
