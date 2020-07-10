


"""
EXAMPLE:

input = "x = 2"
output = "Node(type="root",
children = [Node(type="assign", children =
[Node(type="identifier", value="x"),
Node(type="integer", value=2)]))

[{'type': 'identifier', 'value': 'val'} {'type': 'logical_operator', 'value': '='}, {'type': 'digit', 'value': '104'}, {'type': 'reserved_word', 'value': 'while'}, {'type': 'syntactic_operator', 'value': '('}, {'type': 'identifier', 'value': 'val'}, {'type': 'logical_operator', 'value': '>='}, {'type': 'digit', 'value': '2'}, {'type': 'syntactic_operator', 'value': '{'}, {'type': 'reserved_word', 'value': 'if'}, {'type': 'syntactic_operator', 'value': '('}, {'type': 'identifier', 'value': 'val'}, {'type': 'arithmetic_operator', 'value': '%'}, {'type': 'digit', 'value': '2'}, {'type': 'logical_operator', 'value': '=='}, {'type': 'digit', 'value': '0'}, {'type': 'identifier', 'value': 'next'}, {'type': 'logical_operator', 'value': '='}, {'type': 'identifier', 'value': 'val'}, {'type': 'arithmetic_operator', 'value': '/'}, {'type': 'digit', 'value': '2'}, {'type': 'reserved_word', 'value': 'else'}, {'type': 'identifier', 'value': 'next'}, {'type': 'logical_operator', 'value': '='}, {'type': 'digit', 'value': '3'}, {'type': 'arithmetic_operator', 'value': '*'}, {'type': 'identifier', 'value': 'val'}, {'type': 'arithmetic_operator', 'value': '+'}, {'type': 'digit', 'value': '1'}, {'type': 'reserved_word', 'value': 'print'}, {'type': 'identifier', 'value': 'val'}, {'type': 'identifier', 'value': 'next'}, {'type': 'identifier', 'value': 'val'}, {'type': 'logical_operator', 'value': '='}, {'type': 'identifier', 'value': 'next'}, {'type': 'syntactic_operator', 'value': '}'}, {'type': 'end', 'value': 'end'}]


def parse(tokens):




rules for different types of statements:

assignment:
identifier = expression
i.e. an assignment has two children. Assignment is denoted by =
it takes from before it, and after it

print
evaluates and prints out everything after it, until there is a new line
TODO: add in the new line to the tokens

selection	if ( expression ) statement1 else statement2

started by "if" - it has three children
first child: the expression to be evaluated (begun and ended by a bracket)
seceond child: everytihng up until "else"
third child: everything after else

iteration: it has two children
1. the condition (started and ended by a bracket)
2. the statement (ended by "end" or })

compound:
this has as many children as it wants, but it is ended by }

"""


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0
        self.symbols = {}
        self.current_token = None

        self.symbol(",")
        self.symbol(")")
        self.symbol("}")
        self.symbol("newline")
        self.symbol("digit", lambda number: number)
        self.symbol("identifier", lambda name: name)
        self.symbol("(", self.parenthesis)

        self.infix("==", 7)
        self.infix(">", 7)
        self.infix("<", 7)
        self.infix("<=", 7)
        self.infix(">=", 7)
        self.infix("&&", 7)
        self.infix("||", 7)
        self.infix("!=", 7)
        self.infix("^", 6, 5)
        self.infix("*", 4)
        self.infix("/", 4)
        self.infix("%", 4)
        self.infix("+", 3)
        self.infix("-", 3)
        self.prefix('-')

        self.infix('=', 1, 2, self.assignment)

    def parse(self):
        parseTree = []
        #         pp.pprint(self.symbols)
        while self.token()['type'] != 'end':
            parseTree.append(self.expression(0))
        return parseTree

    def symbol(self, id, ndf=None, lbp=None, ldf=None):
        """
        // 1. Associate every operational token with a "left binding power" (lbp),
//    and an operational function.
// 2. If the operator manipulates tokens to its left (such as "+"),
//    associate it with a "left denotative function" (ldf).
// 3. If the operator does not manipulate the tokens on its left (such as the unary "-"),
//    associate it with a "null denotative function" (ndf).
// 4. Identifiers and numbers also have a "ndf" function associated with them.
        """
        sym = self.symbols.get(id, {})

        self.symbols[id] = {
            'lbp': sym.get('lbp', lbp),
            'ndf': sym.get('ndf', ndf),
            'ldf': sym.get('ldf', ldf)
        }
        return sym

    def token(self):
        self.current_token = self.tokens[self.index]
        sym = self.symbol(self.current_token['type'])
        sym['type'] = self.current_token['type']
        sym['value'] = self.current_token['value']
        return sym

    def advance(self):
        self.index += 1
        self.token()

    def expression(self, rbp):
        left = self.token()
        t = self.token()
        self.advance()
        if t['ndf'] is None:
            raise Exception("Unexpected token: ", t['type'])
        left = t['ndf'](t)
        while True:
            self_token_lbp = self.token()['lbp']
            if self_token_lbp is not None and (rbp < self_token_lbp or self.token()['type'] == '='):
                t = self.token()
                self.advance()
                if t['ldf'] is None:
                    raise Exception("Unexpected token: ", t['type'])
                left = t['ldf'](left)
            else:
                break

        return left

    def infix(self, id, lbp=None, rbp=None, ldf=None):
        rbp = self.choose_non_null(rbp, lbp)
        self.symbol(id, None, lbp, self.choose_non_null(ldf,
                                                        lambda left: {'type': id,
                                                                      'left': left,
                                                                      'right': self.expression(rbp)}
                                                        ))

    def prefix(self, id, rbp):
        def func(id, rbp):
            return {'type': id, 'right': self.expression(rbp)}
            self.symbol(id, func(id, rbp))

    def choose_non_null(self, first_val, second_val):
        if first_val is not None:
            return first_val
        else:
            return second_val


    def parenthesis(self, val=None):
        value = self.expression(2)
        if self.token()['type'] != ")":
            raise Exception("Expected closing parenthesis )")
        self.advance()
        return value






