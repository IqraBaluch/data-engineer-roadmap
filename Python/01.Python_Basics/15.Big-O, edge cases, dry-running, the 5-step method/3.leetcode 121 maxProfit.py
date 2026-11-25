# LeetCode 121: Best Time to Buy and Sell Stock
# Idea: keep the lowest price so far; each day ask if selling today beats the best profit.
# Time: O(n), one loop over the prices
# Space: O(1), only the lowest price and the profit are stored

# a = [23,45,2,33,6]

# best_val = a[0]
# profit = 0
# best_index =  0

# for i in range(len(a)):
#     #print(a[i])
#     #print("buy: ",a[i], "day:", i)
#     if best_val > a[i]:
#         best_val = a[i]
#     if profit < a[i]:
#         profit = a[i]-best_val
#         print(profit,i)
#         best_index = i
    
# print(best_val)
# print(best_index)


# def maxProfit(a):

#     if len(a)==0:
#         return 0
    
#     best_buy_day = a[0]
#     best_sell_day_ind =0
#     profit = 0

#     for i in range(len(a)):
        

#         if best_buy_day > a[i]:
#             best_buy_day = a[i]

#         if a[i]-best_buy_day>profit:
#             profit = a[i]-best_buy_day
#             best_sell_day_ind = i
#             return 
       



#     return profit

# print(maxProfit([23,45,2,33,6]))
# assert maxProfit([2,2,2,2,2,2]) == 0
# assert maxProfit([]) == 0
# assert maxProfit([23,45,2,33,6]) == 2


def maxProfit(a):

    if len(a)==0:
        return 0
    
    best_buy_day = a[0]
    profit = 0

    for i in range(len(a)):
        

        if best_buy_day > a[i]:
            best_buy_day = a[i]

        if a[i]-best_buy_day>profit:
            profit = a[i]-best_buy_day


    return profit

print(maxProfit([23,45,2,33,6]))
assert maxProfit([2,2,2,2,2,2]) == 0
assert maxProfit([]) == 0
assert maxProfit([23,45,2,33,6]) == 31

