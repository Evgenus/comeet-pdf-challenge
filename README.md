# Home Assignment on PDF Crawler

[![Heroku](https://heroku-badge.herokuapp.com/?app=comeet-challenge-pdf-crawler)](https://comeet-challenge-pdf-crawler.herokuapp.com)

[Description](https://docs.google.com/document/d/1oWsx9TyKDiM7swrDTS7G-ymfZilgN35rI4NNFHabxvI/edit?usp=sharing)

I assume that uploaded files are rather small and internet is fast, otherwise
tasks of checking urls alive and parsing pdf documents should be handled by
standalone workers processing some queues and don't deffer response.

The requested form with ability to upload files is just at the bottom of documents 
list page then accessing service via web browser.

## What it is made of?


### PDFx

https://stackoverflow.com/questions/31436357/how-to-extract-all-links-from-pdf-file

https://www.metachris.com/pdfx/

https://github.com/metachris/pdfx


### Django deployment pattern for Heroku

https://github.com/heroku/python-getting-started


### Django Rest Framework

https://github.com/encode/rest-framework-tutorial


### drf-nested-routers

https://github.com/alanjds/drf-nested-routers


### requests

http://docs.python-requests.org/

### factory-boy

https://github.com/FactoryBoy/factory_boy

