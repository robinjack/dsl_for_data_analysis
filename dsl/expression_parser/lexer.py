import string

"""
const lex = (input) => { // used some lambdas, even though this is not idiomatic (old style JS)
    const isOperator = (c) => /[+\-*\/\^%=(),]/.test(c);
    const isDigit = (c) => /[0-9]/.test(c);
    const isWhiteSpace = (c) => /\s/.test(c);
    const isIdentifier = (c) => typeof c === "string" && !isOperator(c) && !isDigit(c) && !isWhiteSpace(c);

    let tokens = [];
    let ch = 0;
    let index = 0;

    const advance = () => ch = input[++index]; // procedure rather than function!

    const addToken = (type, value) => // add an object
        tokens.push({
            type: type,
            value: value
        });

    // body of the "lex" function

    while (index < input.length) {
        ch = input[index];
        if (isWhiteSpace(ch)) {
            advance();
        } else if (isOperator(ch)) {
            addToken(ch);
            advance();
        } else if (isDigit(ch)) {
            let num = ch;
            while (isDigit(advance())) {
                num += ch;
            }
            if (ch === ".") {
                do {
                    num += ch;
                } while (isDigit(advance()));
            }
            num = parseFloat(num);
            if (!isFinite(num)) {
                throw "Number is too large or too small for a 64-bit double.";
            }
            addToken("number", num);
        } else if (isIdentifier(ch)) {
            let idn = ch;
            while (isIdentifier(advance())) {
                idn += ch;
            }
            addToken("identifier", idn);
        } else {
            throw "Unrecognized token.";
        }
    }
    addToken("(end)");
    return tokens;
};

exports.lex = lex;
"""


def lex(input):
    def isArithmeticOperator(char):
        return char in '*-/+%'

    def isLogicalOperator(char):
        return char in '><=!&|'

    def isMultiCharacterLogicalOperator(token):
        return token in ['==', '||', '>=', '<=', '!=', '&&']

    def isSyntacticOperator(char):
        return char in '{}(),'

    def isDigit(char):
        return char in '0123456789'

    def isWhiteSpace(char):
        # TODO: add all the relevant whitespaces
        return char == ' ' or char == '\t' or char == '\n'

    # def isNewLine(char):
    # 	# TODO: figure out how to do newlines
    # 	return char == '\n'

    def isLetter(char):
        return char in string.ascii_letters

    def isReservedWord(token):
        return token in ['print', 'if', 'else', 'while']

    tokens = []
    ch = 0
    index = 0

    """
    Plan for lexer:
    for character in input:
    if it is whitespace, continue
    if it is an operator 
        (syntactic, add token with type, value)
        logical, continue once to see if also logicalm
        add token with type, value
        syntactic -- add token with type value

    if it is a digit, advance until no longer a digit
    and add the number 

    if it is a letter, advance until no longer a letter
    test to see if it is one of the reserved words
    if it is, explain it is a reserved word - otherwise add to 
    """

    def addToken(type, value=None):
        tokens.append({
            'type': type,
            'value': value
        })

    def addMultiCharacterToken(char, func, t, index):
        token = char
        while func(char):
            index += 1
            if index < len(input):
                char = input[index]
                if func(char):
                    token += char
                    index += 1
                else:
                    index += 1

        addToken(t, token)
        index += 1
        return index

    while index < len(input):
        char = input[index]
        if isWhiteSpace(char):
            index += 1
        elif isSyntacticOperator(char):
            addToken(char)
            index += 1
        elif isLogicalOperator(char):
            token = char
            index += 1
            char = input[index]
            if isLogicalOperator(char):
                token += char
                index += 1
                addToken(token)
            else:
                addToken(token)
        elif isArithmeticOperator(char):
            addToken(char)
            index += 1
        elif isDigit(char):
            # addMultiCharacterToken(char, isDigit, 'digit', index)
            token = char
            index += 1
            while (isDigit(char) and index < len(input)):
                char = input[index]
                if isDigit(char):
                    token += char
                    index += 1
                else:
                    break
            addToken('digit', token)
        # index+=1
        elif isLetter(char):
            # token=''
            token = char
            index += 1
            char = input[index]

            while (isLetter(char)):
                if index < len(input):
                    char = input[index]
                    if isLetter(char):
                        token += char
                        index += 1
                    else:
                        break
                else:
                    break
            if isReservedWord(token):
                addToken(token)
            else:
                addToken('identifier', token)
        # elif isNewLine(char):
        # 	addToken('newline')
        # 	index+=1
        else:
            raise Exception("Character not recognised as a valid expression: ", char)
    addToken('end', 'end')
    return tokens





