# Cyclomatic Complexity Analyzer

## Description

This project analyzes the cyclomatic complexity of Python functions. It
demonstrates how cyclomatic complexity can be calculated using Python's `ast`
module.

## Project Structure

```css
cyclomatic_complexity_analyzer/
├── analyzer/
│   └── analyzer.py          # Main logic for cyclomatic complexity analysis
├── analyzees/
│   ├── function1.py         # Function file 1
│   ├── function2.py         # Function file 2
│   ├── function3.py         # Function file 3
│   ├── function4.py         # Function file 4
│   └── function5.py         # Function file 5
├── main.py                  # Entry point to run the analysis
└── README.md                # Documentation
```

### Directories and Files

- `analyzer/`: Contains the core logic for analyzing the cyclomatic complexity
  of Python functions.
- `analyzees/`: Contains Python files with functions whose cyclomatic complexity
  will be analyzed.
- `main.py`: The entry point for running the analysis on the functions in the
  `analyzees/` directory.
- `requirements.txt`: A list of Python dependencies needed for the project.

## Usage

1. Clone the repository
1. (Optional) Add Python files with single functions to the `analyzees/` directory.
1. Run the analysis:

   ```css
   python main.py
   ```

1. View the results in the console.

## Example Output

```css
function1.py: Cyclomatic Complexity = 5
function2.py: Cyclomatic Complexity = 4
function3.py: Cyclomatic Complexity = 3
```
