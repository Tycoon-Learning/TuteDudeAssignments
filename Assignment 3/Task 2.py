import math

# Get user input
number = float(input("Enter a number: "))

# Calculate values using math module
square_root = math.sqrt(number)
natural_log = math.log(number)
sine_value = math.sin(number)  # Input is treated as radians

# Display results
print(f"\nCalculations for {number}:")
print(f"Square root: {square_root:}")
print(f"Natural logarithm: {natural_log:}")
print(f"Sine (radians): {sine_value:}")