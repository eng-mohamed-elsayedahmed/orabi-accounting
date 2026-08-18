"""Build a single self-contained preview file from the two language pages.

The published preview has no network access, so the fonts, stylesheet and script
are all inlined, and the two language versions live in one document behind a
toggle instead of two URLs.

Usage:  python build-preview.py [path/to/fonts-inline.css]
Output: preview.html
"""

import base64
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
IDS = ["top", "companies", "individuals", "about", "media", "faq", "contact"]


def inline_images(body):
    """The preview cannot reach the filesystem, so every image travels with it."""
    def repl(m):
        name = m.group(1)
        path = os.path.join(HERE, "assets", "media", name)
        if not os.path.exists(path):
            return m.group(0)
        with open(path, "rb") as f:
            data = base64.b64encode(f.read()).decode()
        return 'src="data:image/jpeg;base64,%s"' % data
    return re.sub(r'src="(?:\.\./)?assets/media/([\w.-]+)"', repl, body)


def read(*parts):
    with open(os.path.join(HERE, *parts), encoding="utf-8") as f:
        return f.read()


def body_of(html):
    start = html.index("<body>") + len("<body>")
    end = html.index("</body>")
    body = html[start:end]
    body = re.sub(r'<script src="[^"]*app\.js"></script>', "", body)
    return body.strip()


def namespace_en(body):
    """Keep the English anchors from colliding with the Arabic ones."""
    for name in IDS:
        body = body.replace('id="%s"' % name, 'id="en-%s"' % name)
        body = body.replace('href="#%s"' % name, 'href="#en-%s"' % name)
    return body


def main():
    fonts_path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "fonts-inline.css")
    fonts = ""
    if os.path.exists(fonts_path):
        with open(fonts_path, encoding="utf-8") as f:
            fonts = f.read()
    else:
        print("note: no inlined fonts found at %s — preview will fall back to system fonts" % fonts_path)

    css = read("assets", "style.css")
    js = read("assets", "app.js")
    ar = inline_images(body_of(read("index.html")))
    en = inline_images(namespace_en(body_of(read("en", "index.html"))))

    # the language links become in-page toggles
    ar = ar.replace('href="en/"', 'href="#" data-lang="en"')
    en = en.replace('href="../"', 'href="#" data-lang="ar"')

    preview_css = """
.pv-pane[hidden]{display:none}
"""

    toggle_js = """
(function(){
  var panes = {ar: document.getElementById('pane-ar'), en: document.getElementById('pane-en')};
  function show(lang){
    panes.ar.hidden = lang !== 'ar';
    panes.en.hidden = lang !== 'en';
    document.documentElement.setAttribute('lang', lang);
    window.scrollTo(0, 0);
  }
  document.addEventListener('click', function(e){
    var t = e.target.closest ? e.target.closest('[data-lang]') : null;
    if(!t) return;
    e.preventDefault();
    show(t.getAttribute('data-lang'));
  });
})();
"""

    out = []
    out.append("<title>مجموعة عرابي المحاسبية</title>")
    out.append("<style>\n%s\n%s\n%s\n</style>" % (fonts, css, preview_css))
    out.append('<div class="pv-pane" id="pane-ar" dir="rtl" lang="ar">\n%s\n</div>' % ar)
    out.append('<div class="pv-pane" id="pane-en" dir="ltr" lang="en" hidden>\n%s\n</div>' % en)
    out.append("<script>\ndocument.documentElement.classList.add('js');\n%s\n%s\n</script>" % (js, toggle_js))

    html = "\n".join(out)
    with open(os.path.join(HERE, "preview.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("preview.html written — %d KB" % (len(html.encode("utf-8")) // 1024))


if __name__ == "__main__":
    main()
