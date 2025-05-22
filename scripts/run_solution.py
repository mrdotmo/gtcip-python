#!/usr/bin/env python3
import importlib
import sys
import os
from pathlib import Path


def find_solution_file(problem_number):
    problem_number_str = str(problem_number).zfill(4)
    solutions_dir = Path("solutions")

    for file in solutions_dir.glob(f"p{problem_number_str}_*.py"):
        return file

    return None


def run_solution(problem_number, *args):
    solution_file = find_solution_file(problem_number)

    if not solution_file:
        print(f"Solution for problem {problem_number} not found.")
        sys.exit(1)

    # Extract module name from file path (e.g., 'solutions.p0001_two_sum')
    module_name = str(solution_file.with_suffix("")).replace(os.sep, ".")

    try:
        # Import the solution module
        solution_module = importlib.import_module(module_name)
        solution = solution_module.Solution()

        # Print available methods
        methods = [m for m in dir(solution) if not m.startswith("__")]
        if not methods:
            print(f"No solution methods found in {solution_file}.")
            sys.exit(1)

        if len(methods) == 1:
            method_name = methods[0]
        else:
            print("Available methods:")
            for i, method in enumerate(methods):
                print(f"{i + 1}. {method}")
            choice = int(input("Select method number: ")) - 1
            method_name = methods[choice]

        # Get the method
        method = getattr(solution, method_name)

        # Convert string arguments to appropriate types
        # This is a simple implementation and might need customization
        converted_args = []
        for arg in args:
            try:
                # Try to evaluate as Python literal
                converted_args.append(eval(arg))
            except:
                # If not possible, keep as string
                converted_args.append(arg)

        # Run the method with provided arguments
        result = method(*converted_args)
        print(f"Result: {result}")

    except Exception as e:
        print(f"Error running solution: {e}")
        import traceback

        traceback.print_exc()


def main():
    if len(sys.argv) < 2:
        print("Usage: python run_solution.py <problem_number> [arg1 arg2 ...]")
        print('Example: python run_solution.py 1 "[2,7,11,15]" 9')
        sys.exit(1)

    problem_number = int(sys.argv[1])
    args = sys.argv[2:]

    run_solution(problem_number, *args)


if __name__ == "__main__":
    main()
