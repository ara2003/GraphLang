
from enum import *

class SemanticContext:

    def __init__(self, isFunc = False) -> None:
        self.isFunc = isFunc
        self.variables = []
        self.functions = []

    def newFunctionContext(self):
        ctx = SemanticContext(True)
        ctx.variables.extend(self.variables)
        ctx.functions.extend(self.functions)
        return ctx
    
    def newContext(self):
        ctx = SemanticContext()
        ctx.variables.extend(self.variables)
        ctx.functions.extend(self.functions)
        return ctx
    
    def isFunctionContext(self) -> bool:
        return self.isFunc

    def hasVariable(self, name: str) -> bool:
        return name in self.variables

    def addVariable(self, name: str):
        self.variables.append(name)

    def hasFunction(self, name: str) -> bool:
        return name in self.functions

    def addFunction(self, name: str):
        self.functions.append(name)


