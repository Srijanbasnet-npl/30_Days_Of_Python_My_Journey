def power_set(input_set):
    """Return all subsets of a given set."""
    items = sorted(input_set)
    subsets = [[]]

    for item in items:
        subsets += [subset + [item] for subset in subsets]

    return subsets


# Example usage
my_set = {1, 2, 3}
result = power_set(my_set)
print("Power set of", my_set, "is:")
for subset in result:
    print(subset)
