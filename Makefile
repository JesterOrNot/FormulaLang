.PHONY: clean
.PHONY: build
.PHONY: test

test:
	python3 Formula.py

build:
	antlr -Dlanguage=Python3 -visitor Formula.g4

clean:
	rm *.interp *.tokens *Lexer.py *Parser.py *Listener.py *Visitor.py
