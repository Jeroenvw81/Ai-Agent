from functions.get_file_content import get_file_content

def main():
    result = get_file_content("calculator", "main.py")
    print(f"Result for 'main.py' directory:\n{result}")

    result = get_file_content("calculator", "pkg/calculator.py")
    print(f"Result for 'calculator.py' directory:\n{result}")
    
    result = get_file_content("calculator", "/bin/cat")
    print(f"Result for '/bin/cat' directory:\n{result}")

    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print(f"Result for 'pkg/does_not_exit.py' directory:\n{result}")


if __name__ == "__main__":
    main()