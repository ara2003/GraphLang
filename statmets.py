
from abc import *
from context import *

class Statment(ABC):
    
    @abstractmethod
    def checkSemantic(self, context: SemanticContext) -> bool:
        pass

class EmptyStatment(Statment):

    def checkSemantic(self, context: SemanticContext) -> bool:
        return True

class MergeStatment(Statment):
    
    def __init__(self, *statments) -> None:
        super().__init__()
        self.statments : list[Statment] = list(statments)

    def checkSemantic(self, context: SemanticContext) -> bool:
        for s in self.statments:
            if not s.checkSemantic(context):
                return False
        return True

class VarStatment(Statment):
    def __init__(self, name: str, line: int) -> None:
        super().__init__()
        self.name = name
        self.line = line

    def checkSemantic(self, context: SemanticContext) -> bool:
        if context.hasVariable(self.name):
            return True
        print("line: {self.line} variable '{self.name}' is not defined")
        return False

class VarDefStatment(Statment):
    def __init__(self, name: str, line: int) -> None:
        super().__init__()
        self.name = name
        self.line = line

    def checkSemantic(self, context: SemanticContext) -> bool:
        if context.hasVariable(self.name):
            print("line: {self.line} variable '{self.name}' already defined")
            return False
        context.addVariable(self.name)
        return True

class FuncCallStatment(Statment):
    def __init__(self, name: str, line: int) -> None:
        super().__init__()
        self.name = name
        self.line = line

    def checkSemantic(self, context: SemanticContext) -> bool:
        if context.hasFunction(self.name):
            return True
        print("line: {self.line} function '{self.name}' is not defined")
        return False

class FuncDefStatment(Statment):
    def __init__(self, name: str, parametrNames: list[str], code: Statment) -> None:
        super().__init__()
        self.name = name
        self.parametrNames = parametrNames
        self.code = code

    def checkSemantic(self, context: SemanticContext) -> bool:
        if context.hasFunction(self.name):
            print("line: {self.line} function '{self.name}' already defined")
            return False
        ctx = context.newFunctionContext()
        for name in self.parametrNames:
            ctx.addVariable(name)
        if not self.code.checkSemantic(ctx):
            return False
        context.addFunction(self.name)
        return True

class BlockStatment(Statment):
    def __init__(self, code: Statment) -> None:
        super().__init__()
        self.code = code

    def checkSemantic(self, context: SemanticContext) -> bool:
        ctx = context.newContext()
        return self.code.checkSemantic(ctx)
    
class ReturnStatment(Statment):

    def __init__(self, line: int) -> None:
        super().__init__()
        self.line = line

    def checkSemantic(self, context: SemanticContext) -> bool:
        if context.isFunctionContext():
            return True
        print("line: {self.line} 'return' outside function")
        return False
    