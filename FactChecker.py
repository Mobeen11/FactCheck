import wikipedia
import unicodedata


class FactCheck:
    def __init__(self):
        self.entity = None
        self.wiki_search = None
        self.returnValue = 0

    def isFact(self, entity):
        if entity:
            # for ent in entity:
            ent = entity[0]
            # print "ent: ", ent
            page = ""
            try:
                page = wikipedia.page(ent)
            except Exception as ex:
                # print "exception: ", ex
                return -1.0

            text = unicodedata.normalize('NFKD', page.content).encode('ascii', 'ignore')
            for term in entity:
                if term != "":
                    if term in text:
                        self.returnValue += 1

            if self.returnValue >= 1:
                return 1.0
        return -1.0


