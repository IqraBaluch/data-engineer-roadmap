"""The problem: convert a Roman numeral string to an integer. The symbols are:

I=1, V=5, X=10, L=50, C=100, D=500, M=1000

Normally you add them (VIII = 5+1+1+1 = 8). But when a smaller symbol comes before a larger one, you subtract it (IV = 4, IX = 9, XL = 40)."""




s = "MCMXCIV"
values = {

    "I":1, "V":5, "X":10, "L": 50, "C": 100, "D":500 , "M":1000
}
total =0

for i in range(len(s)):
    if i+1 < len(s) and values[s[i]] < values[s[i+1]]:
        total -= values[s[i]]
    else:
        total += values[s[i]]
print(total)