
import random

questions = {
    "What is the output of 2 ** 3 in Python": "8" ,
    "What is the result of 10 // 3 in python": "3" ,
    "Which symbol is used to comment in python": "#" ,
    "What keyword is used to import a module in python": "import" ,
    "What function is used to get input from the user?": "input" ,
    "What is the keyword to define a function in Python?": "def" ,
    "What is the correct file extension for Python files?": ".py" ,
    "What is the output of 7 // 4 in Python": "1" ,
    "What is the output of 7 // 5 in Python": "1" ,
    "How do you start a for loop in Python?": "for"
}

def trivia_game():
    questions_list = list(questions.keys())
    total_questions = 5
    score = 0

    selected_questions = random.sample(questions_list, total_questions)

    for idx, question in enumerate(selected_questions):
        print (f"{idx+1}. {question}")
        user_answer = input("What is your answer?: ").lower().strip()
        correct_answer = questions[question]

        match user_answer == correct_answer:
            case True:
                print("Correct!\n")
                score += 1

            case False:
                print(f"wrong. The correct answer is: {correct_answer}.\n")

    print (f"Game over! Your final score is: {score}/{total_questions}")


trivia_game()


