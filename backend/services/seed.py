from sqlalchemy.orm import Session
from models import World, Lesson


WORLDS_DATA = [
    {
        "number": 1,
        "title": "Hello World",
        "description": "Start your adventure! Learn to make the computer talk.",
        "icon": "👋",
        "color": "#6366f1",
        "lessons": [
            {
                "order": 1,
                "title": "Your First Program",
                "description": "Make the computer say Hello World!",
                "theory": """\
🖥️  WHAT IS A COMPUTER PROGRAM?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
A program is a list of instructions for the computer.
The computer reads them one by one, top to bottom,
and does exactly what you tell it — no more, no less!

C is one of the oldest and most powerful programming
languages in the world. Video games, robots and apps
are built with it!

📄  THE STRUCTURE OF EVERY C PROGRAM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Every C program has this shape:

    #include <stdio.h>

    int main() {
        /* your code goes here */
        return 0;
    }

Let's understand each part:

  #include <stdio.h>  →  Loads printing tools
                         (stdio = Standard Input/Output)

  int main() { }     →  The program starts here.
                         main is the first thing that runs.

  return 0;          →  Tells the computer "finished, no errors!"

🖨️  PRINTING TEXT WITH printf()
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Use printf() to show text on the screen:

    printf("Hello, World!");

⚠️  Remember:
  • Text goes inside " double quotes "
  • Every statement ends with a semicolon  ;
  • printf() goes INSIDE the { } of main""",
                "starter_code": '#include <stdio.h>\n\nint main() {\n    // Write your code here\n    \n    return 0;\n}\n',
                "expected_output": "Hello, World!",
                "hint": "Use printf(\"Hello, World!\\n\"); inside main()",
                "xp_reward": 50,
                "is_final_project": False,
            },
            {
                "order": 2,
                "title": "Print Your Name",
                "description": "Make the computer print your name on a new line!",
                "theory": """\
🔤  ESCAPE SEQUENCES — SPECIAL CODES INSIDE TEXT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Sometimes you need special characters inside your text.
You write them with a backslash \\ followed by a letter:

    \\n   →  new line (go to the next line)
    \\t   →  tab (add some space / indent)
    \\\\  →  print a real backslash \\
    \\"   →  print a real quote mark "

Example:

    printf("Line 1\\nLine 2\\n");

Output:
    Line 1
    Line 2

The \\n at the end is important! Without it, the next
printf() will print right after on the same line.

🔁  USING printf() MULTIPLE TIMES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
You can use printf() as many times as you want:

    printf("Hello!\\n");
    printf("I am learning C!\\n");
    printf("This is fun!\\n");

Each call continues from where the last one ended.

Output:
    Hello!
    I am learning C!
    This is fun!""",
                "starter_code": '#include <stdio.h>\n\nint main() {\n    printf("Hello, World!\\n");\n    // Now print your name below\n    \n    return 0;\n}\n',
                "expected_output": "Hello, World!\nMy name is CQuest!",
                "hint": "Add another printf() with your name. Use \\n for a new line!",
                "xp_reward": 50,
                "is_final_project": False,
            },
            {
                "order": 3,
                "title": "Hello World Challenge",
                "description": "Final challenge: Print 3 lines - Hello!, Welcome to CQuest!, and Let's code!",
                "theory": """\
📝  REVIEW — WHAT YOU'VE LEARNED SO FAR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✔  Every program needs #include <stdio.h> at the top
✔  The program starts inside int main() { }
✔  printf("text") shows text on screen
✔  \\n creates a new line
✔  Every statement ends with ;

🏆  COMBINING MULTIPLE printf() CALLS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
To print 3 separate lines, use 3 printf() calls,
each one ending with \\n:

    printf("Line 1\\n");
    printf("Line 2\\n");
    printf("Line 3\\n");

Output:
    Line 1
    Line 2
    Line 3

⚠️  COMMON MISTAKES TO AVOID
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✗  Forgetting the semicolon at the end
  ✗  Using single quotes ' instead of double quotes "
  ✗  Forgetting \\n when you want a new line
  ✗  Writing printf without the #include <stdio.h>

You've got this! 💪""",
                "starter_code": '#include <stdio.h>\n\nint main() {\n    // Print Hello!\n    \n    // Print Welcome to CQuest!\n    \n    // Print Let\'s code!\n    \n    return 0;\n}\n',
                "expected_output": "Hello!\nWelcome to CQuest!\nLet's code!",
                "hint": "You need 3 printf() calls, one for each line!",
                "xp_reward": 100,
                "is_final_project": True,
            },
        ],
    },
    {
        "number": 2,
        "title": "Variables",
        "description": "Store information in boxes called variables!",
        "icon": "📦",
        "color": "#8b5cf6",
        "lessons": [
            {
                "order": 1,
                "title": "Integer Variables",
                "description": "Create a variable to store the number 12 and print it!",
                "theory": """\
📦  WHAT IS A VARIABLE?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
A variable is like a labeled box where you store data.
You give it a name and put a value inside.

    [ box named "age" ]  →  stores the value  12

In C, you must tell the computer WHAT TYPE of data
you want to store before you can use a variable.

🔢  THE int TYPE — WHOLE NUMBERS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
int stores whole numbers (no decimals): 0, 1, -5, 100...

    int age = 12;       ←  create a box called "age", put 12 inside

To print an int, use %d inside printf():

    printf("My age is %d", age);
    Output:  My age is 12

%d is a placeholder — the computer replaces it
with the value of the variable you give at the end.

⚠️  RULES FOR VARIABLE NAMES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  • Use letters, numbers and underscores _
  • Cannot start with a number
  • No spaces allowed!
  ✔  score, myAge, level_1
  ✗  1score, my age

🔑  ALWAYS DECLARE BEFORE USE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    int age = 12;          ←  first: declare and assign
    printf("%d", age);     ←  then: use it""",
                "starter_code": '#include <stdio.h>\n\nint main() {\n    // Create an int variable called age with value 12\n    \n    // Print it using printf and %d\n    \n    return 0;\n}\n',
                "expected_output": "My age is 12",
                "hint": "Use int age = 12; then printf(\"My age is %d\", age);",
                "xp_reward": 50,
                "is_final_project": False,
            },
            {
                "order": 2,
                "title": "Float Variables",
                "description": "Store the number 9.99 in a float variable and print it!",
                "theory": """\
🔢  THE float TYPE — DECIMAL NUMBERS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
float stores numbers with a decimal point:
    3.14,  9.99,  -0.5,  100.0

    float price = 9.99;

To print a float, use %f inside printf():

    printf("Price: %f", price);
    Output:  Price: 9.990000   ← lots of unwanted zeros!

🎯  CONTROLLING DECIMAL PLACES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Use %.2f to show exactly 2 decimal places:

    printf("Price: %.2f", price);
    Output:  Price: 9.99

The number between . and f controls how many decimals:
    %.0f  →  no decimals     (10)
    %.1f  →  1 decimal       (9.9)
    %.2f  →  2 decimals      (9.99)
    %.4f  →  4 decimals      (9.9900)

📊  int vs float — QUICK COMPARISON
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    int score = 95;        →  whole number,   use %d
    float price = 9.99;    →  decimal number, use %f or %.2f

Use int when you don't need decimals.
Use float when you do!""",
                "starter_code": '#include <stdio.h>\n\nint main() {\n    // Create a float called price with value 9.99\n    \n    // Print: Price: 9.99\n    \n    return 0;\n}\n',
                "expected_output": "Price: 9.99",
                "hint": "Use float price = 9.99; and printf(\"Price: %.2f\", price);",
                "xp_reward": 50,
                "is_final_project": False,
            },
            {
                "order": 3,
                "title": "Adding Numbers",
                "description": "Create two variables, add them, and print the result!",
                "theory": """\
➕  ARITHMETIC OPERATORS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
In C you can do math with variables using these symbols:

    +   addition         5 + 3  =  8
    -   subtraction      5 - 3  =  2
    *   multiplication   5 * 3  =  15
    /   division         10 / 2 =  5
    %   modulo (rest)    7 % 3  =  1

💡  HOW TO STORE AND PRINT A RESULT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    int a = 10;
    int b = 5;
    int sum = a + b;           ←  calculate and store result

    printf("%d + %d = %d", a, b, sum);
    Output:  10 + 5 = 15

You can use multiple %d placeholders — add the variables
at the end in the same order:

    printf("%d + %d = %d", a, b, sum);
              ↑       ↑       ↑
              a       b       sum

⚠️  INTEGER DIVISION — WATCH OUT!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
When you divide two ints, the result is also an int:
    7 / 2  =  3   (NOT 3.5 — the decimal is cut off!)

Use float if you need the decimal part:
    float result = 7.0 / 2.0;   →  3.5""",
                "starter_code": '#include <stdio.h>\n\nint main() {\n    int a = 10;\n    int b = 5;\n    // Calculate the sum and store it\n    \n    // Print: 10 + 5 = 15\n    \n    return 0;\n}\n',
                "expected_output": "10 + 5 = 15",
                "hint": "int sum = a + b; then use three %d in printf for a, b, and sum",
                "xp_reward": 75,
                "is_final_project": False,
            },
            {
                "order": 4,
                "title": "Variables Challenge",
                "description": "Final challenge: Calculate area of a rectangle (width=8, height=5) and print it!",
                "theory": """\
🏋️  PUTTING IT ALL TOGETHER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
You now know:
  ✔  int and float to store numbers
  ✔  %d and %.2f to print them
  ✔  +  -  *  /  to do math with them

📐  AREA OF A RECTANGLE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Area = width × height

In C, the multiplication symbol × is written as  *  :

    int width = 8;
    int height = 5;
    int area = width * height;    ←  8 * 5 = 40

    printf("Area = %d", area);
    Output:  Area = 40

🧩  STEP-BY-STEP APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Variables are already given: width = 8, height = 5
  2. Calculate:  int area = width * height;
  3. Print:      printf("Area = %d", area);

🔑  KEY HABIT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Always store the result of a calculation in a new variable
before printing it. This makes your code easier to read!""",
                "starter_code": '#include <stdio.h>\n\nint main() {\n    int width = 8;\n    int height = 5;\n    // Calculate area\n    \n    // Print: Area = 40\n    \n    return 0;\n}\n',
                "expected_output": "Area = 40",
                "hint": "Multiply width * height and store in int area, then print!",
                "xp_reward": 100,
                "is_final_project": True,
            },
        ],
    },
    {
        "number": 3,
        "title": "If / Else",
        "description": "Teach your program to make decisions!",
        "icon": "🔀",
        "color": "#ec4899",
        "lessons": [
            {
                "order": 1,
                "title": "Simple If",
                "description": "Check if a number is positive and print a message!",
                "theory": """\
🤔  WHAT IS A CONDITION?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
A condition is a question with a YES or NO answer:
  "Is 10 greater than 5?"   →  YES ✔
  "Is 3 equal to 7?"        →  NO  ✗

In programming:  YES = true   NO = false

🔀  THE if STATEMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
if runs a block of code ONLY when the condition is true:

    if (condition) {
        /* runs only if condition is TRUE */
    }

Example:
    int score = 75;
    if (score > 50) {
        printf("You passed!");    ←  runs because 75 > 50 = TRUE
    }

If score were 30, the printf would NOT run (30 > 50 = FALSE).

📏  COMPARISON OPERATORS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    >    greater than          5 > 3   ✔
    <    less than             2 < 8   ✔
    >=   greater or equal      5 >= 5  ✔
    <=   less or equal         3 <= 4  ✔
    ==   exactly equal         7 == 7  ✔   (TWO equals signs!)
    !=   not equal             4 != 9  ✔

⚠️  CRITICAL DIFFERENCE:
    =   assigns a value    (int x = 5)
    ==  compares values    (x == 5)""",
                "starter_code": '#include <stdio.h>\n\nint main() {\n    int score = 75;\n    // If score is greater than 50, print "You passed!"\n    \n    return 0;\n}\n',
                "expected_output": "You passed!",
                "hint": "Use if (score > 50) { printf(\"You passed!\"); }",
                "xp_reward": 50,
                "is_final_project": False,
            },
            {
                "order": 2,
                "title": "If Else",
                "description": "Print 'Even' if number is even, 'Odd' if not!",
                "theory": """\
🔀  THE else BRANCH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
else runs when the if condition is FALSE.
Think of it as the "otherwise" option:

    if (condition) {
        /* runs when TRUE  */
    } else {
        /* runs when FALSE */
    }

Example:
    int x = 3;
    if (x > 10) {
        printf("Big");
    } else {
        printf("Small");     ←  this runs, because 3 > 10 = FALSE
    }

Only ONE branch ever runs — never both!

➗  THE MODULO OPERATOR  %
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
% gives the REMAINDER of a division:

    7 % 2 = 1    (7 ÷ 2 = 3, remainder 1)
    6 % 2 = 0    (6 ÷ 2 = 3, remainder 0)
    9 % 4 = 1    (9 ÷ 4 = 2, remainder 1)
   12 % 5 = 2    (12 ÷ 5 = 2, remainder 2)

🔑  TRICK: Even or Odd?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
A number is EVEN if dividing by 2 leaves no remainder:

    if (number % 2 == 0) {
        printf("Even");
    } else {
        printf("Odd");
    }""",
                "starter_code": '#include <stdio.h>\n\nint main() {\n    int number = 7;\n    // Check if even or odd\n    \n    return 0;\n}\n',
                "expected_output": "Odd",
                "hint": "Use number % 2 == 0 to check if even. 7 % 2 = 1 (not zero = odd)",
                "xp_reward": 75,
                "is_final_project": False,
            },
            {
                "order": 3,
                "title": "If Else If",
                "description": "Grade checker: score 90+ is A, 70+ is B, otherwise C!",
                "theory": """\
🔀  CHAINING CONDITIONS WITH else if
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
When you have more than 2 options, use else if:

    if (first condition) {
        ...
    } else if (second condition) {
        ...
    } else if (third condition) {
        ...
    } else {
        /* when none of the above are true */
    }

The computer checks conditions from TOP to BOTTOM
and stops at the FIRST one that is true!

📝  GRADE EXAMPLE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    int score = 85;

    if (score >= 90) {
        printf("A");         ←  85 >= 90? NO → skip
    } else if (score >= 70) {
        printf("B");         ←  85 >= 70? YES → print B, stop!
    } else {
        printf("C");         ←  never reached
    }

🔑  KEY RULE — MOST SPECIFIC FIRST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Always put the STRICTEST condition first!

❌  Wrong order (score 95 would print B instead of A!):
    if (score >= 70) { printf("B"); }     ← 95 >= 70 = true!
    else if (score >= 90) { printf("A"); }

✔  Correct order:
    if (score >= 90) { printf("A"); }     ← 95 >= 90 = true ✔
    else if (score >= 70) { printf("B"); }""",
                "starter_code": '#include <stdio.h>\n\nint main() {\n    int score = 85;\n    // Print the grade: A, B, or C\n    \n    return 0;\n}\n',
                "expected_output": "Grade: B",
                "hint": "85 is >= 70 but not >= 90, so it should print B",
                "xp_reward": 75,
                "is_final_project": False,
            },
            {
                "order": 4,
                "title": "Decisions Challenge",
                "description": "Final challenge: Check if age (set to 15) is old enough to drive (need 18+)!",
                "theory": """\
🧠  REVIEW — DECISIONS IN C
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
You now know three tools for making decisions:

    if (x > 0) { ... }
      ↑ runs when condition is true

    if (...) { ... } else { ... }
      ↑ else runs when the condition is false

    if (...) { } else if (...) { } else { }
      ↑ checks multiple conditions in order

📏  COMPARISON CHEAT SHEET
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    >    greater than
    <    less than
    >=   greater than OR equal   ← perfect for "minimum age"
    <=   less than OR equal
    ==   exactly equal           ← two equals signs!
    !=   not equal

🎯  FOR THIS CHALLENGE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
You need to check if age is AT LEAST 18.
"At least 18" means >= (greater than or equal to):

    if (age >= 18) {
        printf("You can drive!");
    } else {
        printf("Not old enough yet!");
    }

age is 15, so 15 >= 18 = FALSE → the else branch runs.""",
                "starter_code": '#include <stdio.h>\n\nint main() {\n    int age = 15;\n    // If age >= 18, print "You can drive!"\n    // Otherwise print "Not old enough yet!"\n    \n    return 0;\n}\n',
                "expected_output": "Not old enough yet!",
                "hint": "age is 15, which is less than 18, so the else branch runs",
                "xp_reward": 100,
                "is_final_project": True,
            },
        ],
    },
    {
        "number": 4,
        "title": "Loops",
        "description": "Make your program repeat things automatically!",
        "icon": "🔄",
        "color": "#f59e0b",
        "lessons": [
            {
                "order": 1,
                "title": "For Loop",
                "description": "Print numbers 1 to 5 using a for loop!",
                "theory": """\
🔄  WHY DO WE NEED LOOPS?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Imagine printing numbers 1 to 100.
Without loops you'd need 100 printf() calls!

Loops let you repeat code automatically. ♻️

📖  THE for LOOP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    for (start; condition; update) {
        /* code to repeat */
    }

Three parts separated by semicolons:
  1. start      →  runs once at the beginning
  2. condition  →  checked before each repetition
  3. update     →  runs after each repetition

Example — print 1 to 5:

    for (int i = 1; i <= 5; i++) {
        printf("%d\\n", i);
    }

Step by step:
  i=1 → 1 <= 5? YES → print 1 → i becomes 2
  i=2 → 2 <= 5? YES → print 2 → i becomes 3
  i=3 → 3 <= 5? YES → print 3 → i becomes 4
  i=4 → 4 <= 5? YES → print 4 → i becomes 5
  i=5 → 5 <= 5? YES → print 5 → i becomes 6
  i=6 → 6 <= 5? NO  → STOP

🔑  i++ means "add 1 to i" — same as  i = i + 1""",
                "starter_code": '#include <stdio.h>\n\nint main() {\n    // Print numbers 1 to 5, each on a new line\n    \n    return 0;\n}\n',
                "expected_output": "1\n2\n3\n4\n5",
                "hint": "Use for(int i = 1; i <= 5; i++) and printf(\"%d\\n\", i) inside",
                "xp_reward": 75,
                "is_final_project": False,
            },
            {
                "order": 2,
                "title": "While Loop",
                "description": "Use a while loop to count down from 3 to 1!",
                "theory": """\
🔄  THE while LOOP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
The while loop repeats as long as a condition is true:

    while (condition) {
        /* code to repeat */
    }

Example — count down from 3:

    int count = 3;
    while (count >= 1) {
        printf("%d\\n", count);
        count--;            ← subtract 1 from count
    }

Step by step:
  count=3 → 3 >= 1? YES → print 3 → count becomes 2
  count=2 → 2 >= 1? YES → print 2 → count becomes 1
  count=1 → 1 >= 1? YES → print 1 → count becomes 0
  count=0 → 0 >= 1? NO  → STOP

Output:  3  2  1

➕➖  INCREMENT AND DECREMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    i++   →  adds 1       (same as i = i + 1)
    i--   →  subtracts 1  (same as i = i - 1)

🆚  for vs while
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    for    → use when you know exactly how many times
    while  → use when you repeat until something changes

⚠️  INFINITE LOOP — AVOID THIS!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
If the condition never becomes false, the loop runs forever!
Always make sure your update (count--) moves you toward
the exit condition (count < 1).""",
                "starter_code": '#include <stdio.h>\n\nint main() {\n    int count = 3;\n    // Count down from 3 to 1\n    \n    return 0;\n}\n',
                "expected_output": "3\n2\n1",
                "hint": "Use while(count >= 1) and count-- to decrease count each time",
                "xp_reward": 75,
                "is_final_project": False,
            },
            {
                "order": 3,
                "title": "Sum with Loop",
                "description": "Calculate the sum of numbers 1 to 10!",
                "theory": """\
➕  ACCUMULATING VALUES WITH A LOOP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
An "accumulator" is a variable that collects values
as the loop runs. The key is to start at 0, then
keep adding to it each iteration:

    int sum = 0;                  ←  start at zero
    for (int i = 1; i <= 10; i++) {
        sum = sum + i;            ←  add i to sum each time
    }
    printf("Sum = %d", sum);

Let's trace through a small example (1 to 4):
    Before loop: sum = 0
    i=1:  sum = 0 + 1 = 1
    i=2:  sum = 1 + 2 = 3
    i=3:  sum = 3 + 3 = 6
    i=4:  sum = 6 + 4 = 10

For 1 to 10, the final answer is 55.

🔑  SHORTHAND OPERATORS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    sum = sum + i;   is the same as   sum += i;

Other useful shortcuts:
    x += 5;   →  x = x + 5
    x -= 3;   →  x = x - 3
    x *= 2;   →  x = x * 2

💡  FUN MATH FACT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
The sum of 1 + 2 + 3 + ... + n = n × (n+1) / 2
For n=10:  10 × 11 / 2 = 55  ✔""",
                "starter_code": '#include <stdio.h>\n\nint main() {\n    int sum = 0;\n    // Add numbers 1 through 10 to sum\n    \n    // Print: Sum = 55\n    \n    return 0;\n}\n',
                "expected_output": "Sum = 55",
                "hint": "Loop from 1 to 10, add each i to sum. 1+2+...+10 = 55",
                "xp_reward": 75,
                "is_final_project": False,
            },
            {
                "order": 4,
                "title": "Loops Challenge",
                "description": "Final challenge: Print the multiplication table of 3 (3x1 to 3x5)!",
                "theory": """\
🔄  COMBINING LOOPS AND MATH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
You can use the loop variable i directly in calculations
and inside printf():

    for (int i = 1; i <= 5; i++) {
        printf("3 x %d = %d\\n", i, 3 * i);
    }

Output:
    3 x 1 = 3
    3 x 2 = 6
    3 x 3 = 9
    3 x 4 = 12
    3 x 5 = 15

Note:
  • Two %d placeholders — one for i, one for 3*i
  • 3 * i is calculated directly inside printf()
  • \\n creates a new line after each result

🧠  REVIEW — LOOPS CHEAT SHEET
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    for (int i = start; i <= end; i++) { ... }
    while (condition) { ... }

    i++  →  add 1       i--  →  subtract 1
    sum += i  →  accumulate into sum

🏆  YOU NOW KNOW HOW TO:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✔  Count up and down with loops
  ✔  Sum values using an accumulator
  ✔  Use the loop variable in math and printf""",
                "starter_code": '#include <stdio.h>\n\nint main() {\n    // Print multiplication table of 3 from 1 to 5\n    \n    return 0;\n}\n',
                "expected_output": "3 x 1 = 3\n3 x 2 = 6\n3 x 3 = 9\n3 x 4 = 12\n3 x 5 = 15",
                "hint": "Use printf(\"3 x %d = %d\\n\", i, 3*i) inside a loop from 1 to 5",
                "xp_reward": 100,
                "is_final_project": True,
            },
        ],
    },
    {
        "number": 5,
        "title": "Functions",
        "description": "Create reusable blocks of code — like superpowers!",
        "icon": "⚡",
        "color": "#10b981",
        "lessons": [
            {
                "order": 1,
                "title": "Your First Function",
                "description": "Create a function called greet() that prints Hello from a function!",
                "theory": """\
⚡  WHAT IS A FUNCTION?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
A function is a named block of code that you can
run (call) whenever you need it — like a mini-program!

Why use functions?
  ✔  Write code once, use it many times
  ✔  Organize your program into logical pieces
  ✔  Easier to read and fix

📝  DEFINING A FUNCTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    void functionName() {
        /* code here */
    }

  void    →  means "this function returns nothing"
  ()      →  parentheses (empty = no inputs needed)
  { }     →  the function body — your code goes here

📞  CALLING A FUNCTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Define the function BEFORE main, then call it FROM main:

    void greet() {                   ←  DEFINE it here
        printf("Hello from a function!");
    }

    int main() {
        greet();                     ←  CALL it here
        return 0;
    }

⚠️  ORDER MATTERS!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
C reads from top to bottom — define the function
BEFORE you call it, or the compiler won't know it exists.""",
                "starter_code": '#include <stdio.h>\n\n// Define your greet() function here\n\n\nint main() {\n    // Call greet()\n    \n    return 0;\n}\n',
                "expected_output": "Hello from a function!",
                "hint": "Define void greet() { printf(\"Hello from a function!\"); } before main",
                "xp_reward": 75,
                "is_final_project": False,
            },
            {
                "order": 2,
                "title": "Functions with Parameters",
                "description": "Create add(a, b) that returns the sum and prints 7 + 3 = 10!",
                "theory": """\
📥  GIVING INPUTS TO FUNCTIONS — PARAMETERS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Parameters let you pass information into a function:

    void showAge(int age) {          ←  age is a parameter
        printf("You are %d years old!", age);
    }

    showAge(12);    →  You are 12 years old!
    showAge(25);    →  You are 25 years old!

Same function, different results depending on the input! 🎯

📤  RETURNING VALUES FROM FUNCTIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Functions can also send a result back to the caller:

    int add(int a, int b) {     ←  takes two ints, returns an int
        return a + b;           ←  sends the result back
    }

    int result = add(7, 3);     ←  result = 10
    printf("7 + 3 = %d", result);

📋  FULL PATTERN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    returnType name(type param1, type param2) {
        return value;
    }

  void    →  returns nothing
  int     →  returns a whole number
  float   →  returns a decimal number

🔑  KEY DIFFERENCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  void greet() { ... }         →  does something, no result
  int add(int a, int b) { ... }→  does something AND returns a value""",
                "starter_code": '#include <stdio.h>\n\n// Define add function that takes two ints and returns their sum\n\n\nint main() {\n    int result = add(7, 3);\n    // Print: 7 + 3 = 10\n    \n    return 0;\n}\n',
                "expected_output": "7 + 3 = 10",
                "hint": "Define int add(int a, int b) { return a + b; } before main",
                "xp_reward": 75,
                "is_final_project": False,
            },
            {
                "order": 3,
                "title": "Function with Loop",
                "description": "Create printStars(n) that prints n stars on one line. Call it with 5!",
                "theory": """\
🔗  COMBINING FUNCTIONS AND LOOPS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Functions can contain ANY code — including loops!

    void printStars(int n) {
        for (int i = 0; i < n; i++) {
            printf("*");
        }
        printf("\\n");
    }

Calling it with different values:
    printStars(1);   →  *
    printStars(3);   →  ***
    printStars(5);   →  *****

The parameter n controls how many stars to print.
Each call can produce different output! 🌟

📌  NOTE ON THE LOOP CONDITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    for (int i = 0; i < n; i++)

Starts at 0, runs while i < n (NOT i <= n)
→ runs exactly n times:
  n=3: i = 0, 1, 2  →  3 iterations ✔
  n=5: i = 0, 1, 2, 3, 4  →  5 iterations ✔

🔑  KEY INSIGHT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Functions make loops reusable!
Instead of copying the loop every time,
just call printStars(n) with any number.

This is called the DRY principle:
  Don't Repeat Yourself! 🚫📋""",
                "starter_code": '#include <stdio.h>\n\n// Define printStars(n) that prints n stars\n\n\nint main() {\n    printStars(5);\n    return 0;\n}\n',
                "expected_output": "*****",
                "hint": "Loop n times printing * each time, then printf(\"\\n\") at the end",
                "xp_reward": 75,
                "is_final_project": False,
            },
            {
                "order": 4,
                "title": "Functions Challenge",
                "description": "Final challenge: Create isEven(n) that returns 1 if even, 0 if odd. Test with 4 and 7!",
                "theory": """\
✅❌  RETURNING YES/NO FROM FUNCTIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
C doesn't have a true/false type in the basics.
Instead, we use integers:
    1  →  true  (yes)
    0  →  false (no)

Example:
    int isEven(int n) {
        if (n % 2 == 0) {
            return 1;     ←  even!
        }
        return 0;         ←  odd
    }

🧪  USING THE RESULT IN AN if STATEMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    if (isEven(4)) {                       ←  returns 1 = true
        printf("4 is even\\n");            ←  this runs!
    } else {
        printf("4 is odd\\n");
    }

    if (isEven(7)) {                       ←  returns 0 = false
        printf("7 is even\\n");
    } else {
        printf("7 is odd\\n");             ←  this runs!
    }

🧠  REVIEW — FUNCTIONS CHEAT SHEET
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    void f() { }                 →  no input, no output
    void f(int x) { }            →  input, no output
    int  f(int x) { return x; }  →  input + output
    if (f(n)) { }                →  use result as condition

🏆  YOU NOW KNOW HOW TO:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✔  Define and call functions
  ✔  Pass parameters
  ✔  Return values
  ✔  Use function results in conditions and math""",
                "starter_code": '#include <stdio.h>\n\n// Define isEven(n): returns 1 if even, 0 if odd\n\n\nint main() {\n    // Test with 4 (should print "4 is even")\n    \n    // Test with 7 (should print "7 is odd")\n    \n    return 0;\n}\n',
                "expected_output": "4 is even\n7 is odd",
                "hint": "Check isEven(4) and isEven(7) with if/else to print the correct message",
                "xp_reward": 100,
                "is_final_project": True,
            },
        ],
    },
    {
        "number": 6,
        "title": "Final Project",
        "description": "Become a C Master with your final adventure!",
        "icon": "🏆",
        "color": "#ef4444",
        "lessons": [
            {
                "order": 1,
                "title": "Mini Calculator",
                "description": "Build a calculator that shows results for +, -, * of two numbers (a=10, b=3)!",
                "theory": """\
🏆  YOU MADE IT TO THE FINAL PROJECT!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
This world combines EVERYTHING you've learned:

  World 1  →  printf() to show results on screen
  World 2  →  variables to store numbers
  World 3  →  conditions to control the flow
  World 4  →  loops to repeat operations
  World 5  →  functions to organize your code

🧮  BUILDING A MINI CALCULATOR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
The starter code already has 3 helper functions:

    int add(int a, int b)       →  returns a + b
    int subtract(int a, int b)  →  returns a - b
    int multiply(int a, int b)  →  returns a * b

Your job: call them and print the results!

You can call a function directly inside printf():

    printf("%d + %d = %d\\n", a, b, add(a, b));

No need for an extra variable — the result of add(a, b)
is used directly as the third %d argument!

📋  THREE LINES TO PRINT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    10 + 3 = 13
    10 - 3 = 7
    10 * 3 = 30

Use three printf() calls, one for each operation.
Each line follows the same pattern — just change
the operator symbol and the function name!""",
                "starter_code": '#include <stdio.h>\n\nint add(int a, int b) { return a + b; }\nint subtract(int a, int b) { return a - b; }\nint multiply(int a, int b) { return a * b; }\n\nint main() {\n    int a = 10, b = 3;\n    // Print: 10 + 3 = 13\n    // Print: 10 - 3 = 7\n    // Print: 10 * 3 = 30\n    \n    return 0;\n}\n',
                "expected_output": "10 + 3 = 13\n10 - 3 = 7\n10 * 3 = 30",
                "hint": "Use the three functions already defined and printf with %d",
                "xp_reward": 150,
                "is_final_project": False,
            },
            {
                "order": 2,
                "title": "FizzBuzz",
                "description": "Print 1 to 15. Multiples of 3: Fizz. Multiples of 5: Buzz. Both: FizzBuzz!",
                "theory": """\
🧠  THE CLASSIC FIZZBUZZ CHALLENGE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FizzBuzz is a famous programming puzzle used in
job interviews around the world!

The rules:
  • Print numbers 1 to 15
  • If divisible by 3 → print "Fizz"
  • If divisible by 5 → print "Buzz"
  • If divisible by BOTH 3 and 5 → print "FizzBuzz"
  • Otherwise → print the number

🔗  THE && OPERATOR — LOGICAL AND
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
&& means BOTH conditions must be true at the same time:

    if (i % 3 == 0 && i % 5 == 0)
    →  true only when i is divisible by BOTH 3 AND 5

    i=15: 15%3==0 AND 15%5==0  →  true  →  FizzBuzz
    i=9:  9%3==0 AND 9%5!=0   →  false (only one is true)

🔑  CRITICAL: CHECK FizzBuzz FIRST!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    if (i % 15 == 0) {            ←  check BOTH first!
        printf("FizzBuzz\\n");
    } else if (i % 3 == 0) {      ←  then just 3
        printf("Fizz\\n");
    } else if (i % 5 == 0) {      ←  then just 5
        printf("Buzz\\n");
    } else {
        printf("%d\\n", i);        ←  otherwise the number
    }

i % 15 == 0  is the same as  i % 3 == 0 && i % 5 == 0
(because 15 = 3 × 5, so being divisible by both = divisible by 15)

Wrap this in a for loop from i=1 to i=15!""",
                "starter_code": '#include <stdio.h>\n\nint main() {\n    for (int i = 1; i <= 15; i++) {\n        // Check FizzBuzz conditions\n        \n    }\n    return 0;\n}\n',
                "expected_output": "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz",
                "hint": "Check i%15==0 for FizzBuzz first, then i%3==0 for Fizz, then i%5==0 for Buzz",
                "xp_reward": 150,
                "is_final_project": False,
            },
            {
                "order": 3,
                "title": "C Master Challenge",
                "description": "Print a triangle of stars: row 1 has 1 star, row 2 has 2, up to row 5!",
                "theory": """\
🔄  NESTED LOOPS — A LOOP INSIDE A LOOP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
You can put a loop inside another loop!
The inner loop runs COMPLETELY for EACH step of the outer loop.

    for (int row = 1; row <= 3; row++) {        ←  outer loop
        for (int star = 1; star <= row; star++) {   ←  inner loop
            printf("*");
        }
        printf("\\n");     ←  new line after each row
    }

Step by step:
  row=1: inner runs 1 time   →  *   then newline
  row=2: inner runs 2 times  →  **  then newline
  row=3: inner runs 3 times  →  *** then newline

Output:
    *
    **
    ***

🌟  THE KEY INSIGHT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
The inner loop condition uses the OUTER loop variable:
    star <= row
This means the inner loop runs row times — 1 star for row 1,
2 stars for row 2, 3 stars for row 3, and so on!

🏆  CONGRATULATIONS — YOU ARE A C MASTER!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
By completing this course you have learned:
  ✔  printf() and escape sequences
  ✔  Variables: int and float
  ✔  Conditions: if, else if, else
  ✔  Loops: for and while
  ✔  Functions with parameters and return values
  ✔  Nested loops

You can now call yourself a C programmer! 🎉""",
                "starter_code": '#include <stdio.h>\n\nint main() {\n    // Print a triangle: row 1=1 star, row 2=2 stars, ..., row 5=5 stars\n    \n    return 0;\n}\n',
                "expected_output": "*\n**\n***\n****\n*****",
                "hint": "Use two nested for loops. Outer loop for rows 1-5, inner loop prints that many stars",
                "xp_reward": 200,
                "is_final_project": True,
            },
        ],
    },
]


