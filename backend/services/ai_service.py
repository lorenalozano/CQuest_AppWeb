import re

ERROR_EXPLANATIONS = [
    (r"undeclared|was not declared", "You're using a variable or function that hasn't been created yet! Make sure you declare it before using it. For example: int myNumber = 0; creates a variable called myNumber. You've got this!"),
    (r"expected ';'|expected ';' before", "Looks like you forgot a semicolon! In C, every statement needs to end with a ; — it's like a period at the end of a sentence. Check the line the error points to. You're so close!"),
    (r"expected '\)'|expected '\('", "There's a missing parenthesis! Make sure every opening ( has a closing ). Count them — they must match! Keep trying!"),
    (r"expected '\}'|expected '\{'", "There's a missing curly brace! Every { needs a matching }. Check your main() function — it should end with }. You've got this!"),
    (r"implicit declaration of function", "You're calling a function that C doesn't know about yet! Make sure you have #include <stdio.h> at the top of your file if you're using printf. Great try!"),
    (r"too few arguments|too many arguments", "The function is getting the wrong number of inputs! Check how many values it expects and make sure you provide exactly that many. So close!"),
    (r"incompatible types|invalid conversion", "You're mixing different types of data! For example, putting text where a number is expected. Check what type of variable you're using. Keep it up!"),
    (r"No such file or directory", "The #include file wasn't found! Make sure you wrote #include <stdio.h> exactly like that, with < and > around it. You're doing great!"),
    (r"format '%d'|format '%f'|format '%s'", "The format in your printf doesn't match the variable type! Use %d for whole numbers (int), %f for decimal numbers (float). Almost there!"),
    (r"unused variable", "You created a variable but never used it! Either use it in your code, or remove it if you don't need it. Great attention to detail!"),
    (r"division by zero", "Oops! You can't divide by zero — that's impossible in math too! Make sure the number you're dividing by is never 0. You've got this!"),
    (r"linker|undefined reference", "The program compiled but couldn't link! This usually means you called a function that doesn't exist. Check for typos in function names. Keep trying!"),
]

