import bibtexparser
from bibtexparser.customization import *
from datetime import datetime

import json


with open("resume-nobib.json") as r:
    resume = json.load(r)
    parser = bibtexparser.bparser.BibTexParser(common_strings=True,
                                               customization=convert_to_unicode)

    with open('ref.bib') as bibtex_file:
        bibtex_str = bibtex_file.read()

    bib_database = bibtexparser.loads(bibtex_str, parser=parser)
    pubs = []
    for entry in bib_database.entries:
        pub = {}
        if "booktitle" in entry:
            pub["publisher"] = journal(entry["booktitle"])
        if "year" in entry:
            reldate = datetime.strptime('{}-{}-{}'.format(entry.get('year', 2010),
                                                          entry.get('month', 'January'),
                                                          entry.get('day', 1)),
                                        '%Y-%B-%d')
            pub["releaseDate"] = reldate.strftime('%Y-%m-%d')
            print(pub['releaseDate'])
        if "author" in entry:
            pub["authors"] = author(entry["author"])
        if "abstract" in entry:
            pub["summary"] = author(entry["abstract"])
        pub["name"] = entry["title"].replace("{","").replace("}","")
        pubs.append(pub)
        resume["publications"] = sorted(pubs, key=lambda x: x["releaseDate"], reverse=True)

    with open("resume.json", "w") as out:
        json.dump(resume, out, indent=2)