EXERCISES_DATA = {
    "Your First Program": [
        {"order": 1, "description": "Print the classic message: Hello, World!", "starter_code": '#include <stdio.h>\n\nint main() {\n    // Print: Hello, World!\n    \n    return 0;\n}\n', "expected_output": "Hello, World!", "hint": 'Use printf("Hello, World!");', "xp_reward": 15, "is_final": False},
        {"order": 2, "description": "Print: I love coding!", "starter_code": '#include <stdio.h>\n\nint main() {\n    // Print: I love coding!\n    \n    return 0;\n}\n', "expected_output": "I love coding!", "hint": 'Use printf("I love coding!");', "xp_reward": 15, "is_final": False},
        {"order": 3, "description": "Print: CQuest rocks!", "starter_code": '#include <stdio.h>\n\nint main() {\n    // Print: CQuest rocks!\n    \n    return 0;\n}\n', "expected_output": "CQuest rocks!", "hint": 'Use printf("CQuest rocks!");', "xp_reward": 15, "is_final": False},
        {"order": 4, "description": "Final challenge: Print: I am a programmer!", "starter_code": '#include <stdio.h>\n\nint main() {\n    // Print: I am a programmer!\n    \n    return 0;\n}\n', "expected_output": "I am a programmer!", "hint": 'Use printf("I am a programmer!");', "xp_reward": 50, "is_final": True},
    ],
    "Print Your Name": [
        {"order": 1, "description": "Print two lines: Hello, World! then My name is CQuest!", "starter_code": '#include <stdio.h>\n\nint main() {\n    printf("Hello, World!\\n");\n    // Now print: My name is CQuest!\n    \n    return 0;\n}\n', "expected_output": "Hello, World!\nMy name is CQuest!", "hint": 'Add printf("My name is CQuest!");', "xp_reward": 15, "is_final": False},
        {"order": 2, "description": "Print two lines: Good morning! then Time to code!", "starter_code": '#include <stdio.h>\n\nint main() {\n    // Print: Good morning!\n    // Print: Time to code!\n    \n    return 0;\n}\n', "expected_output": "Good morning!\nTime to code!", "hint": "Use two printf() calls, each ending with \\n", "xp_reward": 15, "is_final": False},
        {"order": 3, "description": "Print three lines: Line 1, Line 2, Line 3", "starter_code": '#include <stdio.h>\n\nint main() {\n    // Print Line 1, Line 2, Line 3 on separate lines\n    \n    return 0;\n}\n', "expected_output": "Line 1\nLine 2\nLine 3", "hint": "Use three printf() calls with \\n after each", "xp_reward": 15, "is_final": False},
        {"order": 4, "description": "Final challenge: Print three lines: Hello!, I love C!, Let's code!", "starter_code": '#include <stdio.h>\n\nint main() {\n    // Print three lines\n    \n    return 0;\n}\n', "expected_output": "Hello!\nI love C!\nLet's code!", "hint": "Three printf() calls, remember \\n after each line", "xp_reward": 50, "is_final": True},
    ],
    "Hello World Challenge": [
        {"order": 1, "description": "Print: Hello!, Welcome to CQuest!, Let's code!", "starter_code": '#include <stdio.h>\n\nint main() {\n    // Print the three lines\n    \n    return 0;\n}\n', "expected_output": "Hello!\nWelcome to CQuest!\nLet's code!", "hint": "Three printf() calls with \\n", "xp_reward": 15, "is_final": False},
        {"order": 2, "description": "Print the colors: Red, Green, Blue each on its own line", "starter_code": '#include <stdio.h>\n\nint main() {\n    // Print Red, Green, Blue\n    \n    return 0;\n}\n', "expected_output": "Red\nGreen\nBlue", "hint": 'printf("Red\\n"); printf("Green\\n"); printf("Blue\\n");', "xp_reward": 15, "is_final": False},
        {"order": 3, "description": "Count down: print 3, 2, 1, Go! each on its own line", "starter_code": '#include <stdio.h>\n\nint main() {\n    // Print 3, 2, 1, Go!\n    \n    return 0;\n}\n', "expected_output": "3\n2\n1\nGo!", "hint": "Four printf() calls", "xp_reward": 15, "is_final": False},
        {"order": 4, "description": "Final challenge: Print Ready, Set, Code! each on its own line", "starter_code": '#include <stdio.h>\n\nint main() {\n    // Print Ready, Set, Code!\n    \n    return 0;\n}\n', "expected_output": "Ready\nSet\nCode!", "hint": "Three printf() calls, the last one without \\n", "xp_reward": 100, "is_final": True},
    ],
    "Integer Variables": [
        {"order": 1, "description": "Create int age = 12 and print: My age is 12", "starter_code": '#include <stdio.h>\n\nint main() {\n    // Create int age = 12\n    \n    // Print: My age is 12\n    \n    return 0;\n}\n', "expected_output": "My age is 12", "hint": 'int age = 12; then printf("My age is %d", age);', "xp_reward": 15, "is_final": False},
        {"order": 2, "description": "Create int score = 100 and print: My score is 100", "starter_code": '#include <stdio.h>\n\nint main() {\n    // Create int score = 100\n    \n    // Print: My score is 100\n    \n    return 0;\n}\n', "expected_output": "My score is 100", "hint": 'int score = 100; then printf("My score is %d", score);', "xp_reward": 15, "is_final": False},
        {"order": 3, "description": "Create int year = 2025 and print: The year is 2025", "starter_code": '#include <stdio.h>\n\nint main() {\n    // Create int year = 2025\n    \n    // Print: The year is 2025\n    \n    return 0;\n}\n', "expected_output": "The year is 2025", "hint": 'int year = 2025; then printf("The year is %d", year);', "xp_reward": 15, "is_final": False},
        {"order": 4, "description": "Final: Create int lives = 3 and int level = 1. Print: Lives: 3 then Level: 1", "starter_code": '#include <stdio.h>\n\nint main() {\n    // Create int lives = 3 and int level = 1\n    \n    // Print: Lives: 3\n    // Print: Level: 1\n    \n    return 0;\n}\n', "expected_output": "Lives: 3\nLevel: 1", "hint": "Two variables and two printf() calls with %d", "xp_reward": 50, "is_final": True},
    ],
    "Float Variables": [
        {"order": 1, "description": "Create float price = 9.99 and print: Price: 9.99", "starter_code": '#include <stdio.h>\n\nint main() {\n    // Create float price = 9.99\n    \n    // Print: Price: 9.99\n    \n    return 0;\n}\n', "expected_output": "Price: 9.99", "hint": 'float price = 9.99; then printf("Price: %.2f", price);', "xp_reward": 15, "is_final": False},
        {"order": 2, "description": "Create float temp = 36.60 and print: Temperature: 36.60", "starter_code": '#include <stdio.h>\n\nint main() {\n    // Create float temp = 36.60\n    \n    // Print: Temperature: 36.60\n    \n    return 0;\n}\n', "expected_output": "Temperature: 36.60", "hint": 'float temp = 36.60; then printf("Temperature: %.2f", temp);', "xp_reward": 15, "is_final": False},
        {"order": 3, "description": "Create float pi = 3.14 and print: Pi is: 3.14", "starter_code": '#include <stdio.h>\n\nint main() {\n    // Create float pi = 3.14\n    \n    // Print: Pi is: 3.14\n    \n    return 0;\n}\n', "expected_output": "Pi is: 3.14", "hint": 'float pi = 3.14; then printf("Pi is: %.2f", pi);', "xp_reward": 15, "is_final": False},
        {"order": 4, "description": "Final: float height = 1.75 and float weight = 68.50. Print both on separate lines.", "starter_code": '#include <stdio.h>\n\nint main() {\n    // Create float height = 1.75\n    // Create float weight = 68.50\n    \n    // Print: Height: 1.75\n    // Print: Weight: 68.50\n    \n    return 0;\n}\n', "expected_output": "Height: 1.75\nWeight: 68.50", "hint": "Two floats and two printf() calls with %.2f", "xp_reward": 50, "is_final": True},
    ],
    "Adding Numbers": [
        {"order": 1, "description": "a = 10, b = 5. Calculate the sum and print: 10 + 5 = 15", "starter_code": '#include <stdio.h>\n\nint main() {\n    int a = 10;\n    int b = 5;\n    // Calculate sum and print: 10 + 5 = 15\n    \n    return 0;\n}\n', "expected_output": "10 + 5 = 15", "hint": "int sum = a + b; then printf with three %d", "xp_reward": 15, "is_final": False},
        {"order": 2, "description": "a = 8, b = 3. Calculate the difference and print: 8 - 3 = 5", "starter_code": '#include <stdio.h>\n\nint main() {\n    int a = 8;\n    int b = 3;\n    // Calculate difference and print: 8 - 3 = 5\n    \n    return 0;\n}\n', "expected_output": "8 - 3 = 5", "hint": "int diff = a - b; then printf with three %d", "xp_reward": 15, "is_final": False},
        {"order": 3, "description": "a = 6, b = 7. Calculate the product and print: 6 * 7 = 42", "starter_code": '#include <stdio.h>\n\nint main() {\n    int a = 6;\n    int b = 7;\n    // Calculate product and print: 6 * 7 = 42\n    \n    return 0;\n}\n', "expected_output": "6 * 7 = 42", "hint": "int product = a * b; then printf with three %d", "xp_reward": 15, "is_final": False},
        {"order": 4, "description": "Final: a = 20, b = 4. Calculate the division and print: 20 / 4 = 5", "starter_code": '#include <stdio.h>\n\nint main() {\n    int a = 20;\n    int b = 4;\n    // Calculate division and print: 20 / 4 = 5\n    \n    return 0;\n}\n', "expected_output": "20 / 4 = 5", "hint": "int result = a / b; then printf with three %d", "xp_reward": 75, "is_final": True},
    ],
    "Variables Challenge": [
        {"order": 1, "description": "width = 8, height = 5. Calculate area and print: Area = 40", "starter_code": '#include <stdio.h>\n\nint main() {\n    int width = 8;\n    int height = 5;\n    // Calculate area and print: Area = 40\n    \n    return 0;\n}\n', "expected_output": "Area = 40", "hint": "int area = width * height;", "xp_reward": 20, "is_final": False},
        {"order": 2, "description": "a = 12, b = 7. Print their sum, difference and product each on a new line.", "starter_code": '#include <stdio.h>\n\nint main() {\n    int a = 12;\n    int b = 7;\n    // Print sum, then difference, then product\n    \n    return 0;\n}\n', "expected_output": "19\n5\n84", "hint": "Three printf() calls: a+b, a-b, a*b each with \\n", "xp_reward": 20, "is_final": False},
        {"order": 3, "description": "side = 6. Calculate the perimeter of a square (4 × side) and print: Square perimeter = 24", "starter_code": '#include <stdio.h>\n\nint main() {\n    int side = 6;\n    // Calculate perimeter = 4 * side\n    // Print: Square perimeter = 24\n    \n    return 0;\n}\n', "expected_output": "Square perimeter = 24", "hint": "int perimeter = 4 * side;", "xp_reward": 20, "is_final": False},
        {"order": 4, "description": "Final: x = 3, y = 4. Print: Hypotenuse squared = 25 (use x*x + y*y)", "starter_code": '#include <stdio.h>\n\nint main() {\n    int x = 3;\n    int y = 4;\n    // Calculate x*x + y*y\n    // Print: Hypotenuse squared = 25\n    \n    return 0;\n}\n', "expected_output": "Hypotenuse squared = 25", "hint": "int h2 = x*x + y*y; — 3²+4² = 25", "xp_reward": 100, "is_final": True},
    ],
    "Simple If": [
        {"order": 1, "description": "score = 75. If score is greater than 50, print: You passed!", "starter_code": '#include <stdio.h>\n\nint main() {\n    int score = 75;\n    // If score > 50, print "You passed!"\n    \n    return 0;\n}\n', "expected_output": "You passed!", "hint": "if (score > 50) { printf(\"You passed!\"); }", "xp_reward": 15, "is_final": False},
        {"order": 2, "description": "age = 20. If age is 18 or more, print: You are an adult!", "starter_code": '#include <stdio.h>\n\nint main() {\n    int age = 20;\n    // If age >= 18, print "You are an adult!"\n    \n    return 0;\n}\n', "expected_output": "You are an adult!", "hint": "if (age >= 18) { printf(\"You are an adult!\"); }", "xp_reward": 15, "is_final": False},
        {"order": 3, "description": "temperature = 35. If temperature is greater than 30, print: It is very hot!", "starter_code": '#include <stdio.h>\n\nint main() {\n    int temperature = 35;\n    // If temperature > 30, print "It is very hot!"\n    \n    return 0;\n}\n', "expected_output": "It is very hot!", "hint": "if (temperature > 30) { printf(\"It is very hot!\"); }", "xp_reward": 15, "is_final": False},
        {"order": 4, "description": "Final: points = 100. If points equals 100, print: Perfect score!", "starter_code": '#include <stdio.h>\n\nint main() {\n    int points = 100;\n    // If points == 100, print "Perfect score!"\n    \n    return 0;\n}\n', "expected_output": "Perfect score!", "hint": "Use == (two equals signs) to check equality", "xp_reward": 50, "is_final": True},
    ],
    "If Else": [
        {"order": 1, "description": "number = 7. Print Odd if it is odd, Even if it is even.", "starter_code": '#include <stdio.h>\n\nint main() {\n    int number = 7;\n    // Check even or odd\n    \n    return 0;\n}\n', "expected_output": "Odd", "hint": "if (number % 2 == 0) print Even, else print Odd", "xp_reward": 15, "is_final": False},
        {"order": 2, "description": "age = 15. Print Adult if age >= 18, otherwise print Minor.", "starter_code": '#include <stdio.h>\n\nint main() {\n    int age = 15;\n    // Print "Adult" or "Minor"\n    \n    return 0;\n}\n', "expected_output": "Minor", "hint": "if (age >= 18) print Adult, else print Minor", "xp_reward": 15, "is_final": False},
        {"order": 3, "description": "score = 45. Print Pass if score >= 60, otherwise print Fail.", "starter_code": '#include <stdio.h>\n\nint main() {\n    int score = 45;\n    // Print "Pass" or "Fail"\n    \n    return 0;\n}\n', "expected_output": "Fail", "hint": "if (score >= 60) print Pass, else print Fail", "xp_reward": 15, "is_final": False},
        {"order": 4, "description": "Final: n = -5. Print Positive if n > 0, otherwise print Not positive.", "starter_code": '#include <stdio.h>\n\nint main() {\n    int n = -5;\n    // Print "Positive" or "Not positive"\n    \n    return 0;\n}\n', "expected_output": "Not positive", "hint": "if (n > 0) print Positive, else print Not positive", "xp_reward": 75, "is_final": True},
    ],
    "If Else If": [
        {"order": 1, "description": "score = 85. Print Grade: A if >= 90, Grade: B if >= 70, Grade: C otherwise.", "starter_code": '#include <stdio.h>\n\nint main() {\n    int score = 85;\n    // Print the grade: A, B or C\n    \n    return 0;\n}\n', "expected_output": "Grade: B", "hint": "Check >= 90 first, then >= 70, then else for C", "xp_reward": 20, "is_final": False},
        {"order": 2, "description": "age = 8. Print Child if age < 13, Teen if age < 18, Adult otherwise.", "starter_code": '#include <stdio.h>\n\nint main() {\n    int age = 8;\n    // Print Child, Teen, or Adult\n    \n    return 0;\n}\n', "expected_output": "Child", "hint": "Check < 13 first, then < 18, then else for Adult", "xp_reward": 20, "is_final": False},
        {"order": 3, "description": "score = 55. Grade: A (>=90), B (>=70), C (>=50), F otherwise.", "starter_code": '#include <stdio.h>\n\nint main() {\n    int score = 55;\n    // Print Grade: A, B, C or F\n    \n    return 0;\n}\n', "expected_output": "Grade: C", "hint": "Four branches: >= 90, >= 70, >= 50, else F", "xp_reward": 20, "is_final": False},
        {"order": 4, "description": "Final: temp = 5. Print Cold if temp < 10, Warm if temp < 25, Hot otherwise.", "starter_code": '#include <stdio.h>\n\nint main() {\n    int temp = 5;\n    // Print Cold, Warm, or Hot\n    \n    return 0;\n}\n', "expected_output": "Cold", "hint": "Check < 10 first, then < 25, then else for Hot", "xp_reward": 75, "is_final": True},
    ],
    "Decisions Challenge": [
        {"order": 1, "description": "age = 15. Print You can drive! if age >= 18, otherwise Not old enough yet!", "starter_code": '#include <stdio.h>\n\nint main() {\n    int age = 15;\n    // Check driving age\n    \n    return 0;\n}\n', "expected_output": "Not old enough yet!", "hint": "if (age >= 18) ... else ...", "xp_reward": 20, "is_final": False},
        {"order": 2, "description": "score = 75. Print Excellent! if >= 90, Good job! if >= 60, Keep trying! otherwise.", "starter_code": '#include <stdio.h>\n\nint main() {\n    int score = 75;\n    // Three levels of feedback\n    \n    return 0;\n}\n', "expected_output": "Good job!", "hint": "Use if / else if / else with >= 90 and >= 60", "xp_reward": 20, "is_final": False},
        {"order": 3, "description": "number = 0. Print Positive, Negative or Zero depending on its value.", "starter_code": '#include <stdio.h>\n\nint main() {\n    int number = 0;\n    // Check positive, negative or zero\n    \n    return 0;\n}\n', "expected_output": "Zero", "hint": "if > 0, else if < 0, else (which means == 0)", "xp_reward": 20, "is_final": False},
        {"order": 4, "description": "Final: x = 6. Print Positive even! if x > 0 AND x is even, otherwise print Other.", "starter_code": '#include <stdio.h>\n\nint main() {\n    int x = 6;\n    // Check if positive AND even\n    \n    return 0;\n}\n', "expected_output": "Positive even!", "hint": "Use && to combine two conditions: x > 0 && x % 2 == 0", "xp_reward": 100, "is_final": True},
    ],
    "For Loop": [
        {"order": 1, "description": "Use a for loop to print numbers 1 to 5, each on a new line.", "starter_code": '#include <stdio.h>\n\nint main() {\n    // Print 1 to 5\n    \n    return 0;\n}\n', "expected_output": "1\n2\n3\n4\n5", "hint": "for (int i = 1; i <= 5; i++) { printf(\"%d\\n\", i); }", "xp_reward": 20, "is_final": False},
        {"order": 2, "description": "Use a for loop to print numbers 1 to 10, each on a new line.", "starter_code": '#include <stdio.h>\n\nint main() {\n    // Print 1 to 10\n    \n    return 0;\n}\n', "expected_output": "1\n2\n3\n4\n5\n6\n7\n8\n9\n10", "hint": "Change the condition to i <= 10", "xp_reward": 20, "is_final": False},
        {"order": 3, "description": "Use a for loop to print even numbers from 2 to 10 (2, 4, 6, 8, 10).", "starter_code": '#include <stdio.h>\n\nint main() {\n    // Print even numbers: 2, 4, 6, 8, 10\n    \n    return 0;\n}\n', "expected_output": "2\n4\n6\n8\n10", "hint": "Start i at 2 and use i += 2 to count by 2", "xp_reward": 20, "is_final": False},
        {"order": 4, "description": "Final: Print multiples of 3 from 3 to 15 (3, 6, 9, 12, 15).", "starter_code": '#include <stdio.h>\n\nint main() {\n    // Print: 3, 6, 9, 12, 15\n    \n    return 0;\n}\n', "expected_output": "3\n6\n9\n12\n15", "hint": "Start i at 3 and use i += 3, or use i*3 inside the loop", "xp_reward": 75, "is_final": True},
    ],
    "While Loop": [
        {"order": 1, "description": "Use a while loop to count down from 3 to 1.", "starter_code": '#include <stdio.h>\n\nint main() {\n    int count = 3;\n    // Count down from 3 to 1\n    \n    return 0;\n}\n', "expected_output": "3\n2\n1", "hint": "while (count >= 1) { printf(\"%d\\n\", count); count--; }", "xp_reward": 20, "is_final": False},
        {"order": 2, "description": "Use a while loop to count up from 1 to 5.", "starter_code": '#include <stdio.h>\n\nint main() {\n    int n = 1;\n    // Count up from 1 to 5\n    \n    return 0;\n}\n', "expected_output": "1\n2\n3\n4\n5", "hint": "while (n <= 5) { printf(\"%d\\n\", n); n++; }", "xp_reward": 20, "is_final": False},
        {"order": 3, "description": "Use a while loop to print: 10, 8, 6, 4, 2 (subtract 2 each time).", "starter_code": '#include <stdio.h>\n\nint main() {\n    int n = 10;\n    // Print 10, 8, 6, 4, 2\n    \n    return 0;\n}\n', "expected_output": "10\n8\n6\n4\n2", "hint": "while (n >= 2) { printf then n -= 2; }", "xp_reward": 20, "is_final": False},
        {"order": 4, "description": "Final: Start with n = 1. While n <= 16, print n then double it. Print: 1, 2, 4, 8, 16.", "starter_code": '#include <stdio.h>\n\nint main() {\n    int n = 1;\n    // Print 1, 2, 4, 8, 16\n    \n    return 0;\n}\n', "expected_output": "1\n2\n4\n8\n16", "hint": "while (n <= 16) { printf then n = n * 2; }", "xp_reward": 75, "is_final": True},
    ],
    "Sum with Loop": [
        {"order": 1, "description": "Use a loop to calculate the sum of numbers 1 to 10. Print: Sum = 55", "starter_code": '#include <stdio.h>\n\nint main() {\n    int sum = 0;\n    // Add 1 to 10 and print Sum = 55\n    \n    return 0;\n}\n', "expected_output": "Sum = 55", "hint": "for loop from 1 to 10, add i to sum each time", "xp_reward": 20, "is_final": False},
        {"order": 2, "description": "Use a loop to sum even numbers from 2 to 10 (2+4+6+8+10). Print: Sum = 30", "starter_code": '#include <stdio.h>\n\nint main() {\n    int sum = 0;\n    // Add even numbers 2,4,6,8,10\n    \n    return 0;\n}\n', "expected_output": "Sum = 30", "hint": "Loop with i += 2 starting from 2, or use if (i%2==0)", "xp_reward": 20, "is_final": False},
        {"order": 3, "description": "Calculate 1 × 2 × 3 × 4 × 5 using a loop. Print: Product = 120", "starter_code": '#include <stdio.h>\n\nint main() {\n    int product = 1;\n    // Multiply 1 to 5\n    \n    return 0;\n}\n', "expected_output": "Product = 120", "hint": "Start product at 1, then product *= i each loop", "xp_reward": 20, "is_final": False},
        {"order": 4, "description": "Final: Sum the odd numbers from 1 to 9 (1+3+5+7+9). Print: Sum = 25", "starter_code": '#include <stdio.h>\n\nint main() {\n    int sum = 0;\n    // Add odd numbers 1,3,5,7,9\n    \n    return 0;\n}\n', "expected_output": "Sum = 25", "hint": "Loop with i += 2 starting at 1, or use if (i%2 != 0)", "xp_reward": 75, "is_final": True},
    ],
    "Loops Challenge": [
        {"order": 1, "description": "Print the multiplication table of 3 from 3×1 to 3×5.", "starter_code": '#include <stdio.h>\n\nint main() {\n    // Print: 3 x 1 = 3 ... 3 x 5 = 15\n    \n    return 0;\n}\n', "expected_output": "3 x 1 = 3\n3 x 2 = 6\n3 x 3 = 9\n3 x 4 = 12\n3 x 5 = 15", "hint": 'for loop: printf("3 x %d = %d\\n", i, 3*i)', "xp_reward": 20, "is_final": False},
        {"order": 2, "description": "Print the multiplication table of 5 from 5×1 to 5×5.", "starter_code": '#include <stdio.h>\n\nint main() {\n    // Print: 5 x 1 = 5 ... 5 x 5 = 25\n    \n    return 0;\n}\n', "expected_output": "5 x 1 = 5\n5 x 2 = 10\n5 x 3 = 15\n5 x 4 = 20\n5 x 5 = 25", "hint": 'printf("5 x %d = %d\\n", i, 5*i)', "xp_reward": 20, "is_final": False},
        {"order": 3, "description": "Use a loop to print the square of each number from 1 to 5: 1, 4, 9, 16, 25.", "starter_code": '#include <stdio.h>\n\nint main() {\n    // Print squares: 1, 4, 9, 16, 25\n    \n    return 0;\n}\n', "expected_output": "1\n4\n9\n16\n25", "hint": "printf(\"%d\\n\", i*i) inside the loop", "xp_reward": 20, "is_final": False},
        {"order": 4, "description": "Final: Print powers of 2 from 2¹ to 2⁵: 2, 4, 8, 16, 32.", "starter_code": '#include <stdio.h>\n\nint main() {\n    // Print 2, 4, 8, 16, 32\n    \n    return 0;\n}\n', "expected_output": "2\n4\n8\n16\n32", "hint": "Use a variable that doubles each loop: n = 2; n *= 2", "xp_reward": 100, "is_final": True},
    ],
    "Your First Function": [
        {"order": 1, "description": "Define a function greet() that prints: Hello from a function! Then call it from main.", "starter_code": '#include <stdio.h>\n\n// Define greet() here\n\n\nint main() {\n    // Call greet()\n    \n    return 0;\n}\n', "expected_output": "Hello from a function!", "hint": "void greet() { printf(\"Hello from a function!\"); }", "xp_reward": 20, "is_final": False},
        {"order": 2, "description": "Define a function sayGoodbye() that prints: See you later! Then call it.", "starter_code": '#include <stdio.h>\n\n// Define sayGoodbye() here\n\n\nint main() {\n    // Call sayGoodbye()\n    \n    return 0;\n}\n', "expected_output": "See you later!", "hint": "void sayGoodbye() { printf(\"See you later!\"); }", "xp_reward": 20, "is_final": False},
        {"order": 3, "description": "Define a function printStars() that prints five stars: ***** Then call it.", "starter_code": '#include <stdio.h>\n\n// Define printStars() here\n\n\nint main() {\n    // Call printStars()\n    \n    return 0;\n}\n', "expected_output": "*****", "hint": 'void printStars() { printf("*****"); }', "xp_reward": 20, "is_final": False},
        {"order": 4, "description": "Final: Define showWelcome() that prints: Welcome to CQuest! Then call it.", "starter_code": '#include <stdio.h>\n\n// Define showWelcome() here\n\n\nint main() {\n    // Call showWelcome()\n    \n    return 0;\n}\n', "expected_output": "Welcome to CQuest!", "hint": 'void showWelcome() { printf("Welcome to CQuest!"); }', "xp_reward": 75, "is_final": True},
    ],
    "Functions with Parameters": [
        {"order": 1, "description": "Define int add(int a, int b) that returns a+b. Call add(7,3) and print: 7 + 3 = 10", "starter_code": '#include <stdio.h>\n\n// Define add(a, b) here\n\n\nint main() {\n    int result = add(7, 3);\n    // Print: 7 + 3 = 10\n    \n    return 0;\n}\n', "expected_output": "7 + 3 = 10", "hint": "int add(int a, int b) { return a + b; }", "xp_reward": 20, "is_final": False},
        {"order": 2, "description": "Define int multiply(int a, int b) that returns a*b. Call multiply(4,5) and print: 4 x 5 = 20", "starter_code": '#include <stdio.h>\n\n// Define multiply(a, b) here\n\n\nint main() {\n    int result = multiply(4, 5);\n    // Print: 4 x 5 = 20\n    \n    return 0;\n}\n', "expected_output": "4 x 5 = 20", "hint": "int multiply(int a, int b) { return a * b; }", "xp_reward": 20, "is_final": False},
        {"order": 3, "description": "Define int subtract(int a, int b) that returns a-b. Call subtract(10,4) and print: 10 - 4 = 6", "starter_code": '#include <stdio.h>\n\n// Define subtract(a, b) here\n\n\nint main() {\n    int result = subtract(10, 4);\n    // Print: 10 - 4 = 6\n    \n    return 0;\n}\n', "expected_output": "10 - 4 = 6", "hint": "int subtract(int a, int b) { return a - b; }", "xp_reward": 20, "is_final": False},
        {"order": 4, "description": "Final: Define int square(int n) that returns n*n. Call square(6) and print: Square of 6 = 36", "starter_code": '#include <stdio.h>\n\n// Define square(n) here\n\n\nint main() {\n    int result = square(6);\n    // Print: Square of 6 = 36\n    \n    return 0;\n}\n', "expected_output": "Square of 6 = 36", "hint": "int square(int n) { return n * n; }", "xp_reward": 75, "is_final": True},
    ],
    "Function with Loop": [
        {"order": 1, "description": "Define printStars(int n) that prints n stars on one line. Call printStars(5).", "starter_code": '#include <stdio.h>\n\n// Define printStars(n)\n\n\nint main() {\n    printStars(5);\n    return 0;\n}\n', "expected_output": "*****", "hint": "Loop n times printing * each time", "xp_reward": 20, "is_final": False},
        {"order": 2, "description": "Define countDown(int n) that prints n, n-1, ..., 1 each on a new line. Call countDown(3).", "starter_code": '#include <stdio.h>\n\n// Define countDown(n)\n\n\nint main() {\n    countDown(3);\n    return 0;\n}\n', "expected_output": "3\n2\n1", "hint": "while or for loop counting down from n to 1", "xp_reward": 20, "is_final": False},
        {"order": 3, "description": "Define printNumbers(int n) that prints 1, 2, ..., n each on a new line. Call printNumbers(4).", "starter_code": '#include <stdio.h>\n\n// Define printNumbers(n)\n\n\nint main() {\n    printNumbers(4);\n    return 0;\n}\n', "expected_output": "1\n2\n3\n4", "hint": "for loop from 1 to n, print i each time", "xp_reward": 20, "is_final": False},
        {"order": 4, "description": "Final: Define printLine(int n) that prints n dashes on one line. Call printLine(6).", "starter_code": '#include <stdio.h>\n\n// Define printLine(n)\n\n\nint main() {\n    printLine(6);\n    return 0;\n}\n', "expected_output": "------", "hint": 'Loop n times printing "-" each time', "xp_reward": 75, "is_final": True},
    ],
    "Functions Challenge": [
        {"order": 1, "description": "Create isEven(n): returns 1 if even, 0 if odd. Print: 4 is even then 7 is odd.", "starter_code": '#include <stdio.h>\n\n// Define isEven(n)\n\n\nint main() {\n    if (isEven(4)) printf("4 is even\\n"); else printf("4 is odd\\n");\n    if (isEven(7)) printf("7 is even\\n"); else printf("7 is odd\\n");\n    return 0;\n}\n', "expected_output": "4 is even\n7 is odd", "hint": "if (n % 2 == 0) return 1; return 0;", "xp_reward": 20, "is_final": False},
        {"order": 2, "description": "Create isPositive(n): returns 1 if n > 0, 0 otherwise. Test with 5 and -3.", "starter_code": '#include <stdio.h>\n\n// Define isPositive(n)\n\n\nint main() {\n    if (isPositive(5)) printf("5 is positive\\n"); else printf("5 is not positive\\n");\n    if (isPositive(-3)) printf("-3 is positive\\n"); else printf("-3 is not positive\\n");\n    return 0;\n}\n', "expected_output": "5 is positive\n-3 is not positive", "hint": "if (n > 0) return 1; return 0;", "xp_reward": 20, "is_final": False},
        {"order": 3, "description": "Create int max(int a, int b) that returns the larger number. Print: Max: 8", "starter_code": '#include <stdio.h>\n\n// Define max(a, b)\n\n\nint main() {\n    int result = max(8, 3);\n    printf("Max: %d", result);\n    return 0;\n}\n', "expected_output": "Max: 8", "hint": "if (a > b) return a; return b;", "xp_reward": 20, "is_final": False},
        {"order": 4, "description": "Final: Create absolute(n) that returns n if positive, -n if negative. Test: absolute(-7) and absolute(5).", "starter_code": '#include <stdio.h>\n\n// Define absolute(n)\n\n\nint main() {\n    printf("Absolute value: %d\\n", absolute(-7));\n    printf("Absolute value: %d", absolute(5));\n    return 0;\n}\n', "expected_output": "Absolute value: 7\nAbsolute value: 5", "hint": "if (n < 0) return -n; return n;", "xp_reward": 100, "is_final": True},
    ],
    "Mini Calculator": [
        {"order": 1, "description": "a = 10, b = 3. Use the functions to print the sum, difference and product.", "starter_code": '#include <stdio.h>\n\nint add(int a, int b) { return a + b; }\nint subtract(int a, int b) { return a - b; }\nint multiply(int a, int b) { return a * b; }\n\nint main() {\n    int a = 10, b = 3;\n    // Print: 10 + 3 = 13\n    // Print: 10 - 3 = 7\n    // Print: 10 * 3 = 30\n    \n    return 0;\n}\n', "expected_output": "10 + 3 = 13\n10 - 3 = 7\n10 * 3 = 30", "hint": 'printf("%d + %d = %d\\n", a, b, add(a,b));', "xp_reward": 30, "is_final": False},
        {"order": 2, "description": "a = 15, b = 4. Print the sum, difference and product.", "starter_code": '#include <stdio.h>\n\nint add(int a, int b) { return a + b; }\nint subtract(int a, int b) { return a - b; }\nint multiply(int a, int b) { return a * b; }\n\nint main() {\n    int a = 15, b = 4;\n    // Print: 15 + 4 = 19\n    // Print: 15 - 4 = 11\n    // Print: 15 * 4 = 60\n    \n    return 0;\n}\n', "expected_output": "15 + 4 = 19\n15 - 4 = 11\n15 * 4 = 60", "hint": "Same pattern as before, just different numbers", "xp_reward": 30, "is_final": False},
        {"order": 3, "description": "n = 5. Print: 5 squared = 25 then 5 cubed = 125", "starter_code": '#include <stdio.h>\n\nint main() {\n    int n = 5;\n    // Print: 5 squared = 25\n    // Print: 5 cubed = 125\n    \n    return 0;\n}\n', "expected_output": "5 squared = 25\n5 cubed = 125", "hint": "n*n = 25 and n*n*n = 125", "xp_reward": 30, "is_final": False},
        {"order": 4, "description": "Final: a = 12, b = 3. Print sum, difference, product AND division (12/3=4).", "starter_code": '#include <stdio.h>\n\nint add(int a, int b) { return a + b; }\nint subtract(int a, int b) { return a - b; }\nint multiply(int a, int b) { return a * b; }\n\nint main() {\n    int a = 12, b = 3;\n    // Print: 12 + 3 = 15\n    // Print: 12 - 3 = 9\n    // Print: 12 * 3 = 36\n    // Print: 12 / 3 = 4\n    \n    return 0;\n}\n', "expected_output": "12 + 3 = 15\n12 - 3 = 9\n12 * 3 = 36\n12 / 3 = 4", "hint": "Add a divide function or use a/b directly", "xp_reward": 150, "is_final": True},
    ],
    "FizzBuzz": [
        {"order": 1, "description": "Classic FizzBuzz: print numbers 1 to 15. Multiples of 3: Fizz. Multiples of 5: Buzz. Both: FizzBuzz.", "starter_code": '#include <stdio.h>\n\nint main() {\n    for (int i = 1; i <= 15; i++) {\n        // Check FizzBuzz conditions\n        \n    }\n    return 0;\n}\n', "expected_output": "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz", "hint": "Check i%15==0 first, then i%3==0, then i%5==0", "xp_reward": 30, "is_final": False},
        {"order": 2, "description": "FizzBuzz from 1 to 20.", "starter_code": '#include <stdio.h>\n\nint main() {\n    for (int i = 1; i <= 20; i++) {\n        // FizzBuzz logic\n        \n    }\n    return 0;\n}\n', "expected_output": "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n16\n17\nFizz\n19\nBuzz", "hint": "Same logic as before, just change the loop to go to 20", "xp_reward": 30, "is_final": False},
        {"order": 3, "description": "Print only the Fizz numbers from 1 to 15 (where i % 3 == 0 but NOT divisible by 15): 3, 6, 9, 12.", "starter_code": '#include <stdio.h>\n\nint main() {\n    for (int i = 1; i <= 15; i++) {\n        // Print i only if divisible by 3 but NOT by 15\n        \n    }\n    return 0;\n}\n', "expected_output": "3\n6\n9\n12", "hint": "if (i%3==0 && i%15!=0) printf(\"%d\\n\", i);", "xp_reward": 30, "is_final": False},
        {"order": 4, "description": "Final: FizzBuzz from 10 to 20.", "starter_code": '#include <stdio.h>\n\nint main() {\n    for (int i = 10; i <= 20; i++) {\n        // FizzBuzz logic\n        \n    }\n    return 0;\n}\n', "expected_output": "Buzz\n11\nFizz\n13\n14\nFizzBuzz\n16\n17\nFizz\n19\nBuzz", "hint": "Same FizzBuzz logic, loop starts at 10", "xp_reward": 150, "is_final": True},
    ],
    "C Master Challenge": [
        {"order": 1, "description": "Print a triangle of stars: row 1 has 1 star, row 2 has 2, up to row 5.", "starter_code": '#include <stdio.h>\n\nint main() {\n    // Nested loops: outer for rows, inner for stars\n    \n    return 0;\n}\n', "expected_output": "*\n**\n***\n****\n*****", "hint": "for (row=1; row<=5; row++) { for (star=1; star<=row; star++) printf(\"*\"); printf(\"\\n\"); }", "xp_reward": 50, "is_final": False},
        {"order": 2, "description": "Print a reversed triangle: row 1 has 5 stars, row 2 has 4, down to 1 star.", "starter_code": '#include <stdio.h>\n\nint main() {\n    // Reversed triangle\n    \n    return 0;\n}\n', "expected_output": "*****\n****\n***\n**\n*", "hint": "Outer loop from 5 down to 1, inner loop prints that many stars", "xp_reward": 50, "is_final": False},
        {"order": 3, "description": "Print a 4×4 square of stars (4 rows, each with 4 stars).", "starter_code": '#include <stdio.h>\n\nint main() {\n    // 4x4 square of stars\n    \n    return 0;\n}\n', "expected_output": "****\n****\n****\n****", "hint": "Outer loop for 4 rows, inner loop always prints exactly 4 stars", "xp_reward": 50, "is_final": False},
        {"order": 4, "description": "Final: Print a number triangle — row 1 prints 1, row 2 prints 12, row 3 prints 123, etc. up to row 5.", "starter_code": '#include <stdio.h>\n\nint main() {\n    // Number triangle\n    \n    return 0;\n}\n', "expected_output": "1\n12\n123\n1234\n12345", "hint": "Outer loop for rows, inner loop prints digits 1 to current row number", "xp_reward": 200, "is_final": True},
    ],
}


