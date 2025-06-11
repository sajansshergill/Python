# Mini Voting System for Favorite Programming Languages

"""
💡 Project Features
1. Register votes
Ask 4 users (or more) to enter their name and favorite programming language.

Use a dictionary to store:
{ "Alice": "Python", "Bob": "JavaScript", ... }

2. Handle Duplicate Keys
If a name already exists in the dictionary, notify the user that their vote has been updated.

3. Display all unique languages voted for
Use a set to store only unique language names.

4. Compare popularity
Accept two different language names from user and check:

Whether both were voted for (using intersection)

Whether one is a subset/superset of another (bonus use of issubset/issuperset)

5. Copy and Reset Function
Let the user copy() the dictionary or clear() it after voting ends.
"""

