# Detailed schedule and resources

## Class 12

Announcements:
* The reading for Monday is available on the Readings page.
* Updated version of HW4 is available (same questions, but with
  some additional hints and clarifications).
  
Topics for today's class:
* Overview of how to book an appointment with a QR tutor at the [QR
  center](https://www.dickinson.edu/info/20525/quantitative_reasoning_center/2962/quantitative_reasoning_center).
* Informal discussion of the *scope* of a variable: most variables and
  parameters are *local*.
* Review of call stack and debugging.
* Printing on the same line from multiple `print()` statements.
* Review of void and fruitful functions.


## Class 11

Demo code: [debug_demo.py](class11/debug_demo.py), [callstack_demo.py](class11/callstack_demo.py)


## Class 10

Social/Ethical discussion I. See Readings web page.

## Class 9

Mostly review of chained and nested conditional statements. 
We want to write a function `decide(hungry, tired)` that prints output according to

|             |  hungry     | not hungry   |
|-------------|-------------|--------------|
|**tired**    |get takeout  | sleep        |
|**not tired**|cook dinner  | watch Netflix|

Example code: (try to figure out for yourself?) [decide.py](class09/decide.py)

Also Boolean variables and parameters -- see SSG11.

## Class 8

We cover cascading conditional statements and nested conditional
statements. Example Python code: [convert_miles2.py](class08/convert_miles2.py)

We will also go over sections 8 to 10 of the supplementary study
guide, which are needed for lab this afternoon.

Please take a look at the extra question that is in the solutions of
homework assignment 2. You need to understand how to answer this type
of question (distinguishing between function calls in a module and
method calls on an object).


## Class 7

Today we cover topics from the assigned textbook reading, including
floor division and modulus, boolean expressions, relational operators
(`==`, `!=`, `>`, `>=` etc.), logical operators (`and`, `or`, `not`),
conditional execution (`if`, `else`).

Example Python code (but try to do the warmup exercise yourself before
looking at this): [convert_miles.py](class07/convert_miles.py), [boolean_demos.py](class07/boolean_demos.py)

Optional: A "real" example of using conditionals, using the Scratch
programming language: [Potion making](https://scratch.mit.edu/projects/889677445), by Scratch user [cc196](https://scratch.mit.edu/users/cc196/). Click on "See inside" then "Backdrops 1" to see a lot of nested `if/else`s


## Class 6

Today we cover Sections 4-7 of the supplementary study guide: nested
`for` loops; constructors; `graphics.py`; methods and dot notation.

Just for interest: if you want to find out about one of the areas of
computer science that I'm interested in, check out today's episode
(September 8) of a radio show called The Academic Minute, which is
broadcast on about 70 radio stations in North America. It's also
available as a podcast: [The Academic Minute NPR
podcast](https://www.npr.org/podcasts/564572329/the-academic-minute)

Code from class (slightly improved version compared to what was shown
in class): [graphics_demo.py](class06/graphics_demo.py)


## Class 5

Agenda for today's class:
1. We'll go over the supplementary study guide content about `for`
   loops, which explains how to use the loop variable.
2. We'll begin working through the textbook exercises in section 4.3.

Useful tip: Learn how to use IDLE's Indent Region and Dedent Region
features, in the Format menu.


## Class 4

Important note about the teaching style in this course: Many concepts
will not be covered during our lecture session. It is essential to
read the textbook carefully and ask questions on any content you don't
understand. For example, the assigned reading for Class 3 included the
important concept of *string concatenation*, but we did not discuss
that during class.

New link on main homepage: supplementary study guide.

Plan for today: We will go over some key concepts from the assigned
reading, especially how to define new functions and how to generate
random numbers.

Note that for section 13.2, you are not expected to understand all of
this content. The only things we need from this section are:
* `import random`
* `random.randint()`

#### Hopefully you will never need this advice, but just in case...

1. At the end of class, we saw a mysterious "unexpected indent" error
   from IDLE. Usually, this is caused by indenting your code
   incorrectly. However, it can also be caused by certain invisible
   characters in the Python file. Different computer systems use
   different specialized characters for representing the end of a
   line, and it is possible for IDLE to report these characters as
   causing an indentation error. One easy way to remove all unwanted
   end-of-line characters is to copy and paste your code into this
   [end-of-line fixer website](https://ryanve.dev/eol/). Click
   "Convert line endings to LF", copy the output into a new file, and
   now the weird characters have been removed from your Python script.

2. I have also occasionally seen the presence of certain invisible
   characters prevent IDLE from saving a file. If IDLE refuses to
   save, you should create a new file and paste your code into it
   after following step 1 above to ensure that any weird invisible
   characters have been removed.



## Class 3

* Make sure that you have Show File Extensions turned on in your
  operating system. For example, you must be able to see the `.py` at
  the end of your Python files, when browsing folders.
* When opening a Python file, do not just double-click on it in the
  folder view. First open the IDLE application, then use the Open
  command in the File menu.
  
Today we review the concepts in the assigned reading, including script mode, order of operations, string operations, comments, function calls, and math functions.

Example programs: [area.py](class03/area.py), [ask_question.py](class03/ask_question.py)


## Class 2

We will review the concepts in the assigned reading, then look ahead
to some things needed in the afternoon lab: commenting out code; the
distinction between executing code via the console and running Python
scripts.

Here are a couple of clarifications of the assigned reading material:
* In this course, we use Python 3 (not Python 2), the same as
  recommended by the textbook.
* For running Python in a web browser, the textbook author recommends
  [pythonanywhere.com](https://www.pythonanywhere.com/). Another good
  option is [replit.com](https://replit.com), which we played around
  with in the last class meeting.
* *However*, in this course we will mostly be learning to write
  programs using files on our own computer and running Python on our
  own computer (not in the cloud inside a web browser). For this, you
  should use the IDLE editor. This comes bundled with a standard
  Python download, which is available at
  [python.org](https://www.python.org/)

Pair programming will be discussed if we have time, otherwise we can
talk about it in lab. Key ideas:
* There are two roles, *driver* and *navigator*. The driver uses the
  keyboard and mouse to write and run code, whereas the navigator
  assists by making suggestions.
* You must switch roles at least every 30 minutes.


## Class 1

* We will play around a little on [replit.com](https://replit.com),
  but this will mostly be an informal introduction to the course.
* Please read the syllabus carefully and bring any questions to the
  next class.
* Note the required reading: complete this before the next class.
* Note when the first homework assignment is due. 
* Finally, don't forget we have a lab on Wednesday at 3 PM.



---- Last modified: Fri Sep 22 11:20:53 UTC 2023 by jmac.
