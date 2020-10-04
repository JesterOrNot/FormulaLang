import sys
from antlr4 import *
from FormulaLexer import FormulaLexer
from FormulaParser import FormulaParser
from FormulaListener import FormulaListener

class FormulaPrintListener(FormulaListener):
  def enterOperation(self, ctx):
    operator = ctx.operator.text
    left = float(ctx.left.text)
    right = float(ctx.right.text)
    if operator == "+":
      print(left + right)
    elif operator == "-":
      print(left + right)
    elif operator == "*":
      print(left + right)
    elif operator == "/":
      print(left + right)
    elif operator == "%":
      print(left + right)
    else:
      print("Syntax Error")

def interpret(formula):
  lexer = FormulaLexer(InputStream(formula))
  stream = CommonTokenStream(lexer)
  parser = FormulaParser(stream)
  tree = parser.operation()
  printer = FormulaPrintListener()
  walker = ParseTreeWalker()
  walker.walk(printer, tree)

def main(argv):
  while True:
    formula = input(">>> ")
    interpret(formula)


if __name__ == '__main__':
    main(sys.argv)
