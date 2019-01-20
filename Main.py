from NER import NERCreator


def main():
    print("python main function")
    fact = NERCreator()
    fact.ReadFile("train.tsv")
    fact.CreateNER()


if __name__ == '__main__':
    main()
