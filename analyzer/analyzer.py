# pylint: disable=invalid-name,missing-function-docstring

import ast


class CyclomaticComplexityAnalyzer(ast.NodeVisitor):
    """
    A class that traverses the abstract syntax tree (AST) of a Python function
    to calculate its cyclomatic complexity by counting control flow statements.
    """

    def __init__(self):
        """
        Initialize the complexity counter to 0.
        """
        self.complexity = 0

    def visit_If(self, node):
        self.complexity += 1
        self.generic_visit(node)

    def visit_For(self, node):
        self.complexity += 1
        self.generic_visit(node)

    def visit_While(self, node):
        self.complexity += 1
        self.generic_visit(node)

    def visit_With(self, node):
        self.complexity += 1
        self.generic_visit(node)

    def visit_And(self, node):
        self.complexity += 1
        self.generic_visit(node)

    def visit_Or(self, node):
        self.complexity += 1
        self.generic_visit(node)


def analyze_cyclomatic_complexity(file_path):
    """
    Analyze the cyclomatic complexity of a Python file.

    Args:
    file_path (str): The path to the Python file to analyze.

    Returns:
    int: The cyclomatic complexity of the function in the file.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()
    tree = ast.parse(code)
    analyzer = CyclomaticComplexityAnalyzer()
    analyzer.visit(tree)
    return analyzer.complexity + 1  # Add 1 for the base path
