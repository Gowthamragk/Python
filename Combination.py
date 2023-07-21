def generate_subsets(s):
    subsets = []
    generate_subsets_helper(s, "", subsets)
    return subsets

def generate_subsets_helper(s, current_subset, subsets):
    if len(s) == 0:
        subsets.append(current_subset)
        return
    
    generate_subsets_helper(s[1:], current_subset + s[0], subsets)
    
    generate_subsets_helper(s[1:], current_subset, subsets)
input_str = "abc"
result = generate_subsets(input_str)
print(result)
