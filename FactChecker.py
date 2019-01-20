import wikipedia


class FactCheck:

    def __init__(self):
        self.entity = None
        self.wiki_search = None

    def isFact(self, entity):
        entity = []
        if entity:
            count_dict = {}
            entityList = []
            combining_ner = None
            for e in entity:
                ent = e[0]
                entityList.append(ent.encode(encoding="latin-1"))
            for e in entityList:
                wikiPage = e
                try:
                    page = wikipedia.page(wikiPage)
                    text = page.content.encode(encoding='UTF-8', errors='strict')

                    for term in entityList:
                        if term != "":
                            count = text.count(term)
                            # if count > 0:
                            count_dict[term] = count

                except Exception as e:
                    print "error: ", e
                    return False
            print "count_dict: ", count_dict
        return False

# statement = ""
# wikiPage = unicode("P\xe4r Lagerkvist", 'latin-1')
# page = wikipedia.page(wikiPage)
#
# termsList = ["P\xe4r Lagerkvist", "Nobel Prize", "Physics"]
# # text = unicodedata.normalize('NFKD', page.content).encode('ascii','ignore')
# text = page.content.encode(encoding='UTF-8',errors='strict')
#
# def get_term_count(list):
#     count_dict = {}
#
#     for term in list:
#         if term != "":
#             count = text.count(term)
#             # if count > 0:
#             count_dict[term] = count
#     return count_dict
#
#
# dic = get_term_count(termsList)
#
# print dic



