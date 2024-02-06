def count_lengths(items):
    return [len(str(element)) for element in items]

# Example usage:
str_array = ["abc", "apple", "orange"]
int_array = [12, 456, 9000]

output_str = count_lengths(str_array)
output_int = count_lengths(int_array)

print("Input:", str_array)
print("Output:", output_str)
print("Input:", int_array)
print("Output:", output_int)
