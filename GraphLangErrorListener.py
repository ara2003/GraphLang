from antlr4.error.ErrorListener import ErrorListener


class GraphLangErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print("Syntax error: line", line, "column", column, "message", msg)

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        print("Ambiguity error at indexes " + str(startIndex) + "-" + str(stopIndex))

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        print("Attempting full context error at indexes " + str(startIndex) + "-" + str(stopIndex))

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        print("Context sensitivity error at indexes " + str(startIndex) + "-" + str(stopIndex))