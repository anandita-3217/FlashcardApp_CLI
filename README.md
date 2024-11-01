# Flashcard CLI Application
A command-line interface (CLI) application for creating and studying flashcards, built with Python.

## Overview
This Flashcard CLI Application is a simple yet powerful tool that helps users create, manage, and study with digital flashcards. The application features a text-based interface, making it lightweight and easy to use across different platforms.

## Features
- 📝 Create individual flashcards with questions and answers
- 🔄 Update existing flashcards
- 🗑️ Delete flashcards or entire decks
- 👀 View all flashcards in the deck
- 📊 Track deck size (maximum 150 cards)
- 📥 Import flashcards from JSON files
- 📝 Interactive quiz mode with three difficulty levels

### Quiz Modes
- Beginner: 5 questions
- Mid: 10 questions
- Pro: 15 questions

Each quiz has a 60-second time limit and provides immediate feedback on answers.

## Installation
1. Ensure you have Python 3.x installed on your system
2. Clone this repository or download the source code
3. No additional dependencies required! The application uses only Python standard library modules:
   - `random`
   - `time`
   - `json`

## Usage
1. Run the application:
```bash
python project.py
```

2. Select from the following menu options:
```
1. Add Flashcard
2. Update Flashcard
3. Delete Flashcard
4. View Deck
5. Upload Deck (from JSON)
6. Delete Deck
7. Take Quiz
8. View Deck Size
9. Exit
```

### Example JSON Format for Deck Upload
```json
{
    "What is Python?": "A high-level programming language",
    "Who created Python?": "Guido van Rossum",
    "When was Python released?": "1991"
}
```

## Project Structure
The project consists of two main classes:

### FlashcardDeck Class
- Core functionality for flashcard management
- Handles data storage and retrieval
- Implements quiz logic
- Manages deck operations (add, update, delete)
- Handles JSON file imports

### FlashcardApp Class
- Implements the command-line interface
- Manages user interaction
- Displays menus and prompts
- Handles user input and validation

## Features in Detail

### Flashcard Management
- **Add Flashcards**: Create individual cards with questions and answers
- **Update Flashcards**: Modify answers for existing questions
- **Delete Flashcards**: Remove individual cards or clear entire deck
- **View Deck**: Display all flashcards in an easy-to-read format

### Quiz System
- Three difficulty levels with different question counts
- Randomized question selection
- Case-insensitive answer checking
- Score tracking and immediate feedback
- Time limit implementation

### Input Validation
- Prevents duplicate questions
- Checks for empty or whitespace-only inputs
- Validates deck size limits
- Ensures proper JSON format for deck imports

## Error Handling
The application includes robust error handling for:
- File operations
- JSON parsing
- Input validation
- Deck size limitations
- Quiz requirements

## Future Improvements
Potential enhancements for future versions:
1. Persistent storage (save decks between sessions)
2. Multiple deck support
3. Custom quiz configurations
4. Progress tracking
5. Export functionality
6. Category tagging for flashcards
7. Search and filter capabilities



