a = "level"

b = a.lower()

def reverse(a):
    b = a.lower()
    if b == " ":
        return "empty string"
    elif b == b[::-1]:
        return True
    else:
        return False

print(reverse("level"))

assert reverse("python") == False
assert reverse("level") == True
assert reverse(" ") == "empty string"
