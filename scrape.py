import pywikibot as wiki
from inspect import getmembers, ismethod
site = wiki.Site()
page = wiki.Page(site, u"philosophy")

itempage = wiki.ItemPage.fromPage(page)

def wikiDocs(page):
    return "Doc for wiki".join(["Doc for {}:\n{}".format(name,func.__doc__) for name, func in getmembers(page, ismethod)])

wikidocs = wikiDocs(page)

NextLevel = [link for link in itempage.interwiki()]
