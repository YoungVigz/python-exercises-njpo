import re

class Validator:
    def __init__(self, successor=None):
        self._successor = successor

    def handle(self, request):
        if self._successor:
            return self._successor.handle(request)
        return True

class ParenthesesValidator(Validator):
    def handle(self, request):
        open_parentheses = request.count('(')
        close_parentheses = request.count(')')
        if open_parentheses != close_parentheses:
            return False
        return super().handle(request)

class OperatorValidator(Validator):
    def handle(self, request):
        if re.search(r'[a-zA-Z]\s*=\s*[a-zA-Z]', request) or re.search(r'=\s*', request):
            return super().handle(request)
        return False

class ExpressionValidator(Validator):
    def handle(self, request):
        pattern = re.compile(r'^[a-zA-Z]\s*[+\-*/]\s*[a-zA-Z]\s*=\s*[a-zA-Z]$')
        if pattern.match(request):
            return super().handle(request)
        return False

def validate_expression(expression):
    chain = ParenthesesValidator(OperatorValidator(ExpressionValidator()))
    if chain.handle(expression):
        print(f"Wyrażenie jest poprawne: {expression}")
    else:
        print(f"Wyrażenie jest niepoprawne: {expression}")

expressions = [
    "a + b = c",
    "(a + b = c",
    "a + = c"
]

for expr in expressions:
    validate_expression(expr)
