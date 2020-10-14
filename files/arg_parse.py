import argparse

def main():
    parser = argparse.ArgumentParser(description="Mots dans la liste de Swadesh")
    parser.add_argument("-v", "--verbose", help="verbose mode", action="store_true")
    parser.add_argument("file", help="input file")
    args = parser.parse_args()

    print(args.file)

if __name__ == "__main__":
    main()
