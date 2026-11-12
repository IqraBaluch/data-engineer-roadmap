# a list can be changed in place

names = ["Sara", "Ali", "Noor"]

names.append("Zain")        # add at the end        → ["Sara","Ali","Noor","Zain"]
names.insert(0, "Hina")     # add at position 0     → ["Hina","Sara","Ali","Noor","Zain"]
names.remove("Ali")         # remove by value       → ["Hina","Sara","Noor","Zain"]
last = names.pop()          # remove the LAST and give it back → last is "Zain"
names[0] = "Maha"           # replace the item at position 0

print(names)

# example

nums = [10, 20, 30]
nums.append(40)
print(nums)
nums.insert(1, 15)
print(nums)
nums.remove(30)
print(nums)
nums[0] = 5
print(nums)
