# Program to find the sum of the first n terms of an arithmetic series

first_term = 2
common_difference = 4
number_of_terms = 20

sum_of_terms = (number_of_terms / 2) * (2 * first_term + (number_of_terms - 1) * common_difference)

print("The sum of the first 20 terms is:", int(sum_of_terms))
