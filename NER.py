from nltk import ne_chunk, pos_tag, word_tokenize
from FactChecker import FactCheck
from nltk.corpus import stopwords
from nltk.tree import Tree
import csv, spacy, re


class NERCreator:
    def __init__(self):
        self.training_facts = []
        self.NERFactEntities = []
        self.wikipedia_model = spacy.load('xx_ent_wiki_sm')
        self.stop_words = set(stopwords.words("english"))

    def ReadFile(self, filename):
        with open(filename) as trainingFile:
            for row in csv.DictReader(trainingFile, delimiter='\t'):
                self.training_facts.append(row)
                # print "row: ", row

    # def CreateNER(self):
    #     for fact in self.training_facts:
    #         fact_id = fact['FactID']
    #         fact_statement = fact['Fact_Statement']
    #         text = self.wikipedia_model(unicode(fact_statement, encoding="latin-1"))
    #
    #         self.NERFactEntities = [(token.text, token.label_) for token in text.ents]
    #         print "entity: ", self.NERFactEntities
    #         FactCheck().isFact(entity=self.NERFactEntities)

    def CreateNER(self):
        for fact in self.training_facts:
            fact_id = fact['FactID']
            fact_statement = unicode(fact['Fact_Statement'], encoding="latin-1")
            # text = " ".join(re.findall(r"[a-zA-Z0-9]+", fact_statement))
            text = fact_statement
            tokenized_word = word_tokenize(text)
            filtered_sent = ""
            for w in tokenized_word:
                if w not in self.stop_words:
                    filtered_sent += " " + w
            print("Filterd Sentence:", filtered_sent)
            print ("get_continuous_chunks: ", self.get_continuous_chunks(filtered_sent))

            FactCheck().isFact(entity=self.NERFactEntities)

    def get_continuous_chunks(self, text):
        chunked = ne_chunk(pos_tag(word_tokenize(text)))
        continuous_chunk = []
        current_chunk = []
        for i in chunked:
            if type(i) == Tree:
                current_chunk.append(" ".join([token for token, pos in i.leaves()]))
            elif current_chunk:
                named_entity = " ".join(current_chunk)
                if named_entity not in continuous_chunk:
                    continuous_chunk.append(named_entity)
                    current_chunk = []
            else:
                continue
        return continuous_chunk

    def WriteFile(self):
        fact_URI = "<http://swc2017.aksw.org/task2/dataset/"
        prop_URI = "<http://swc2017.aksw.org/hasTruthValue"
        value = "^^<http://www.w3.org/2001/XMLSchema#double>"
        with open("result.ttl", 'a') as resultFile:
            for facts in self.training_facts:
                resultFile.write(fact_URI + str(facts['FactID']) + "> " + prop_URI + ".\"" + str(facts['value']) + "\"" + value)
                resultFile.write("\n")

