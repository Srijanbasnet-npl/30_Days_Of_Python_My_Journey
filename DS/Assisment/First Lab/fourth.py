# Program to check if a function is injective, surjective, bijective,
# and to compute its inverse if it is bijective.

# Given function: f: {1, 2} -> {10, 20}
# f(1) = 10, f(2) = 20

function = {1: 10, 2: 20}
domain = {1, 2}
codomain = {10, 20}

values = list(function.values())

injective = len(set(values)) == len(values)
surjective = set(values) == codomain
bijective = injective and surjective

print("Function:", function)
print("Domain:", domain)
print("Codomain:", codomain)
print("Injective:", injective)
print("Surjective:", surjective)
print("Bijective:", bijective)

if bijective:
    inverse = {v: k for k, v in function.items()}
    print("Inverse function:", inverse)
else:
    print("Inverse function does not exist because the function is not bijective.")
