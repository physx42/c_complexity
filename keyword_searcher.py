# Scans C file for keywords

import numpy as np
import re

from pycparser import parse_file, c_parser, c_generator, c_ast, CParser


keywords = ["+", "-", "*", "/", "if", "for", "while", "return"]
kw_dict = {"+": "[^+]\+[^+]",
			"-": "[^-]\-[^-]",
			"*": "[^*]\*[^*]",
			"/": "[^/]\/[^/]",
			"if": "[^\w]if[^\w]",
			"for": "[^\w]for[^\w]",
			"while": "[^\w]while[^\w]",
			"return": "[^\w]return[^\w]"
			}

class FuncDefVisitor(c_ast.NodeVisitor):
    def visit_FuncDef(self, node):
        print('%s at %s' % (node.decl.name, node.decl.coord))
class FuncCallVisitor(c_ast.NodeVisitor):
    def __init__(self, funcname):
        self.funcname = funcname
    def visit_FuncCall(self, node):
        if node.name.name == self.funcname:
            print('%s called at %s' % (self.funcname, node.name.coord))

def show_func_calls(src, funcname):
    ast = CParser().parse(src)
    v = FuncCallVisitor(funcname)
    v.visit(ast)
def show_all_funcs(src):
    ast = CParser().parse(src)
    v = FuncDefVisitor()
    v.visit(ast)

def comment_remover(text):
    def replacer(match):
        s = match.group(0)
        if s.startswith('/'):
            return ""
        else:
            return s
    pattern = re.compile(
        r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
        re.DOTALL | re.MULTILINE
    )
    return re.sub(pattern, replacer, text)


def getOneHot(filename):
	# Scans the C file for how many instances of each keyword there are
	instances = np.zeros(len(keywords), dtype=int) #len(keywords)*[0]
	filename = "input/fnc1.c"

	f = open(filename, "r")
	file_contents = f.read()
	print(file_contents)

	for i, kw in enumerate(keywords):
		instances[i] = len(re.findall(kw_dict[kw],file_contents))

	print ("Keyword\tNum instances")
	for kw,inst in zip(keywords, instances):
		print (kw, "\t", inst)
	
	return instances

#def getEffort(filename):

filename = "./input/fnc1.c"
print (filename)
f = open(filename,"r")
src =comment_remover("".join(f.readlines()))

getOneHot(filename)

print("Show list of function definitions:")
show_all_funcs(src)
print ("Show calls for fnc1")
show_func_calls(src, "fnc1")