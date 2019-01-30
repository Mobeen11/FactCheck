# Fact-Checking Engine

Fact Checking engine returns a value between +1 and -1 given a fact from DBpedia.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required packages used in project.
python 2.x
```bash
pip install -r requirements.txt 
```
python 3.x
```bash
pip3 install -r requirements.txt 
```
After the requirements are installed add the .tsv file path and run the main and result.ttl will be created in existing directory.
```python
    fact.ReadFile("test.tsv")
```

## Approach 
![Approach](https://res.cloudinary.com/dymq10xxe/image/upload/v1548608998/approach.png)
 
**FactChecker Model:** Extract the Name Entity Recognition from the input statements. 

**Query Wikipedia:** Once the NER is determined query the wikipedia to check its true value.

## Description

In FactChecker first NER model is created using spacy (Open source NLP package). Then it is trained using train.tsv for the extraction of SUB/OBJ/PRE from the input statments. Once SUB and OBJ are extracted these entities are searched on the wikipedia and returns the factValue.

## Non-Working facts

**False Positive**
```
1- George Bernard Shaw born in Liverpool. 	-1
2- Palo Alto is Siebel Systems' innovation place. 	-1  
3- Netherlands is Wim Kok's role.	-1
4- Star Trek Into Darkness directed by Chris Pine.  	-1
5- Compton, California nascence place of Dr. Dre.   -1
```
**False Negative**
```
1- Beck's birth place is Königsberg.   1
2- Vernor Vinge is A Deepness in the Sky's generator.  1
3- Pano Logic founded in California United States.     1
4- Doris Lessing won Nobel in Literature.  1
5- Adore(film) is adapted from The Grandmothers.   1
```
### Algorithm
```
1- Train NER model (factCheckerModel)
2- Get Entities from statement
3- query entities on wikipedia
4- if other entities found on wikipedia page
5-      return 1
6- else
7-      return -1
```

## Team: Void 2.0
Zulfiqar Ahmed

Mobeen Ahmed
