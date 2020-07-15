# from dsl.expression_parser.lexer import Lex
#
# list_of_logical_operators = '><=!&|'
# list_of_arithmetic_operators = '*-/+=%|'
# list_of_syntactic_operators = '{}(),'
# list_of_whitespace = '\\s\\t\\n'
#
# l = Lex()

# def test_isArithmeticOperator():
#     assert l.isArithmeticOperator('*')
#     assert l.isArithmeticOperator('%')
#     assert l.isArithmeticOperator('=')
#     assert l.isArithmeticOperator('+')
#     assert not l.isArithmeticOperator('a')
#     assert l.isArithmeticOperator('%')
#
# def test_isLogicalOperator():
#     for op in list_of_logical_operators:
#         assert l.isLogicalOperator(op)
#
#
# def test_lex():
#     assert l.lex("2 + 2") == [{'type': 'digit', 'value': '2'},
#             {'type': 'arithmetic_operator', 'value': '+'},
#             {'type': 'digit', 'value': '2'},
#             {'type': 'end', 'value': 'end'}]
#
#     assert l.lex("22 + 2") == [{'type': 'digit', 'value': '22'},
#                             {'type': 'arithmetic_operator', 'value': '+'},
#                             {'type': 'digit', 'value': '2'},
#                             {'type': 'end', 'value': 'end'}]
#
#
#
#
# def test_isDigit():
#     assert l.isDigit('1')
#     assert l.isDigit('a')
#
# def test_isWhiteSpace():
#     assert l.isWhiteSpace(' ')
#     assert l.isWhiteSpace(('    '))
#     assert not l.isWhiteSpace(('1'))