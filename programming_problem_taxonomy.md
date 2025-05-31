# Programming Problem Classification Rubric

## 🔍 How to Use This Rubric
1. Read the problem statement carefully
2. Look for key characteristics and keywords
3. Check multiple categories as problems often combine techniques
4. Start with the most obvious pattern, then consider optimizations

---

## 📊 Dynamic Programming (DP)

### **Key Identifiers:**
- **Optimal substructure**: Solution can be built from optimal solutions of subproblems
- **Overlapping subproblems**: Same subproblems solved multiple times
- **Keywords**: "maximum/minimum", "count ways", "optimal", "best"

### **Common Patterns:**
- **Optimization problems**: Find max/min value
- **Counting problems**: Number of ways to do something
- **Decision problems**: Is it possible to achieve X?

### **Red Flags for DP:**
- "Find the maximum sum..."
- "Count the number of ways..."
- "What's the minimum cost to..."
- Involves sequences, arrays, or grids
- Previous choices affect future options
- Exponential brute force solution exists

### **Sub-types:**
- **Linear DP**: 1D array problems (Fibonacci, house robber)
- **2D DP**: Grid problems, string matching
- **Tree DP**: Problems on trees
- **Digit DP**: Problems involving digit constraints
- **Bitmask DP**: State represented by bitmasks

---

## 🎯 Greedy Algorithms

### **Key Identifiers:**
- **Local optimal choices**: Making best choice at each step
- **No need to reconsider**: Once choice is made, it's final
- **Keywords**: "schedule", "interval", "deadline", "priority"

### **Common Patterns:**
- Activity/interval scheduling
- Huffman coding type problems
- Fractional knapsack
- Minimum spanning tree

### **Red Flags for Greedy:**
- "Schedule activities to maximize..."
- "Assign tasks to minimize..."
- Sorting often helps
- Exchange argument works
- Choice property exists

---

## 🌐 Graph Algorithms

### **Key Identifiers:**
- **Explicit graphs**: Nodes and edges given
- **Implicit graphs**: Grid, state transitions
- **Keywords**: "connected", "path", "distance", "reachable"

### **Sub-categories:**

#### **DFS/BFS Traversal:**
- Find connected components
- Check if path exists
- Explore all possibilities
- **Grid traversal** (2D arrays as graphs)

#### **Shortest Path:**
- **Dijkstra**: Non-negative weights, single source
- **Bellman-Ford**: Negative weights allowed
- **Floyd-Warshall**: All pairs shortest path
- **BFS**: Unweighted graphs

#### **Minimum Spanning Tree:**
- **Kruskal's/Prim's**: Connect all nodes with minimum cost

#### **Topological Sort:**
- **DAG problems**: Dependencies, course scheduling
- **Keywords**: "prerequisite", "dependency", "order"

#### **Strong Connected Components:**
- **Tarjan's/Kosaraju's**: Find SCCs in directed graphs

---

## 🏗️ Data Structures

### **Segment Trees/Fenwick Trees:**
- **Range queries**: Sum, min, max over ranges
- **Point updates**: Update single elements
- **Keywords**: "range sum", "range minimum", "update queries"

### **Union-Find (Disjoint Set):**
- **Dynamic connectivity**: Check if elements connected
- **Keywords**: "connected components", "merge sets"

### **Priority Queue/Heap:**
- **Keywords**: "kth largest", "top k", "median"
- Always need the min/max element

### **Trie:**
- **String problems**: Prefix matching, word search
- **Keywords**: "prefix", "dictionary", "word game"

---

## 🔢 Mathematics & Number Theory

### **Key Identifiers:**
- **Keywords**: "prime", "factorial", "modulo", "GCD", "LCM"
- Mathematical formulas can solve directly
- Pattern recognition in sequences

### **Common Types:**
- **Prime numbers**: Sieve of Eratosthenes
- **Modular arithmetic**: Large numbers with MOD
- **Combinatorics**: Permutations, combinations
- **Number theory**: GCD, LCM, Euclidean algorithm

---

## 🧵 String Algorithms

### **Key Identifiers:**
- **String manipulation**: Substrings, patterns
- **Keywords**: "substring", "pattern", "match", "palindrome"

### **Common Algorithms:**
- **KMP**: Pattern matching
- **Rolling hash**: String hashing
- **Suffix array/tree**: Advanced string processing
- **Manacher's**: Palindrome detection

