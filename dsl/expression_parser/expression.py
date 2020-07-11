import dsl.expression_parser.lexer.lex as l
import dsl.expression_parser.parser.Parser as parse




def ast(input_string):
    return parse(l(input_string)).parse()

