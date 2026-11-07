"""

1. Restate: messy name in, clean "Ali Raza" out.
2. Example: "  aLi  rAZA " -> "Ali Raza"
3. Plan:
   - strip the spaces at the ends
   - lower everything
   - split into words (no argument, so it ignores extra spaces)
   - capitalise each word
   - join the words with one space
4. Code: (write below each comment)
5. Test: run it with the example.

"""

name = '  aLI rAZA  '

#strip the spaces at the ends
name = name.strip()

#lower everything
name = name.lower()

#split into words (no argument, so it ignores extra spaces)
word = name.split()

clean = " ".join(word)
clean_name = clean.title()
print(clean_name)


