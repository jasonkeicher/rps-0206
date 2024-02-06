import random
from rps import get_computer_choice

def test_get_computer_choice():
    random.seed(42)  # Set a seed for reproducibility
    
    # Test 1: Check if the returned choice is one of the valid choices
    choice = get_computer_choice()
    assert choice in ['rock', 'paper', 'scissors'], f"Invalid choice: {choice}"
    
    # Test 2: Check if the function returns a different choice on subsequent calls
    choice1 = get_computer_choice()
    choice2 = get_computer_choice()
    assert choice1 != choice2, f"Choices are not different: {choice1}, {choice2}"
    
    # Test 3: Check if the function returns a random choice
    choices = []
    for _ in range(100):
        choice = get_computer_choice()
        choices.append(choice)
    unique_choices = set(choices)
    assert len(unique_choices) == 3, f"Expected 3 unique choices, but got {len(unique_choices)}"
    
    print("All tests passed!")

test_get_computer_choice()