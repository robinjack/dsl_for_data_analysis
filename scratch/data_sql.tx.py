from textx import metamodel_from_file





def main():
    meta = metamodel_from_file('data_sql.tx')
    model = meta.model_from_str("SELECT col +1, sepal_length FROM TABLE where data_col < 10 and new_data_col=10")
    print()

if __name__ == '__main__':
    main()
    print()