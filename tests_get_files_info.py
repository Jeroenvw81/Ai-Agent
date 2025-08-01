from functions.get_files_info import get_files_info


def main():
    result_calc = get_files_info("calculator", ".")
    print(f"Result for current directory:\n{result_calc}")

    result_pkg = get_files_info("calculator", "pkg")
    print(f"Result for 'pkg' directory:\n{result_pkg}")

    result_bin = get_files_info("calculator", "/bin")
    print(f"Result for '/bin' directory:\n{result_bin}")

    result_Err = get_files_info("calculator", "../")
    print(f"Result for '../' directory:\n{result_Err}")


if __name__ == "__main__":
    main()