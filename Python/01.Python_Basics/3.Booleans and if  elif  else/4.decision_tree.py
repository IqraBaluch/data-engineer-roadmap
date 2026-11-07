"""
Build a tiny text “decision tree” that tells you which storage to use for data. 
 It uses nested ifs, which means an if inside another if.

Is the data in tables (structured)?
 ├─ yes → Is it more than 1 TB?
 │         ├─ yes → "Use a data warehouse (like Snowflake)"
 │         └─ no  → "Use a regular database (like SQL Server)"
 └─ no  → "Use a data lake (files in storage)"

Your steps:

Plan in comments first: restate, examples, plan.
Store the answers in variables at the top:



"""

"""Write the nested if / else for the tree.
Test all 3 results by changing the variables.
Bonus: make it interactive with input(). 
For example, answer = input("Is the data structured? 
(yes/no): ") gives you the text the user typed, 
and you compare it with answer == "yes".


        Is it structured?          ← the "root" (the first question)
         /            \
       yes             no          ← branches
       /                \
 More than 1 TB?      Data lake    ← leaf (a final answer)
   /        \
 yes         no
  |           |
Warehouse   Database               ← leaves



"""


is_structured = True
more_than_1tb = True

if is_structured:
    if more_than_1tb:
        print("Warehouse")
    else:
        print("Database")
else:
    print("Data lake")