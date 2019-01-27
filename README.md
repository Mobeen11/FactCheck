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
## Approach Description
![Approach](https://res.cloudinary.com/dymq10xxe/image/upload/v1548608998/approach.png)

**FactChecker Model:** Extract the Name Entity Recognition from the input statements. The model was built using python NLP package "Spacy".

**Query Wikipedia:** Once the NER is determined query the wikipedia to check its true value.

### Algorithm
```
1- Get Entities from statement
2- query entities on **wikipedia**
3- if other entities found on wikipedia page
4-      **return** 1
5- else
      **return** -1
```

## Collaborators
Zulfiqar 
MOBEEN AHMED
## License
[MIT](https://choosealicense.com/licenses/mit/)
