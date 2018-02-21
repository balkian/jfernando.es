from python:3.5

WORKDIR /usr/src/app

ADD requirements.txt .

RUN pip install -r requirements.txt

ADD create_bibliography.py ref.bib resume-nobib.json /usr/src/app/

RUN python create_bibliography.py


from node

RUN npm install -g resume-cli jsonresume-theme-elegant

WORKDIR /usr/src/app

COPY --from=0 /usr/src/app/resume.json /usr/src/app/

RUN resume export --theme elegant --format html index.html
 
from nginx

COPY --from=1 /usr/src/app/index.html /usr/src/app/resume.json /usr/share/nginx/html/

EXPOSE 80
ADD . /usr/share/nginx/html/
