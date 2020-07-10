from lexer import lex as l

list_of_logical_operators = '><=!&|'
list_of_arithmetic_operators = '*-/+=%|'
list_of_syntactic_operators = '{}(),'
list_of_whitespace = '\\s\\t\\n'

def test_isArithmeticOperator():
    assert l.isArithmeticOperator('*') == True
    assert l.isArithmeticOperator('%') == True
    assert l.isArithmeticOperator('=') == True
    assert l.isArithmeticOperator('+') == True
    assert l.isArithmeticOperator('a') == False
    assert l.isArithmeticOperator('%') == True

def test_isLogicalOperator():
    for op in list_of_logical_operators:
        assert l.isLogicalOperator(op) == True


def test_lex():
    assert l("2 + 2") == [{'type': 'digit', 'value': '2'},
            {'type': 'arithmetic_operator', 'value': '+'},
            {'type': 'digit', 'value': '2'},
            {'type': 'end', 'value': 'end'}]

    assert l("22 + 2") == [{'type': 'digit', 'value': '22'},
                            {'type': 'arithmetic_operator', 'value': '+'},
                            {'type': 'digit', 'value': '2'},
                            {'type': 'end', 'value': 'end'}]




def test_isDigit():
    assert l.isDigit('1') == True
    assert l.isDigit('a') == False

def test_isWhiteSpace():
    assert l.isWhiteSpace(' ') == True
    assert l.isWhiteSpace(('    ')) == True
    assert l.isWhiteSpace(('1')) == True