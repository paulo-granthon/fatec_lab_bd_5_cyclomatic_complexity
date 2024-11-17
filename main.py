import os

from analyzer import analyze_cyclomatic_complexity


def main():
    """
    Main function to scan all Python files in the 'analyzees' directory and
    print their cyclomatic complexity.

    It looks for `.py` files in the `analyzees/` directory, analyzes each one,
    and outputs the cyclomatic complexity of the function in each file.
    """

    analyzees_dir = "analyzees"
    for file in os.listdir(analyzees_dir):
        if file.endswith(".py"):
            file_path = os.path.join(analyzees_dir, file)
            complexity = analyze_cyclomatic_complexity(file_path)
            print(f"{file}: Cyclomatic Complexity = {complexity}")


if __name__ == "__main__":
    main()