def seed_database(db: Session):
    if db.query(World).count() > 0:
        return

    for world_data in WORLDS_DATA:
        lessons_data = world_data.pop("lessons")
        world = World(**world_data)
        db.add(world)
        db.flush()

        for lesson_data in lessons_data:
            lesson = Lesson(world_id=world.id, **lesson_data)
            db.add(lesson)
            db.flush()

            for ex_data in EXERCISES_DATA.get(lesson_data["title"], []):
                db.add(Exercise(lesson_id=lesson.id, **ex_data))

        world_data["lessons"] = lessons_data

    db.commit()


def update_lesson_theories(db: Session):
    """Update theory and description for all lessons without touching user progress."""
    for world_data in WORLDS_DATA:
        for lesson_data in world_data["lessons"]:
            lesson = db.query(Lesson).filter(Lesson.title == lesson_data["title"]).first()
            if lesson:
                lesson.theory = lesson_data["theory"]
                lesson.description = lesson_data["description"]
                lesson.hint = lesson_data["hint"]
    db.commit()


def seed_exercises(db: Session):
    """Add exercises to existing lessons. Safe to run on an existing database."""
    from models import Exercise as Ex
    for lesson_title, exercises in EXERCISES_DATA.items():
        lesson = db.query(Lesson).filter(Lesson.title == lesson_title).first()
        if not lesson:
            continue
        if db.query(Ex).filter(Ex.lesson_id == lesson.id).count() > 0:
            continue
        for ex_data in exercises:
            db.add(Ex(lesson_id=lesson.id, **ex_data))
    db.commit()
