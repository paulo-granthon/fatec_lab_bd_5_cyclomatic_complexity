# pylint: disable=invalid-name,missing-function-docstring

import ast
import argparse


class CyclomaticComplexityAnalyzer(ast.NodeVisitor):
    """
    A class that traverses the abstract syntax tree (AST) of a Python function
    to calculate its cyclomatic complexity by counting control flow statements.
    """

    def __init__(self, debug=False):
        """
        Initialize the complexity counter and debug mode.

        Args:
        debug (bool): Whether to print debug messages.
        """
        self.complexity = 0
        self.debug = debug

    def _debug_log(self, message, node):
        """
        Print a debug message if debug mode is enabled.

        Args:
        message (str): The debug message to print.
        node (ast.AST): The AST node being processed.
        """
        if self.debug:
            line_number = getattr(node, "lineno", "unknown")
            print(f"{message} at line {line_number}")

    def visit_If(self, node):
        self.complexity += 1
        if self.debug:
            self._debug_log("\t• Found 'if' statement", node)
        self.generic_visit(node)

    def visit_For(self, node):
        self.complexity += 1
        if self.debug:
            self._debug_log("\t• Found 'for' loop", node)
        self.generic_visit(node)

    def visit_While(self, node):
        self.complexity += 1
        if self.debug:
            self._debug_log("\t• Found 'while' loop", node)
        self.generic_visit(node)

    def visit_With(self, node):
        self.complexity += 1
        if self.debug:
            self._debug_log("\t• Found 'with' statement", node)
        self.generic_visit(node)

    def visit_BoolOp(self, node):
        """
        Handle Boolean operations ('And' / 'Or').
        These nodes don't have `lineno`, so we log the parent or 'unknown'.
        """
        self.complexity += 1
        if self.debug:
            self._debug_log(
                f"\t• Found '{type(node.op).__name__.lower()}' operator",
                node
            )
        self.generic_visit(node)


def analyze_cyclomatic_complexity(file_path, debug=False):
    """
    Analyze the cyclomatic complexity of a Python file.

    Args:
    file_path (str): The path to the Python file to analyze.
    debug (bool): Whether to enable debug mode.

    Returns:
    int: The cyclomatic complexity of the function in the file.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()
    tree = ast.parse(code)
    analyzer = CyclomaticComplexityAnalyzer(debug=debug)
    analyzer.visit(tree)
    return analyzer.complexity + 1  # Add 1 for the base path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Cyclomatic Complexity Analyzer"
    )
    parser.add_argument(
        "file",
        help="Path to the Python file to analyze"
    )
    parser.add_argument(
        "--debug", action="store_true", required=False,
        help="Enable debug mode to print details"
    )
    args = parser.parse_args()

    complexity = analyze_cyclomatic_complexity(args.file, debug=args.debug)
    print(f"Cyclomatic Complexity: {complexity}")
