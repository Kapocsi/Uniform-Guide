import time
import markdown


def main(lines):
    markdownText = markdown.markdown(lines, extensions=["tables", "md_in_html"])
    with open("index.html", "w+") as f:
        f.write(markdownText)


if __name__ == "__main__":
    lines,prevline = "",""
    while 1:
        lines = ""
        with open("index.md") as f:
            for line in f:
                lines = lines + line
        if lines != prevline:
            main(lines)
            prevline = lines
            print("FileUpdate")
        else:
            time.sleep(1)
