# 📄 Pytest automated tests avaliative activity


### ✍️ Goals
* Learn how to use **Pytest** and apply best testing practices in Python.
* Apply functional and structural testing techniques (Equivalence Partitioning and Boundary Value Analysis).
* Generate and analyze code coverage reports.

## ⬇️ Installation Instructions

To run this project properly, you can use **Poetry** (a Python packaging and dependency manager) or standard **pip**.

#### Option 1: Using Poetry (Recommended)
If you have Poetry installed, simply run the following commands to install dependencies and activate the virtual environment:

```bash
poetry install 
```

#### Option 2: Using Pip
Since this is a very small project, you can also easily install the required frameworks using pip:

```bash
pip install pytest pytest-cov 
```

## 🚀 Running the Tests

After installing the dependencies, run the command below. Pytest will execute the test suite, and pytest-cov will generate a full HTML coverage report.

```bash
pytest ./tests/ --cov --cov-report=html
```

#### 💡 Tip: After running the tests, a new folder named htmlcov will be created. Just open the index.html file inside it with your web browser to view the detailed coverage report.
