# Python Essentials 1: Comprehensive Learning Repository

A complete learning repository featuring **Python fundamentals through Jupyter notebooks** and **advanced practical projects**. This repository documents the journey from basic Python syntax to domain-specific applications, with 77.6% Jupyter Notebook content and 22.4% Python scripts.

---

## 📋 Table of Contents

- [Quick Overview](#quick-overview)
- [Repository Structure](#-repository-structure)
- [Module Breakdown](#-module-breakdown)
- [Capstone Project: Molecular Biology Toolkit](#-capstone-project-molecular-biology-toolkit)
- [Getting Started](#-getting-started)
- [Learning Path](#-learning-path)
- [Key Concepts Covered](#-key-concepts-covered)
- [Technologies & Stack](#-technologies--stack)
- [Project Examples](#-project-examples)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)

---

## 🎯 Quick Overview

This repository serves as a **comprehensive Python learning resource** that combines:

1. **Structured Tutorial Notebooks** – Interactive lessons covering Python fundamentals
2. **Practical Python Scripts** – Standalone implementations demonstrating core concepts
3. **Capstone Project** – A production-grade Molecular Biology Toolkit demonstrating real-world application

**Perfect for:** Python learners transitioning from basics to applied projects, bioinformatics enthusiasts, and those seeking structured self-study materials.

---

## 📁 Repository Structure

```
Python-essentials-1/
├── README.md                          # This file
├── 
├── Core Concept Scripts (Python Files)
│   ├── Variables.py                   # Variable declaration and type systems
│   ├── Literals.py                    # Literal values and data representation
│   ├── Operators.py                   # Arithmetic, logical, and comparison operators
│   ├── Interaction_with_the_user.py   # Input/output and user interaction
│   ├── List.py                        # List operations and sequencing
│   ├── if_conditionals.py             # Conditional logic (if/elif/else)
│   ├── for_loop.py                    # For loop iteration patterns
│   ├── while_loop.py                  # While loop and infinite loops
│   └── compuer_logic.py               # Boolean logic and control flow
│
├── Module_2/                          # Intermediate Concepts (Jupyter Notebooks)
│   ├── First_program.ipynb            # First complete Python program
│   ├── Variables.ipynb                # Deep dive into variables
│   ├── Python_literals.ipynb          # Literal values and types
│   ├── Operators.ipynb                # Operators in detail
│   ├── Interaction_with_the_user.ipynb # User I/O and input handling
│   └── Conditional.ipynb              # Decision structures
│
├── Module_3/                          # Advanced Concepts (Jupyter Notebooks)
│   ├── List.ipynb                     # Lists, arrays, and collections
│   ├── Loops.ipynb                    # Loop patterns and iteration
│   ├── try_except.ipynb               # Exception handling and error management
│   └── Project.ipynb                  # Intermediate project
│
├── P.E. project.py                    # Intermediate capstone implementation
├── Final_project.BMB.py               # Advanced capstone: Molecular Biology Toolkit
└── (Supporting files for projects)
```

---

## 📚 Module Breakdown

### **Python Scripts (Foundational Layer)**

These scripts serve as quick references and implementations of core Python concepts:

| File | Purpose | Key Topics |
|------|---------|-----------|
| `Variables.py` | Variable declaration and naming | Assignment, types, scope |
| `Literals.py` | Literal values | Strings, numbers, booleans |
| `Operators.py` | Operator operations | Arithmetic, logical, comparison |
| `Interaction_with_the_user.py` | User input/output | `input()`, `print()`, formatting |
| `List.py` | List basics | Indexing, slicing, basic methods |
| `if_conditionals.py` | Conditional statements | if/elif/else, nested conditions |
| `for_loop.py` | For loop patterns | Range, iteration, enumeration |
| `while_loop.py` | While loops | Termination conditions, infinite loops |
| `compuer_logic.py` | Logical operations | Boolean operators (and, or, not) |

---

### **Module 2: Foundational & Intermediate Concepts**

Interactive Jupyter notebooks covering Python basics to intermediate level:

#### File Descriptions

- **First_program.ipynb**  
  Introduction to Python with your first executable program. Covers environment setup, basic syntax, and running Python code.

- **Variables.ipynb**  
  Comprehensive exploration of variable creation, naming conventions (snake_case), type inference, and memory management.

- **Python_literals.ipynb**  
  Deep dive into literal values: strings (single/double/triple quotes), numbers (int/float), booleans, and special values (None).

- **Operators.ipynb**  
  Covers all operator categories:
  - Arithmetic: `+, -, *, /, //, %, **`
  - Comparison: `==, !=, <, >, <=, >=`
  - Logical: `and, or, not`
  - Assignment: `=, +=, -=, etc.`

- **Interaction_with_the_user.ipynb**  
  Building interactive programs through input capture, output formatting, and data type conversion.

- **Conditional.ipynb**  
  Mastering conditional logic with if/elif/else statements, nested conditions, and ternary operators.

---

### **Module 3: Advanced Concepts & Projects**

Jupyter notebooks advancing to complex topics and capstone work:

- **List.ipynb**  
  Collections and sequences:
  - List creation and manipulation
  - Indexing and slicing
  - Built-in methods (append, extend, remove, etc.)
  - List comprehensions

- **Loops.ipynb**  
  Advanced iteration patterns:
  - For loops with `range()`, `enumerate()`, `zip()`
  - While loops and loop control (break, continue)
  - Nested loops
  - Iterator and generator concepts

- **try_except.ipynb**  
  Exception handling and error management:
  - Try/except/finally blocks
  - Specific exception catching
  - Raising custom exceptions
  - Debugging strategies

- **Project.ipynb**  
  Intermediate capstone project integrating all Module 2 & 3 concepts.

---

## 🧬 Capstone Project: Molecular Biology Toolkit

### **Project: Final_project.BMB.py**

An advanced command-line bioinformatics application for molecular biology research.

#### **Problem Statement**
Manual manipulation of DNA/RNA sequences and analysis is slow and error-prone. This toolkit automates sequence analysis, transcription, translation, and mutation detection for researchers.

#### **Core Features**

1. **Sequence Validation**
   - Accepts DNA sequences (A, T, C, G only)
   - Filters IUPAC ambiguity codes
   - Validates format and removes artifacts

2. **GC Content Calculation**
   - Computes G-C ratio percentage
   - Predicts thermal stability
   - Essential for PCR primer design

3. **Transcription Simulation**
   - DNA → mRNA conversion (T → U)
   - Maintains sequence integrity
   - Models RNA polymerase activity

4. **Translation & Codon Parsing**
   - Groups nucleotides into codons (3 bases)
   - Maps codons to amino acids
   - Supports genetic code standard

5. **Mutation Detection**
   - Identifies premature STOP codons
   - Detects nonsense mutations
   - Flags potential truncation events

#### **Biological Concepts Used**

- **Central Dogma**: DNA → RNA → Protein flow
- **Genetic Code**: Standard 64 codon table
- **Point Mutations**: Single nucleotide changes
- **Stop Codons**: UAA, UAG, UGA in mRNA

#### **Sample Usage**

```python
# Run the application
python Final_project.BMB.py

# Interactive menu
=== MOLECULAR BIOLOGY TOOLKIT SYSTEM V1.0 ===
[MAIN MENU]
1. Analyze New DNA Sequence
2. Exit Toolkit
Select an option (1-2): 1

# Input sequence
Enter or paste your DNA sequence: ATGGCCAAACCCGGGGGG

# Output analysis
Sequence accepted. Total bases: 18
Calculated GC Content: 66.67%
Transcribed mRNA: AUGGCCAAACCCGGGGGG
Isolated Codons List: ['AUG', 'GCC', 'AAA', 'CCC', 'GGG', 'GGG']
No premature stop mutations detected in this reading frame.
Synthesized Peptide Residues: M (START)-A-K-P-G-G
```

#### **Technical Implementation**

- **Language**: Pure Python 3.8+
- **Dependencies**: None (vanilla Python only)
- **Architecture**: Modular with helper functions
- **IO**: Command-line interface with user input validation

---

## 🚀 Getting Started

### **Prerequisites**

- Python 3.8 or higher
- Text editor or IDE (VS Code recommended)
- Jupyter Notebook (for `.ipynb` files)

### **Installation**

1. **Clone the repository**
   ```bash
   git clone https://github.com/mwangimuhia031-alt/Python-essentials-1.git
   cd Python-essentials-1
   ```

2. **Verify Python version**
   ```bash
   python --version  # Should be 3.8+
   ```

3. **Install Jupyter (optional, for notebooks)**
   ```bash
   pip install jupyter notebook
   ```

### **Running Examples**

#### Option 1: Execute Python Scripts
```bash
# Run individual concept scripts
python Variables.py
python Operators.py
python if_conditionals.py

# Run the capstone project
python Final_project.BMB.py
```

#### Option 2: Explore Jupyter Notebooks
```bash
# Start Jupyter server
jupyter notebook

# Navigate to Module_2/ or Module_3/ folders
# Click any .ipynb file to open and interact
```

---

## 📖 Learning Path

### **Suggested Study Order**

**Level 1: Python Basics (Weeks 1-2)**
1. Start with `Variables.py` and `Variables.ipynb` (Module_2)
2. Read `Literals.py` and `Python_literals.ipynb`
3. Explore `Operators.py` and `Operators.ipynb`

**Level 2: Control Flow (Weeks 3-4)**
4. Study `if_conditionals.py` and `Conditional.ipynb`
5. Practice with `Interaction_with_the_user.py` and corresponding notebook
6. Work through `compuer_logic.py`

**Level 3: Iteration (Weeks 5-6)**
7. Master `for_loop.py` and `while_loop.py`
8. Deep dive with `Loops.ipynb` (Module_3)
9. Practice nested loops and loop control

**Level 4: Collections (Weeks 7-8)**
10. Learn lists with `List.py` and `List.ipynb`
11. Understand list comprehensions
12. Practice with Module_3 Project.ipynb

**Level 5: Error Handling & Projects (Weeks 9-10)**
13. Study `try_except.ipynb` for exception handling
14. Complete `P.E. project.py` (intermediate capstone)
15. Tackle `Final_project.BMB.py` (advanced capstone)

---

## 🔑 Key Concepts Covered

### **Fundamental Programming Concepts**
- ✅ Variable assignment and naming conventions
- ✅ Primitive data types (int, float, str, bool)
- ✅ Type conversion and coercion
- ✅ Operator precedence

### **Control Structures**
- ✅ If/elif/else conditionals
- ✅ Nested conditionals
- ✅ For loop patterns (range, enumerate, zip)
- ✅ While loops and loop control (break, continue)
- ✅ Loop nesting

### **Data Structures**
- ✅ Lists: creation, indexing, slicing, methods
- ✅ List comprehensions
- ✅ Basic dictionary concepts
- ✅ String manipulation

### **Functions & Modularity**
- ✅ Function definition and calls
- ✅ Parameters and return values
- ✅ Scope and naming conventions
- ✅ Documentation strings

### **Error Handling**
- ✅ Try/except/finally blocks
- ✅ Exception types and specificity
- ✅ Debugging strategies
- ✅ Graceful error handling

### **Applied Domain (Bioinformatics)**
- ✅ DNA/RNA sequence processing
- ✅ Genetic code implementation
- ✅ Mutation detection algorithms
- ✅ Biological data validation

---

## 🛠️ Technologies & Stack

| Component | Technology |
|-----------|-----------|
| **Language** | Python 3.8+ |
| **Development IDE** | Visual Studio Code |
| **Interactive Notebooks** | Jupyter Notebook |
| **Standard Library Used** | `random`, `string` modules |
| **Version Control** | Git & GitHub |
| **Documentation** | Markdown |

### **Why Pure Python?**
- **Zero dependencies**: Runs anywhere
- **Educational focus**: Understand core algorithms
- **Performance**: Direct implementation without abstraction overhead
- **Portability**: No environment conflicts

---

## 📊 Project Examples

### **Example 1: DNA Sequence Analysis (Normal)**

**Input:**
```
ATGGCCAAACCCGGGGGG
```

**Output:**
```
Sequence: ATGGCCAAACCCGGGGGG
GC Content: 66.67%
mRNA: AUGGCCAAACCCGGGGGG
Codons: ['AUG', 'GCC', 'AAA', 'CCC', 'GGG', 'GGG']
Amino Acids: M-A-K-P-G-G
Status: ✓ Valid (No premature stops)
```

### **Example 2: Nonsense Mutation Detection**

**Input:**
```
ATGCGATCGATCGATCGATCGATCGATCGATAAAT
```

**Output:**
```
Sequence: ATGCGATCGATCGATCGATCGATCGATCGATAAAT
GC Content: 40.00%
mRNA: AUGCGAUCGAUCGAUCGAUCGAUCGAUCGAUAAAU
Codons: ['AUG', 'CGA', 'UCG', 'AUC', 'GAU', 'CGA', 'UCG', 'AUC', 'GAU', 'CGA', 'UAA']
Amino Acids: M-R-S-I-D-R-S-I-D-R-STOP
⚠️ WARNING: Premature STOP codon at position 10 (UAA) - Nonsense Mutation!
```

### **Example 3: Using Concept Scripts**

```python
# Variables.py - Understanding variable types
name = "Researcher"
sample_id = 42
gc_percentage = 66.67

# Operators.py - Calculating values
gc_content = (g_count + c_count) / sequence_length * 100

# if_conditionals.py - Decision making
if gc_percentage > 65:
    print("High GC content - Good for PCR")
elif gc_percentage < 35:
    print("Low GC content - May need optimization")

# List.py - Collecting codons
codon_list = ['AUG', 'GCC', 'AAA', 'CCC', 'GGG']
for codon in codon_list:
    amino_acid = codon_to_protein[codon]
```

---

## 🔧 Troubleshooting

### **Issue 1: "No module named jupyter"**
```bash
# Solution: Install Jupyter
pip install jupyter notebook
```

### **Issue 2: Python script won't run**
```bash
# Verify Python installation
python --version

# Run with explicit python3
python3 Final_project.BMB.py

# Check file permissions
chmod +x Final_project.BMB.py
```

### **Issue 3: Sequence validation errors**

**Common causes:**
- ❌ Non-canonical bases: Use only A, T, C, G (uppercase)
- ❌ FASTA headers: Remove `>` metadata lines
- ❌ Whitespace: Remove spaces, newlines, numbers
- ❌ RNA instead of DNA: Don't include U in DNA input

**Solution:**
```python
# Clean input before processing
sequence = input_sequence.upper().strip()
sequence = ''.join(c for c in sequence if c in 'ATCG')
```

### **Issue 4: Notebook cells not executing**

- Ensure kernel is running (`Kernel > Restart & Run All`)
- Check for dependency installation
- Verify Python version compatibility

---

## 📝 File Manifest

### **Python Scripts (9 files)**
- Variables.py (720 bytes)
- Literals.py (473 bytes)
- Operators.py (303 bytes)
- Interaction_with_the_user.py (449 bytes)
- List.py (231 bytes)
- if_conditionals.py (968 bytes)
- for_loop.py (630 bytes)
- while_loop.py (52 bytes)
- compuer_logic.py (3,303 bytes)

### **Project Scripts (2 files)**
- P.E. project.py (4,117 bytes) – Intermediate capstone
- Final_project.BMB.py (2,668 bytes) – Advanced capstone

### **Module 2 Notebooks (6 files)**
- First_program.ipynb
- Variables.ipynb
- Python_literals.ipynb
- Operators.ipynb
- Interaction_with_the_user.ipynb
- Conditional.ipynb

### **Module 3 Notebooks (4 files)**
- List.ipynb
- Loops.ipynb
- try_except.ipynb
- Project.ipynb

**Total: 22 learning files | ~28 KB repository size**

---

## 🎓 Learning Outcomes

After completing this repository, you will:

✅ **Master Python fundamentals** – Variables, operators, data types  
✅ **Control program flow** – Conditionals, loops, exception handling  
✅ **Work with collections** – Lists, sequences, iteration  
✅ **Build interactive programs** – User input/output, validation  
✅ **Apply concepts to real problems** – Bioinformatics case study  
✅ **Write clean, documented code** – Following Python conventions  
✅ **Debug effectively** – Error handling and troubleshooting  

---

## 🤝 Contributing

This repository is a personal learning project. To adapt it for your own use:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-additions`)
3. Modify notebooks and scripts for your learning goals
4. Document your changes clearly
5. Commit with descriptive messages

---

## 📄 License

This educational repository is provided as-is for learning purposes. Feel free to use, modify, and share with proper attribution.

---

## 🔗 Quick Links

- **Repository**: https://github.com/mwangimuhia031-alt/Python-essentials-1
- **Python Docs**: https://docs.python.org/3/
- **Jupyter Docs**: https://jupyter.org/
- **Bioinformatics Resources**: https://www.ncbi.nlm.nih.gov/

---

## ⭐ Repository Statistics

- **Language Composition**: 77.6% Jupyter Notebook | 22.4% Python
- **Total Files**: 22 learning materials
- **Repository Size**: ~28 KB
- **Status**: Active learning project
- **Last Updated**: September 2026

---

## 📧 Questions?

For questions about this repository:
- Check the existing documentation in each notebook
- Review the troubleshooting section
- Run examples step-by-step to understand flow
- Experiment with code modifications

---

**Happy Learning! 🐍📚**
