class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def ask_question(self, question):
        print(question['text'])
        for index, option in enumerate(question['options'], start=1):
            print(f"{index}. {option}")

        user_answer = input("Select your answer (enter the option number): ")
        return user_answer

    def run_quiz(self):
        for question in self.questions:
            user_answer = self.ask_question(question)
            if user_answer == str(question['answer']):
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Incorrect! The correct answer is: {question['options'][question['answer'] - 1]}\n")

        print(f"Quiz Completed!\nYour score: {self.score}/{len(self.questions)}")
        if self.score == len(self.questions):
            print("Great job! You got all the questions right.")
        elif self.score >= len(self.questions) // 2:
            print("Not bad! You did well.")
        else:
            print("Keep practicing. You can do better!")

def main():
    questions = [
        {
            'text': "What is the capital of France?",
            'options': ["Paris", "London", "Berlin"],
            'answer': 1
        },
        {
            'text': "Which planet is known as the 'Red Planet'?",
            'options': ["Mars", "Venus", "Jupiter"],
            'answer': 1
        },
        {
            'text': "What is the largest mammal?",
            'options': ["Elephant", "Blue Whale", "Giraffe"],
            'answer': 2
        }

    ]

    print("Welcome to the Quiz Game!")
    print("You will be presented with multiple-choice questions.")
    
    play_again = True
    while play_again:
        quiz = Quiz(questions)
        quiz.run_quiz()

        play_again_input = input("Do you want to play again? (yes/no): ")
        play_again = play_again_input.lower() == "yes"

    print("Thank you for playing!")

if __name__ == "__main__":
    main()
