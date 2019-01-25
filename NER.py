from nltk import ne_chunk, pos_tag, word_tokenize
from FactChecker import FactCheck
from nltk.corpus import stopwords
from nltk.tree import Tree
import csv, spacy, re


class NERCreator:
    def __init__(self):
        self.training_facts = []
        self.NERFactEntities = []
        # self.wikipedia_model = spacy.load('xx_ent_wiki_sm')
        self.wikipedia_model = spacy.load('./factCheckerModel')
        self.stop_words = set(stopwords.words("english"))

    def ReadFile(self, filename):
        with open(filename) as trainingFile:
            for row in csv.DictReader(trainingFile, delimiter='\t'):
                self.training_facts.append(row)

    def CreateNER(self):
        # print "traiing: ", self.training_facts
        for fact in self.training_facts:
            fact_id = fact['FactID']
            fact_statement = unicode(fact['Fact_Statement'], encoding="latin-1")
            text = fact_statement

            doc = self.wikipedia_model(text)
            ents = [e.text for e in doc.ents]
            fact['NER'] = ents
            fact['value'] = FactCheck().isFact(entity=fact['NER'])
            # fact['value'] = FactCheck().isFact(entity=fact['NER'])
            self.WriteFile(fact['FactID'], fact['value'])
        # print "fact: ", FactCheck().isFact(entity=[u'David Lee', u'Memphis Grizzlies'])

    def WriteFile(self, factID, prob):
        fact_URI = "<http://swc2017.aksw.org/task2/dataset/"
        prop_URI = "<http://swc2017.aksw.org/hasTruthValue> "
        value = "^^<http://www.w3.org/2001/XMLSchema#double> ."
        with open("result.ttl", 'a') as resultFile:
                resultFile.write(fact_URI + str(factID) + "> " + prop_URI + "\"" +str(prob) + "\"" + value)
                resultFile.write("\n")

