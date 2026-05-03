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
                "theory": """In C, every program starts with a main() function.
To print text, we use printf().
Don't forget to include <stdio.h> at the top!

Example:
#include <stdio.h>
int main() {
    printf("Hello!");
    return 0;
}""",
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
                "theory": """\\n inside quotes creates a new line.
You can print anything between the quotes in printf().

Example:
printf("My name is Alex\\n");""",
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
                "theory": """You can use printf() multiple times.
Each call prints on the same line unless you use \\n.

printf("Line 1\\n");
printf("Line 2\\n");
printf("Line 3\\n");""",
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
                "description": "Create a variable to store the number 42 and print it!",
                "theory": """Variables store data. An int stores whole numbers.
int myNumber = 10;
printf("%d", myNumber);  // prints 10

%d is a placeholder for integers in printf.""",
                "starter_code": '#include <stdio.h>\n\nint main() {\n    // Create an int variable called age with value 12\n    \n    // Print it using printf and %d\n    \n    return 0;\n}\n',
                "expected_output": "My age is 12",
                "hint": "Use int age = 12; then printf(\"My age is %d\", age);",
                "xp_reward": 50,
                "is_final_project": False,
            },
            {
                "order": 2,
                "title": "Float Variables",
                "description": "Store the number 3.14 in a float variable and print it!",
                "theory": """float stores decimal numbers.
float pi = 3.14;
printf("%.2f", pi);  // prints 3.14

%.2f means: print 2 decimal places.""",
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
                "theory": """You can do math with variables!
int a = 5;
int b = 3;
int sum = a + b;
printf("Sum: %d", sum);  // prints Sum: 8""",
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
                "theory": """Area = width * height
In C, * means multiply.
int width = 8;
int height = 5;
int area = width * height;""",
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
                "theory": """if checks a condition. If true, runs the block.
int x = 10;
if (x > 0) {
    printf("Positive!");
}""",
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
                "theory": """else runs when the if condition is false.
if (x % 2 == 0) {
    printf("Even");
} else {
    printf("Odd");
}
% is modulo - gives remainder of division.""",
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
                "theory": """else if adds more conditions:
if (score >= 90) {
    printf("A");
} else if (score >= 70) {
    printf("B");
} else {
    printf("C");
}""",
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
                "theory": """Combine what you learned:
- Use if/else
- Compare with >=
- Print different messages""",
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
                "theory": """A for loop repeats code.
for (int i = 1; i <= 5; i++) {
    printf("%d\\n", i);
}
i starts at 1, runs while i <= 5, adds 1 each time.""",
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
                "theory": """while loops repeat while condition is true.
int i = 3;
while (i >= 1) {
    printf("%d\\n", i);
    i--;  // i-- subtracts 1
}""",
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
                "theory": """Use a variable to accumulate values:
int sum = 0;
for (int i = 1; i <= 10; i++) {
    sum = sum + i;
}
printf("Sum: %d", sum);""",
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
                "theory": """Use a loop and multiply:
for (int i = 1; i <= 5; i++) {
    printf("3 x %d = %d\\n", i, 3*i);
}""",
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
                "theory": """Functions are reusable code blocks.
void greet() {
    printf("Hello!");
}
int main() {
    greet();  // call it
    return 0;
}
void means it returns nothing.""",
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
                "theory": """Functions can take inputs (parameters) and return values.
int add(int a, int b) {
    return a + b;
}
int result = add(5, 3);  // result = 8""",
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
                "theory": """Combine functions and loops!
void printStars(int n) {
    for (int i = 0; i < n; i++) {
        printf("*");
    }
    printf("\\n");
}""",
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
                "theory": """int isEven(int n) {
    if (n % 2 == 0) return 1;
    return 0;
}
Then use it:
if (isEven(4)) printf("4 is even\\n");""",
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
                "theory": """Combine everything you learned:
- Variables for a and b
- Functions for each operation
- printf to show results""",
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
                "theory": """FizzBuzz is a classic challenge!
for i 1 to 15:
  if divisible by both 3 and 5: FizzBuzz
  else if divisible by 3: Fizz
  else if divisible by 5: Buzz
  else: the number
Check 3 AND 5 FIRST using &&.""",
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
                "theory": """Nested loops: a loop inside a loop!
for (int row = 1; row <= 5; row++) {
    for (int star = 1; star <= row; star++) {
        printf("*");
    }
    printf("\\n");
}""",
                "starter_code": '#include <stdio.h>\n\nint main() {\n    // Print a triangle: row 1=1 star, row 2=2 stars, ..., row 5=5 stars\n    \n    return 0;\n}\n',
                "expected_output": "*\n**\n***\n****\n*****",
                "hint": "Use two nested for loops. Outer loop for rows 1-5, inner loop prints that many stars",
                "xp_reward": 200,
                "is_final_project": True,
            },
        ],
    },
]


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

        world_data["lessons"] = lessons_data

    db.commit()
