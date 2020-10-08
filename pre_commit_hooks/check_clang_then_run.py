import sys
import subprocess

def main():
    # First run clang-format to check it exists
    try:
        result = subprocess.run("clang-format-6.0")
    except FileNotFoundError:
        print("clang-format-6.0 not found, skipping this check")
        return 0
    result = subprocess.run(["clang-format-6.0", *sys.argv[1:]])
    return result.returncode
