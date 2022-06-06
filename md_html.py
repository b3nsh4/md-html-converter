#!/usr/bin/env python3
import argparse
import os
import re
import markdown

preamble = """\
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{title}</title>
<style>
{css}
</style>
</head>
<body>
<div id="resume">
"""

postamble = """\
</div>
</body>
</html>
"""



def title(md: str) -> str:
    """
    Return the contents of the first markdown heading in md, which we
    assume to be the title of the document.
    """
    for line in md.splitlines():
        if re.match("^#[^#]", line):  # starts with exactly one '#'
            return line.lstrip("#").strip()
    raise ValueError(
        "Cannot find any lines that look like markdown h1 headings to use as the title"
    )


def make_html(md: str, prefix: str = "resume") -> str:
    """
    Compile md to HTML and prepend/append preamble/postamble.

    Insert <prefix>.css if it exists.
    """
    try:
        with open("style.css") as cssfp:
            css = cssfp.read()
    except FileNotFoundError:
        print("style.css not found. Output will by UNSTYLED!.")
        css = ""
    return "".join(
        (
            preamble.format(title=title(md), css=css),
            markdown.markdown(md, extensions=["smarty"]),
            postamble,
        )
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "file",
        help="markdown input file [FILE.md]",
    )

    args = parser.parse_args()

    prefix, _ = os.path.splitext(os.path.abspath(args.file))

    with open(args.file, encoding="utf-8") as mdfp:
        md = mdfp.read()
    html = make_html(md, prefix=prefix)

    with open(prefix + ".html", "w", encoding="utf-8") as htmlfp:
        htmlfp.write(html)
        print(f"Wrote {htmlfp.name}")

