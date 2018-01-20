from django.core.management.base import BaseCommand, CommandError
from urls_collector.models import Document
from urls_collector.models import URL
from urls_collector.models import Occurence


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):

        url1 = URL(url='https://github.com/heroku/python-getting-started')
        url1.save()

        url2 = URL(url='http://www.django-rest-framework.org')
        url2.save()

        url3 = URL(url='https://github.com/encode/rest-framework-tutorial')
        url3.save()

        url4 = URL(url='https://github.com/metachris/pdfx')
        url4.save()

        url5 = URL(url='https://www.djangoproject.com')
        url5.save()

        doc1 = Document(filename="document1.pdf")
        doc1.save()

        doc2 = Document(filename="document2.pdf")
        doc2.save()

        doc3 = Document(filename="document3.pdf")
        doc3.save()

        occurences = (
            (doc1, (url1, url2, url3)),
            (doc2, (url1, url2, url4)),
            (doc3, (url1, url5)),
        )

        for doc, urls in occurences:
            for url in urls:
                oc = Occurence(document=doc, url=url)
                oc.save()
