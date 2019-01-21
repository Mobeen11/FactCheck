import wikipedia
import unicodedata


class FactCheck:
    def __init__(self):
        self.entity = None
        self.wiki_search = None
        self.returnValue = 0

    def isFact(self, entity):
        if entity:
            # print "entity: ", entity
            for e in entity:
                page = ""
                try:
                    # print "e: ", e
                    page = wikipedia.page(e)

                except wikipedia.exceptions.DisambiguationError as e:
                    print "exception: ", e.options
                    try:
                        page = wikipedia.page(e.options[0])
                    except Exception as e:
                        return -1
                except Exception as e:
                    print "exception 2", e
                    return -1.0

                text = unicodedata.normalize('NFKD', page.content).encode('ascii', 'ignore')
                for term in entity:
                    if term != "":
                        count = text.count(term)
                        if count > 0:
                            self.returnValue += 1

            if self.returnValue > 1:
                return 1.0
        return -1


