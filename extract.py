import requests
import codecs

print("#"*5 + " XML")
resp = requests.post('https://europass.cedefop.europa.eu/rest/v1/document/extraction',
                     headers={ "Content-Type": "application/pdf"},
                     data= open("cv.pdf", "rb")
                     )

print resp
print resp.text
with codecs.open("cv.xml", "w", encoding="utf-8") as f:
    f.write(resp.text)
    print("### File written")

print("#"*5 + " JSON")
resp = requests.post('https://europass.cedefop.europa.eu/rest/v1/document/to/json',
                     headers={ "Content-Type": "application/xml"},
                     data= open("cv.xml", "rb")
                     )

print resp
print resp.text
with codecs.open("cv.json", "w", encoding="utf-8") as f:
    f.write(resp.text)
    print("### File written")
