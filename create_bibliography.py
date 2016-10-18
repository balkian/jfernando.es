import bibtexparser
from bibtexparser.customization import *
import json

with open("resume-nobib.json") as r:
    resume = json.load(r)
    with open('ref.bib') as bibtex_file:
        parser = bibtexparser.bparser.BibTexParser()
        parser.customization = convert_to_unicode
        bibtex_str = bibtex_file.read()

    bib_database = bibtexparser.loads(bibtex_str)
    pubs = []
    for entry in bib_database.entries:
        pub = {}
        if "booktitle" in entry:
            pub["publisher"] = journal(entry["booktitle"])
        if "year" in entry:
            pub["releaseDate"] = entry["year"]
        if "author" in entry:
            pub["authors"] = author(entry["author"])
        if "abstract" in entry:
            pub["summary"] = author(entry["abstract"])
        pub["name"] = entry["title"].replace("{","").replace("}","")
        pubs.append(pub)
        resume["publications"] = sorted(pubs, key=lambda x: x["releaseDate"], reverse=True)

    with open("resume.json", "w") as out:
        json.dump(resume, out, indent=2)