---

## 🔍 Two Pointers & Sliding Window

### **Two Pointers:**
- **Sorted arrays**: Find pairs with target sum
- **Keywords**: "two sum", "pair", "opposite ends"

**Does your problem match this pattern?**
Yes, if all of these conditions are fulfilled:
* **Linear data structure:** The input data can be traversed in a linear fashion, such as an array, linked list, or string.
* **Process pairs:** Process data elements at two different positions simultaneously.
* **Dynamic pointer movement:** Both pointers move independently of each other according to certain conditions or criteria. In addition, both pointers might move along the same or two different data structures.

### **Fast and Slow Pointers:**
- **Cycle detection**: Floyd's algorithm, tortoise and hare
- **Keywords**: "cycle", "loop", "middle element", "intersection"

**Does your problem match this pattern?**
Yes, if the following condition is fulfilled:
* **Linear data structure:** The input data can be traversed in a linear fashion, such as an array, linked list, or string.

In addition, if either of these conditions is fulfilled:
* **Cycle or intersection detection:** The problem involves detecting a loop within a linked list or an array or involves finding an intersection between two linked lists or arrays.
* **Find the starting element of the second quantile:** This means identifying the element where the second part of a divided dataset begins—like the second half, second third (tertile), or second quarter (quartile). For example, the task might ask you to find the middle element of an array or a linked list, which marks the start of the second half.

### **Sliding Window:**
- **Contiguous subarrays**: Fixed or variable size windows
- **Keywords**: "subarray", "substring", "window", "consecutive"

**Does your problem match this pattern?**
Yes, if all of these conditions are fulfilled:
* **Contiguous data:** The input data is stored in a contiguous manner, such as an array or string.
* **Processing subsets of elements:** The problem requires repeated computations on a contiguous subset of data elements (a subarray or a substring), such that the window moves across the input array from one end to the other. The size of the window may be fixed or variable, depending on the requirements of the problem.
* **Efficient computation time complexity:** The computations performed every time the window moves take constant or very small time.

---

## 🔄 Backtracking

### **Key Identifiers:**
- **Explore all possibilities**: Try all combinations
- **Constraint satisfaction**: N-Queens, Sudoku
- **Keywords**: "all possible", "generate", "permutation"

### **Common Patterns:**
- Generate all permutations/combinations
- Constraint satisfaction problems
- Puzzle solving

---

## ⚡ Divide & Conquer

### **Key Identifiers:**
- **Break into subproblems**: Similar smaller problems
- **Combine results**: Merge solutions
- **Keywords**: Often involves recursion

### **Common Examples:**
- Merge sort, quick sort
- Binary search
- Fast exponentiation

---

## 🎲 Game Theory

### **Key Identifiers:**
- **Two-player games**: Optimal play assumption
- **Keywords**: "game", "player", "optimal strategy", "win/lose"
- **Nim games**: XOR operations

---

## 🔧 Bit Manipulation

### **Key Identifiers:**
- **Binary operations**: AND, OR, XOR, shifts
- **Keywords**: "bit", "binary", "power of 2"
- Often involves XOR properties

---

## 📐 Computational Geometry

### **Key Identifiers:**
- **Geometric objects**: Points, lines, polygons
- **Keywords**: "coordinate", "distance", "area", "intersection"

---

## 🚀 Quick Decision Tree

1. **Does it involve optimization or counting?** → Consider DP
2. **Can you make greedy choices?** → Try Greedy
3. **Are there nodes and edges?** → Graph algorithms
4. **Range queries or updates?** → Data structures
5. **String processing?** → String algorithms
6. **Mathematical formulas?** → Math/Number theory
7. **Need to try all possibilities?** → Backtracking
8. **Two pointers or windows?** → Two pointers/Sliding window

## 💡 Pro Tips

- **Read constraints carefully**: Often hints at the expected algorithm
- **Small constraints (n ≤ 20)**: Might allow brute force or backtracking
- **Medium constraints (n ≤ 10³)**: O(n²) solutions
- **Large constraints (n ≤ 10⁶)**: Need O(n log n) or O(n) solutions
- **Very large constraints (n ≤ 10⁹)**: Need O(log n) or O(1) solutions

**Remember**: Many problems combine multiple techniques! Start with the most obvious pattern and then optimize.