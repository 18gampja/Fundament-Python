from parser import Parser
from tokenizer import Tokenizer
import sys

# if len(sys.argv) > 1 and sys.argv[1] == "start":
while 1 > 0:
    code = input()
    if code.lower() == "done":
      break
    parser = Parser(code)
    parsed = parser.parse_input()

    tokenizer = Tokenizer(parsed)
    tokenized = tokenizer.line_tokenizer()