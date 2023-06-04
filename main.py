from antlr4 import *

from context import *
from statmets import *

from grammer.GraphLangLexer import GraphLangLexer
from grammer.GraphLangParser import *
from GraphLangErrorListener import GraphLangErrorListener
from grammer.GraphLangVisitor import *


class GraphLangVisitor(GraphLangVisitor):

    def aggregateResult(self, aggregate, nextResult):
        return MergeStatment(aggregate, nextResult)

    def defaultResult(self):
        return EmptyStatment()

    def visitInit_var_stmt(self, ctx: GraphLangParser.Init_var_stmtContext):
        return MergeStatment(VarDefStatment(ctx.ID().getText(), ctx.getChild(0).symbol.line), self.visit(ctx.expr()))

    def visitVariable_expr(self, ctx: GraphLangParser.Variable_exprContext):
        return VarStatment(ctx.ID().getText(), ctx.getChild(0).symbol.line)

    def visitFunc_call(self, ctx: GraphLangParser.Func_callContext):
        return MergeStatment(VarDefStatment(ctx.ID().getText(), ctx.getChild(0).symbol.line), *map(self.visit, ctx.expr()))

    def visitFunc_def_stmt(self, ctx: GraphLangParser.Func_def_stmtContext):
        return FuncDefStatment(ctx.ID().getText(), list(map(self.visit, ctx.parametr())), self.visit(ctx.code()), ctx.getChild(0).symbol.line)

    def visitReturn_stmt(self, ctx: GraphLangParser.Return_stmtContext):
        return MergeStatment(ReturnStatment(ctx.getChild(0).symbol.line), self.visit(ctx.expr()))

    def visitCode_block(self, ctx: GraphLangParser.Code_blockContext):
        return BlockStatment(self.visit(ctx.code()))

def main():

    input_stream = FileStream("input.txt")

    lexer = GraphLangLexer(input_stream)
    stream = CommonTokenStream(lexer)

    parser = GraphLangParser(stream)
    parser.removeErrorListeners()

    error_listener = GraphLangErrorListener()

    parser.addErrorListener(error_listener)
    tree = parser.stat()
    print(tree)

    visitor = GraphLangVisitor()
    visitor.visitStat(tree)


if __name__ == '__main__':
    main()
