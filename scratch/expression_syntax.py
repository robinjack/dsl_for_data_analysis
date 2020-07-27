from textx import metamodel_from_file





def main():
    meta = metamodel_from_file('expression_syntax.tx')
    model = meta.model_from_str("x = x + 1")
    print()

if __name__ == '__main__':
    main()
    print()