EXERCISES_BY_WORLD = {
    1: [
        {
            "title": "Say Hello!",
            "description": "Make the computer print the message 'Hello, Coder!' on the screen. Use printf to show your message!",
            "starter_code": '#include <stdio.h>\n\nint main() {\n    // Print Hello, Coder!\n    \n    return 0;\n}\n',
            "expected_output": "Hello, Coder!",
            "hint": "Use printf(\"Hello, Coder!\"); inside main()",
        },
        {
            "title": "Two Lines",
            "description": "Print two lines: 'Line 1' and 'Line 2'. Each on its own line!",
            "starter_code": '#include <stdio.h>\n\nint main() {\n    // Print Line 1 and Line 2 on separate lines\n    \n    return 0;\n}\n',
            "expected_output": "Line 1\nLine 2",
            "hint": "Use \\n inside printf to create a new line!",
        },
    ],
    2: [
        {
            "title": "Your Age",
            "description": "Create an integer variable with value 12 and print 'I am 12 years old'.",
            "starter_code": '#include <stdio.h>\n\nint main() {\n    // Create int variable age = 12\n    \n    // Print: I am 12 years old\n    \n    return 0;\n}\n',
            "expected_output": "I am 12 years old",
            "hint": "Use int age = 12; then printf(\"I am %d years old\", age);",
        },
        {
            "title": "Multiply",
            "description": "Create two variables: a = 6 and b = 7. Multiply them and print 'Result: 42'.",
            "starter_code": '#include <stdio.h>\n\nint main() {\n    int a = 6;\n    int b = 7;\n    // Calculate result and print it\n    \n    return 0;\n}\n',
            "expected_output": "Result: 42",
            "hint": "int result = a * b; then printf(\"Result: %d\", result);",
        },
    ],
    3: [
        {
            "title": "Positive Check",
            "description": "Given number = 5, print 'Positive' if it's greater than 0, otherwise 'Not positive'.",
            "starter_code": '#include <stdio.h>\n\nint main() {\n    int number = 5;\n    // Check if positive\n    \n    return 0;\n}\n',
            "expected_output": "Positive",
            "hint": "Use if (number > 0) { printf(\"Positive\"); }",
        },
        {
            "title": "Big or Small",
            "description": "Given x = 20, print 'Big' if x >= 10, otherwise print 'Small'.",
            "starter_code": '#include <stdio.h>\n\nint main() {\n    int x = 20;\n    // Check if big or small\n    \n    return 0;\n}\n',
            "expected_output": "Big",
            "hint": "Use if (x >= 10) to check the condition",
        },
    ],
    4: [
        {
            "title": "Count to 3",
            "description": "Use a for loop to print the numbers 1, 2, and 3, each on a new line.",
            "starter_code": '#include <stdio.h>\n\nint main() {\n    // Use a for loop to print 1, 2, 3\n    \n    return 0;\n}\n',
            "expected_output": "1\n2\n3",
            "hint": "for(int i = 1; i <= 3; i++) then printf(\"%d\\n\", i)",
        },
        {
            "title": "Repeat Star",
            "description": "Use a loop to print the * character 4 times on the same line.",
            "starter_code": '#include <stdio.h>\n\nint main() {\n    // Print **** using a loop\n    \n    return 0;\n}\n',
            "expected_output": "****",
            "hint": "Loop 4 times and printf(\"*\") each time, without \\n",
        },
    ],
    5: [
        {
            "title": "Say Hi Function",
            "description": "Create a function called sayHi() that prints 'Hi there!' and call it from main.",
            "starter_code": '#include <stdio.h>\n\n// Define sayHi() here\n\n\nint main() {\n    // Call sayHi()\n    \n    return 0;\n}\n',
            "expected_output": "Hi there!",
            "hint": "Define void sayHi() { printf(\"Hi there!\"); } before main",
        },
        {
            "title": "Double It",
            "description": "Create a function double(n) that returns n*2. Print the result of double(5).",
            "starter_code": '#include <stdio.h>\n\n// Define double function\n\n\nint main() {\n    // Print the result of doubling 5\n    \n    return 0;\n}\n',
            "expected_output": "10",
            "hint": "int doubleIt(int n) { return n * 2; } then printf(\"%d\", doubleIt(5));",
        },
    ],
    6: [
        {
            "title": "Mini Stats",
            "description": "Given a=8 and b=2, print their sum, difference and product each on a new line.",
            "starter_code": '#include <stdio.h>\n\nint main() {\n    int a = 8, b = 2;\n    // Print sum, difference and product\n    \n    return 0;\n}\n',
            "expected_output": "10\n6\n16",
            "hint": "Use three printf calls with a+b, a-b, and a*b",
        },
    ],
}


async def generate_hint(lesson_title: str, theory: str, code: str, error: str | None) -> str:
    if error:
        explanation = _explain_error_text(error)
        return f"Great try! I see there's a compiler error. {explanation}"

    has_printf = "printf" in code
    has_include = "#include" in code
    has_return = "return 0" in code

    if not has_include:
        return "Great try! Don't forget to add #include <stdio.h> at the very top of your file — it gives your program the power to print things! You're so close!"
    if not has_printf:
        return "You're on the right track! Now you need to use printf() to print your message. Put it inside the main() function. You've got this!"
    if not has_return:
        return "Almost there! Make sure your main() function ends with return 0; before the closing }. Keep it up!"

    return f"Great try! You're working on '{lesson_title}'. Read the theory section carefully — it has an example that matches exactly what you need to do. You've got this!"


async def explain_error(error_message: str, code: str) -> str:
    return _explain_error_text(error_message)


async def generate_exercise(world_number: int, topic: str) -> dict:
    import random
    exercises = EXERCISES_BY_WORLD.get(world_number, EXERCISES_BY_WORLD[1])
    return random.choice(exercises)


def _explain_error_text(error_message: str) -> str:
    for pattern, explanation in ERROR_EXPLANATIONS:
        if re.search(pattern, error_message, re.IGNORECASE):
            return explanation
    return "There's a small mistake in your code! Read the error message carefully — it tells you the line number where the problem is. Fix it one step at a time. You've got this!"
