# #1281. The question, as an interviewer would ask it:

"""“Given an integer n, return the difference between the product of its digits and the sum of its digits.”

Example: n = 234 → product 2 × 3 × 4 = 24, sum 2 + 3 + 4 = 9, and the answer is 24 - 9 = 15."""

# n = 50
total = 0
product = 1

while n > 0:

    num = n % 10
    total = num +total
    product = product * num
    
    n = n // 10
    
print(total - product)


# convert it into function for resuablity 
def product_and_sum_num(n):
    total = 0
    product = 1
    while n > 0:
        num = n % 10
        total = num + total
        product = num*product

        n = n // 10

    return product - total

print(product_and_sum_num(23))



