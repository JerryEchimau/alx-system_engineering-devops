# 0x02. Shell, I/O Redirections and filters

- In this project, we learnt about shell redirection to and from  the output and input stream
- i.e ``>`` directs output to a stream (file or standard output) and ``<`` takes input from the stream (i.e file) <br>

Here are the tasks in this project <br>

## Tasks:clipboard:
### 0. Hello World
- one can use ``echo`` with ``-e`` option that allows it to inteprete the backlash(\) or ``printf`` which simply intepretes the ``\n``

### 1. Confused smiley
- This can be achieved by using escape backlash ``\`` with the ``echo`` command to include literal double quotes within the double quotes that indicate the beginning and end of a string

### 2. Let's display a file
- we use ``cat`` (concatenate) to display contents of a file

### 3. What about 2?
- For this one, just add files and ``cat`` will display the contents of each

### 4. Last lines of a file
- use ``tail`` command to display the contents of a file (last 10 as default)

### 5. I'd prefer the first ones actually
- use ``head`` command to disp;ay the contents of a file (first 10 lines as default)

### 6. Line #2
- For this one, we use the ``head`` command and ``-n`` to specify number of lines as 3 then pipeline the product to ``tail`` command and specify ` line to display only line 3

### 7. It is a good file that cuts iron without making a noise
- For this one, we write the contents using ``echo`` command then redirect its output (using >) to a file (*\\'"Best School"\'\\*$\?\*\*\*\*\*:))
- for the file, we use \\ (double backlash) to ignore a preceding backlash (i.e to print one \, we use \\\)
- together with other rules, this is the code for this task ``echo "Best School" > \\\*\\\\"'\"Best School\"\\'"\\\\\*\$\\\?\\\*\\\*\\\*\\\*\\\*\:\)``

### 8. Save current state of directory
- Here, we use the > to output the contents of a command to a file without appending

### 9. Duplicate last line
- Here, we just append the last line of the file onto itself
- we first use ``tail`` to access the last line and then output to the file using >> that appends to the file

### 10. No more javascript
- we use the ``find`` feature to find all files (specify using -f argument) in the current dir and its subdirs (use the name argument to find and the delete argument)

### 11. Don't just count your directories, make your directories count
- Here, we use the ``find`` feature and specify type as directory (-d)
- pipeline to ``wc`` command (wordcount) per line

### 12. What’s new
- Here, we list the files with ``-t`` (time) argument to ``ls`` to display newest to oldest
- we then pipeline this to ``head`` in order to list the first 10

### 13. Being unique is better than being perfect
- For this one, sort the list and use ``uniq`` command to print unique lines

### 14. It must be in that file
- use the ``grep`` command with the pattern

### 15. Count that word
- We can either use -c argument to ``grep`` to count lines
- or pipeline the contents of ``grep`` to ``wc`` with a -n option for counting number of lines

### 16. What's next?
- ``grep`` also has a 'lines of context' feature that displays a number of lines after the specified pattern to reveal the context
- This is enabled by option -A (after)

### 17. I hate bins
- grep also has an 'invert match' feature that outputs everything that doesn't match the pattern
- achieved using -v option

### 18. Letters only please
- use the ``[[:alpha:]]`` argument to ``grep``

### 19. A to Z
- Replacing can be done using ``tr`` with te following syntax: ``tr [what_to_replace] [what_to_replace_with]``
- This will be done respectively (i.e first in 'what to replace' will be replaced with the first char in 'what to replace with')

### 20. Without C, you would live in hiago
- we can use the ``tr`` feature with a -d option that deletes the specified pattern

### 21. esreveR
- ``rev`` revreses the inout text

### 22. DJ Cut Killer
- Here, we will use a combination of ``cat`` to list, ``cut`` to remove sections from each line, and ``sort`` to sort the output
- for the ``cut``, we will need to use a delimiter function and find where usernames and their Home dir are located in order to cut the rest of the info
