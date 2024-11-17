import os
import argparse
from analyzer import analyze_cyclomatic_complexity


def main(directory, debug=False):
    """
    Analyze all Python files in the specified directory for cyclomatic
    complexity.

    Args:
    directory (str): The directory containing Python files to analyze.
    debug (bool): Whether to enable debug mode for detailed output.
    """
    print(f"Analyzing files in directory: {directory}")
    print(f"Debug mode: {'ON' if debug else 'OFF'}")

    for filename in os.listdir(directory):
        if filename.endswith(".py"):
            file_path = os.path.join(directory, filename)
            print(f"\nAnalyzing {filename}:")
            complexity = analyze_cyclomatic_complexity(file_path, debug=debug)
            print(f"Cyclomatic Complexity: {complexity}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""
        Analyze Cyclomatic Complexity in a directory of Python files
        """
    )
    parser.add_argument(
        "--directory", default="analyzees", required=False,
        help="Path to the directory containing Python files to analyze"
    )
    parser.add_argument(
        "--debug", action="store_true", required=False,
        help="Enable debug mode to print detailed complexity analysis"
    )
    args = parser.parse_args()

    main(args.directory, debug=args.debug)
