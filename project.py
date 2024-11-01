import random
import time
import json

# Class for flashcards and their management
class FlashcardDeck:
    MAX_DECK_SIZE = 150  # size of deck

    # Initialize flashcard deck as a dictionary - flashcards as key-value pairs
    def __init__(self):
        self.deck = {}

    # Will be called when viewing the cards.
    def __str__(self):
        if not self.deck:
            return "No cards to show"
        return "\n".join([f"Q: {question} - A: {answer}" for question, answer in self.deck.items()])

    @property
    def card_count(self):
        return len(self.deck)

    # Helper functions
    def _is_deck_full(self):
        return len(self.deck) >= FlashcardDeck.MAX_DECK_SIZE

    def _flashcard_exists(self, question):
        return question in self.deck

    def _handle_existing_flashcard(self, question):
        return f"Flashcard with question '{question}' already exists."

    # Main functions
    def update_flashcard(self, question, new_answer):
        if self._flashcard_exists(question):
            if (question.isspace() or new_answer.isspace()): 
                return "Invalid question and answer pairing"
            self.deck[question] = new_answer
            return f"Flashcard '{question}' updated!"
        else:
            return f"Flashcard '{question}' does not exist"

    # Will add a single card
    def add_flashcard(self, question, answer):
        if self._flashcard_exists(question):
            return self._handle_existing_flashcard(question)
        if self._is_deck_full():
            return "Deck size reached"
        if (question.isspace() or answer.isspace()): 
            return "Invalid question and answer pairing"
        if (question == "" or answer == ""): 
            return "No question or answer entered"
        self.deck[question] = answer
        return f"Flashcard '{question}' added"

    # Will add an entire deck
    def add_deck(self, new_flashcards):
        for question, answer in new_flashcards.items():
            if self._flashcard_exists(question):
                self._handle_existing_flashcard(question)
            else:
                if self._is_deck_full():
                    return f"Deck size cannot exceed {FlashcardDeck.MAX_DECK_SIZE} flashcards."
                self.deck[question] = answer
        return "Deck added!"

    # Upload a .json file containing the cards
    def upload_deck(self, filepath):
        try:
            with open(filepath, 'r') as file:
                new_flashcards = json.load(file)
                return self.add_deck(new_flashcards)
        except FileNotFoundError:
            return "File not found. Please check the file path and try again."
        except json.JSONDecodeError:
            return "Invalid JSON format. Please check the file content."

    # Deletes card by question
    def delete_card(self, question):
        if question in self.deck:
            del self.deck[question]
            return f"Flashcard '{question}' deleted"
        if question.isspace() or question == "":
            return "Invalid question format"
        else:
            return f"Flashcard '{question}' not found in deck"

    # Delete an entire deck
    def delete_deck(self):
        if self.card_count == 0:
            return "Deck empty!"
        self.deck.clear()
        return "Deck deleted!"

    # Size of deck
    def deck_size(self):
        return len(self.deck)

    # Prints all flashcards in the deck
    def view_deck(self):
        return str(self)

    # Returns the quiz details as a dictionary on what questions to display
    def quiz(self, level, shuffle=True):
        time_limit = 60
        
        if level == 'beginner' and self.card_count < 5:
            return f"Error: Not enough flashcards for {level} level quiz."
        elif level == 'mid' and self.card_count < 10:
            return f"Error: Not enough flashcards for {level} level quiz."
        elif level == 'pro' and self.card_count < 15:
            return f"Error: Not enough flashcards for {level} level quiz."

        num_questions = 5 if level == 'beginner' else 10 if level == 'mid' else 15
        questions = list(self.deck.items())  # Get all flashcards

        # Shuffle the questions for user and don't for the tests 
        if shuffle:
            questions = random.sample(questions, num_questions)
        else:
            questions = questions[:num_questions]

        return {
            "questions": questions,
            "time_limit": time_limit
        }

    # Returns a boolean value if true if the user_answer is correct else false
    def check_answer(self, current_question_index, user_answer, questions):
        _, correct_answer = questions[current_question_index]
        is_correct = user_answer.lower() == correct_answer.lower()
        return is_correct


# CLI for Flashcard App
class FlashcardApp:
    def __init__(self):
        self.deck = FlashcardDeck()

    def run(self):
        while True:
            print("\nFlashcard App")
            print("1. Add Flashcard")
            print("2. Update Flashcard")
            print("3. Delete Flashcard")
            print("4. View Deck")
            print("5. Upload Deck (from JSON)")
            print("6. Delete Deck")
            print("7. Take Quiz")
            print("8. View Deck Size")
            print("9. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.add_flashcard()
            elif choice == '2':
                self.update_flashcard()
            elif choice == '3':
                self.delete_flashcard()
            elif choice == '4':
                print(self.deck.view_deck())
            elif choice == '5':
                self.upload_deck()
            elif choice == '6':
                print(self.deck.delete_deck())
            elif choice == '7':
                self.quiz()
            elif choice == '8':
                print(f"Deck size: {self.deck.deck_size()}")
            elif choice == '9':
                print("Exiting the app.")
                break
            else:
                print("Invalid choice, please try again.")

    def add_flashcard(self):
        question = input("Enter the question: ")
        answer = input("Enter the answer: ")
        result = self.deck.add_flashcard(question, answer)
        print(result)

    def update_flashcard(self):
        question = input("Enter the question to update: ")
        new_answer = input("Enter the new answer: ")
        result = self.deck.update_flashcard(question, new_answer)
        print(result)

    def delete_flashcard(self):
        question = input("Enter the question to delete: ")
        result = self.deck.delete_card(question)
        print(result)

    def upload_deck(self):
        filepath = input("Enter the JSON file path: ")
        result = self.deck.upload_deck(filepath)
        print(result)

    def quiz(self):
        level = input("Enter quiz level (beginner, mid, pro): ").lower()
        result = self.deck.quiz(level)

        if isinstance(result, dict) and "error" in result:
            print(result["error"])
            return

        questions = result.get("questions", [])
        score = 0
        for i, (question, correct_answer) in enumerate(questions):
            user_answer = input(f"Question {i + 1}: {question}\nYour answer: ")
            if self.deck.check_answer(i, user_answer, questions):
                score += 1
                print("Correct!")
            else:
                print(f"Wrong! The correct answer was: {correct_answer}")

        print(f"Quiz completed! Your score: {score}/{len(questions)}")

def main():
    FlashcardApp().run()

if __name__ == "__main__":
    main()
