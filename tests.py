from functions.run_python_file import run_python_file

def main():

    result = run_python_file("calculator", "main.py")
    print(f"Result for 'main.py':\n{result}")

    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print(f"Result for 'main.py, ['3 + 5']':\n{result}")

    result = run_python_file("calculator", "tests.py")
    print(f"Result for 'tests.py':\n{result}")

    result = run_python_file("calculator", "../main.py")
    print(f"Result for '../main.py':\n{result}")

    result = run_python_file("calculator", "nonexistent.py")
    print(f"Result for 'nonexistent.py':\n{result}")

    result = run_python_file("calculator", "empty.py")
    print(f"Result for 'empty.py': {result}")

if __name__ == "__main__":
    main()