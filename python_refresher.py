def clamp(value, min_val, max_val):
    """Restricts a value to be within the range [min_val, max_val]."""
    if value < min_val:
        return min_val
    if value > max_val:
        return max_val
    return value

def mean(numbers):
    """Calculates the arithmetic mean (average) of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate the mean of an empty list.")
    return sum(numbers) / len(numbers)

def is_close(a, b, rel_tol=1e-9, abs_tol=0.0):
    """
    Checks if two floating-point numbers are approximately equal.
    This mimics Python's built-in math.isclose().
    """
    return abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

# --- Tests using assert statements ---

# 1. Tests for clamp
assert clamp(5, 1, 10) == 5, "5 is within the range, should return 5"
assert clamp(-2, 0, 100) == 0, "-2 is below the min, should return 0"
assert clamp(200, 0, 100) == 100, "200 is above the max, should return 100"

# 2. Tests for mean
assert mean([1, 2, 3, 4, 5]) == 3.0, "Mean of 1..5 should be 3.0"
assert mean([10, 20, 30]) == 20.0, "Mean of 10, 20, 30 should be 20.0"

# 3. Tests for is_close
assert is_close(0.1 + 0.2, 0.3) == True, "0.1 + 0.2 should be close to 0.3"
assert is_close(1.0001, 1.0, rel_tol=1e-5) == False, "1.0001 is not close to 1.0 with strict tolerance"

if __name__ == "__main__":
    print("All tests passed successfully!")