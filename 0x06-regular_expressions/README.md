# 0x06. Regular expression

- In this project, we learnt about regular expressions and how to use them using Ruby's Oniguruma library
- Here are the tasks in this project

## Tasks :clipboard:

### 0. Simply matching School

- Here, simply put the words ``School`` within the //
- This matches the regular expression "School" in any text

### 1. Repetition Token #0

- Here, we use the quantifier ``{n,m}`` to match t from range 2 to 5

### 2. Repetition Token #1

- Here, we use the quantifier ``?``, which means it will match zero or one occurrence of the preceding element.

### 3. Repetition Token #2

- Here, we use the quantifier ``+`` , which means that it will match 1 or more occurences of the preceding element

### 4. Repetition Token #3

-here, we use the quantifier ``*``, which means that it will match 0 or more occurences of the preceding element

### 5. Not quite HBTN yet

- here, we use ``^`` to match the beginning of a string and ``$`` to match the end
- We then use ``.`` in between ``h`` and ``n`` to match any character except newline

### 6. Call me maybe

- Here, we use ``^`` and ``$`` to only take in digits from the beginning to end and nothing else
- We also use ``\d`` to match digits and use quatifiers ``{n,m}`` to limit to 10 digits