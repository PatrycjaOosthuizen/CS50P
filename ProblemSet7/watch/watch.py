import re


def main():
    print(parse(input("HTML: ")))

def parse(s):
    # Write regular expression testing iframe string :
    # <iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    # Check regular expression format match - ttps://regex101.com/
    if re.search(r"<iframe(.)*><\/iframe>", s):
        # Write regular expression testing URL strings:
        # http://youtube.com/embed/xvFZjo5PgG0
        # https://youtube.com/embed/xvFZjo5PgG0
        # https://www.youtube.com/embed/xvFZjo5PgG0
        # Check regular expression format match - ttps://regex101.com/
        url_format = re.search(r"(http(s)*:\/\/(www\.)*youtube\.com\/embed\/)([a-z_A-Z_0-9]+)", s)
        if url_format:
            # Match.groups method extract the embeded URL of YouTube video
            split_url = url_format.groups()
            # Return converted shorter version youtu.be URLs
            return "https://youtu.be/" + split_url[3]


if __name__ == "__main__":
    main()
