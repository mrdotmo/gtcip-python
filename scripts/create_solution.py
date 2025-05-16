#!/usr/bin/env python3
import os
import re
import sys
from pathlib import Path

def create_files(problem_number, problem_name, function_name):
    # Ensure problem number has leading zeros
    problem_number_str = str(problem_number).zfill(4)
    
    # Create the file name: p0001_two_sum.py
    file_base = f"p{problem_number_str}_{problem_name}"
    
    # Create the solution file
    solution_content = f"""class Solution:
    def {function_name}(self):
        \"\"\"
        LeetCode Problem {problem_number}: {problem_name.replace('_', ' ').title()}
        https://leetcode.com/problems/{problem_name}/
        
        TODO: Add problem description
        
        Args:
            TODO: Add parameters
            
        Returns:
            TODO: Add return value description
        \"\"\"
        # TODO: Implement solution
        pass
"""
    
    solution_path = Path('solutions') / f"{file_base}.py"
    
    # Create the test file
    test_content = f"""import unittest
from solutions.{file_base} import Solution

class Test{problem_name.replace('_', ' ').title().replace(' ', '')}(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        # TODO: Implement test cases
        pass

if __name__ == "__main__":
    unittest.main()
"""
    
    test_path = Path('tests') / f"test_{file_base}.py"
    
    # Write the files
    solution_path.parent.mkdir(exist_ok=True)
    test_path.parent.mkdir(exist_ok=True)
    
    with open(solution_path, 'w') as f:
        f.write(solution_content)
    
    with open(test_path, 'w') as f:
        f.write(test_content)
    
    print(f"Created solution file: {solution_path}")
    print(f"Created test file: {test_path}")

def main():
    if len(sys.argv) < 4:
        print("Usage: python create_solution.py <problem_number> <problem_name> <function_name>")
        print("Example: python create_solution.py 1 two_sum twoSum")
        sys.exit(1)
    
    problem_number = int(sys.argv[1])
    problem_name = sys.argv[2].lower().replace(' ', '_')
    function_name = sys.argv[3]
    
    create_files(problem_number, problem_name, function_name)

if __name__ == "__main__":
    main()