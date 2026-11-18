"""The problem: convert a Roman numeral string to an integer. The symbols are:

I=1, V=5, X=10, L=50, C=100, D=500, M=1000

Normally you add them (VIII = 5+1+1+1 = 8). But when a smaller symbol comes before a larger one, you subtract it (IV = 4, IX = 9, XL = 40)."""




data = "XXV"
values = {

    "I":1, "V":5, "X":10, "L": 50, "C": 100, "D":500 , "M":1000
}

for s in range(len(data)):
    total = 0
    print(data[s])
    current = values[data[s]]

    if s+1 < len(data) and current < values[data[s+1]]:
        total = total - current
           
        total = total + current
print(total)

