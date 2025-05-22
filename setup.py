from setuptools import find_packages, setup

setup(
    name="leetcode-solutions",
    version="0.1.0",
    description="Python solutions to LeetCode problems",
    author="Sang Ahn",
    author_email="mrdotmo@gmail.com",
    packages=find_packages(),
    python_requires=">=3.13",  # Updated to require Python 3.13+
    # No runtime dependencies as this is primarily a collection of solutions
    install_requires=[],
    # Development dependencies grouped in "dev" extra
    extras_require={
        "dev": [
            "isort >= 6.0.1",
            "pytest>=8.3.5",
            "pytest-cov>=6.1.1",
            "ruff>=0.11.1",
            "mypy>=1.15.0",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.13",  # Updated to Python 3.13
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Testing",
        "Private :: Do Not Upload",  # Prevents accidental upload to PyPI
    ],
)
