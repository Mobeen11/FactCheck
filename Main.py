from NER import NERCreator


def main():

    fact = NERCreator()
    fact.ReadFile("test.tsv")
    fact.CreateNER()


if __name__ == '__main__':
    main()
