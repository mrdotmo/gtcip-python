#!/usr/bin/env python3
import argparse
from pathlib import Path


def create_files(*, problem_number, function_name, problem_url):
    problem_name: str = problem_url.rstrip('/').split('/')[-1].replace('-', '_').title()
    # Ensure problem number has leading zeros
    problem_number_str = str(problem_number).zfill(4)

    # Create the file name: e.g. p0001_two_sum.py
    file_base = f"p{problem_number_str}_{problem_name.lower()}"

    # Create the solution file
    solution_content = f"""class Solution:
    def {function_name}(self):
        \"\"\"
        LeetCode Problem {problem_number}: {problem_name.replace("_", " ").title()}
        {problem_url}
        \"\"\"
        # TODO: Implement solution
        pass
"""

    solution_path = Path("solutions") / f"{file_base}.py"

    # Create the test file
    test_content = f"""from solutions.{file_base} import Solution


def test_{problem_name}():
    s = Solution()

    # TODO: Implement test cases

    pass
"""

    test_path = Path("tests") / f"test_{file_base}.py"

    # Write the files
    solution_path.parent.mkdir(exist_ok=True)
    test_path.parent.mkdir(exist_ok=True)

    with open(solution_path, "w") as f:
        f.write(solution_content)

    with open(test_path, "w") as f:
        f.write(test_content)

    print(f"Created solution file: {solution_path}")
    print(f"Created test file: {test_path}")


def main():
    # Create argument parser
    parser = argparse.ArgumentParser(
        description="Create LeetCode solution and test files.",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    # Add arguments
    parser.add_argument(
        "--problem-number", "-n", type=int, help="The LeetCode problem number"
    )
    parser.add_argument(
        "--function-name",
        "-f",
        type=str,
        help="The function name to use in the solution (e.g., twoSum)",
    )
    parser.add_argument(
        "-u",
        "--url",
        default='https://leetcode.com/problems/problem_name/',
        type=str,
        help="Optional custom problem URL "
        "(defaults to https://leetcode.com/problems/problem_name/)",
    )

    # Parse arguments
    args = parser.parse_args()

    create_files(
        problem_number=args.problem_number if args.problem_number else "<problem_number>",
        function_name=args.function_name if args.function_name else "<function_namne>",
        problem_url=args.url if args.url else "<problem_url>",
    )


if __name__ == "__main__":
    main()
