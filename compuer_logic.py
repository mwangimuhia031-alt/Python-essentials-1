'''

and operator - is a binary operator.
or operator - is also a binary operator with a lower priority than and.
not operator - is a unary operator performing a logical negotiation.
bitwise operators allow manipulation  of single bits of data

they include:
& ampersand
':" | bar
~ tilde
^ caret

read more to grasp the full scope of the computer logic

'''

# =====================================================================
# SECTION 1: LOGICAL OPERATORS (Boolean Decision Making)
# =====================================================================
print("--- SECTION 1: LOGICAL OPERATORS ---")

t = True
f = False

# 1. The 'and' Operator (Binary)
print(f"True and True:   {t and t}")   # True
print(f"True and False:  {t and f}")   # False

# Short-circuit proof for 'and': The function 'spy' is never called because 'f' is False
def spy():
    print("   [SPY] Evaluated!")
    return True

print("Evaluating 'False and spy()':")
result_and = f and spy()  # Stops at 'f'

# 2. The 'or' Operator (Binary - lower priority than 'and')
print(f"False or True:   {f or t}")   # True
print(f"False or False:  {f or f}")   # False

# Short-circuit proof for 'or': Stops at 't' because it's already True
print("Evaluating 'True or spy()':")
result_or = t or spy()   # Stops at 't'

# 3. The 'not' Operator (Unary)
print(f"not True:        {not t}")    # False
print(f"not False:       {not f}")    # True
print()


# =====================================================================
# SECTION 2: BITWISE OPERATORS (Single Bit Manipulation)
# =====================================================================
print("--- SECTION 2: BITWISE OPERATORS ---")

# Let's align 5 (0101) and 3 (0011)
a = 5  # Binary: 0101
b = 3  # Binary: 0011

print(f"Base numbers: a = {a} (binary: {a:04b}), b = {b} (binary: {b:04b})\n")

# 1. & Ampersand (Bitwise AND) - 1 if both bits are 1
# 0101 & 0011 = 0001 (Decimal 1)
print(f"a & b (AND): {a & b:<3} | Binary: {a & b:04b}")

# 2. | Bar (Bitwise OR) - 1 if at least one bit is 1
# 0101 | 0011 = 0111 (Decimal 7)
print(f"a | b (OR):  {a | b:<3} | Binary: {a | b:04b}")

# 3. ^ Caret (Bitwise XOR) - 1 if bits are different
# 0101 ^ 0011 = 0110 (Decimal 6)
print(f"a ^ b (XOR): {a ^ b:<3} | Binary: {a ^ b:04b}")

# 4. ~ Tilde (Bitwise NOT / Unary) - Inverts all bits
# Formula: ~x = -(x + 1) -> ~5 = -(5 + 1) = -6
print(f"~a   (NOT): {~a:<3} | Binary (Two's Complement): {~a:b}")
print()


# =====================================================================
# SECTION 3: PRIORITY HIERARCHY (Order of Operations)
# =====================================================================
print("--- SECTION 3: PRIORITY HIERARCHY ---")

# Bitwise operators (~, &, ^, |) execute BEFORE logical operators (not, and, or)
# Formula: True or False and ~5 & 3 ^ 5 | 3
# Evaluated step-by-step automatically by Python priority rules:
# 1. ~5 -> -6
# 2. &  -> (-6 & 3)
# 3. ^  -> ((-6 & 3) ^ 5)
# 4. |  -> (((-6 & 3) ^ 5) | 3)
# 5. and
# 6. or

complex_expression = True or False and ~5 & 3 ^ 5 | 3
print(f"Result of complex priority chain: {complex_expression}")

# Explicit prioritization using parentheses to show how hierarchy alters flow
forced_expression = (True or False) and (~5 & (3 ^ 5) | 3)
print(f"Result with explicit brackets   : {forced_expression}")
