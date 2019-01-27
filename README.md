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

### Algorithm
```
1- Train NER model (factCheckerModel)
2- Get Entities from statement
3- query entities on **wikipedia**
4- if other entities found on wikipedia page
5-      **return** 1
6- else
7-      **return** -1
8- if page not found
9-      **return** 0
```

## Collaborators
**ZULFIQAR AHMED**

**MOBEEN AHMED**
## License
[MIT](https://choosealicense.com/licenses/mit/)
