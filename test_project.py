import unittest
from unittest.mock import patch
from io import StringIO
import re
import requests
from project import m8b  
from project import rps
from project import djm

#code to remove the colors from the output
def remove_ansi_escape_sequences(text):
    ansi_escape = re.compile(r'\x1b\[[0-9;]*m')
    return ansi_escape.sub('', text)

class TestMiniArcade(unittest.TestCase):

    def test_m8b(self):
        responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes, definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."
        ]
        
        with patch('builtins.input', side_effect=['Will I win?', 'quit']): #quit because we want to check it o by running it one time only
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                m8b()
                output = mock_stdout.getvalue().strip()
                output = remove_ansi_escape_sequences(output)
                
                # Check the "Thinking..." text
                self.assertIn("Thinking...", output)
                
                # Check that the Magic 8-Ball response is in the output
                self.assertTrue(any(response in output for response in responses))
                
                # Check final thank you message
                self.assertIn("Thanks for playing!", output)

    def test_rps(self):
        scenarios = [
            {'user_input': 'paper', 'computer_choice': 'rock', 'expected_output': "Computer was rock, You won!"},
            {'user_input': 'rock', 'computer_choice': 'rock', 'expected_output': "You tied! Computer was rock too!"},
            {'user_input': 'scissors', 'computer_choice': 'rock', 'expected_output': "You Lost! Computer was rock"},
        ]
        
        for scenario in scenarios:
            with patch('builtins.input', side_effect=[scenario['user_input'], 'no']): #no because we dont want to play again
                with patch('random.choice', return_value=scenario['computer_choice']):
                    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                        rps()
                        output = mock_stdout.getvalue().strip()
                        output = remove_ansi_escape_sequences(output)
                        
                        self.assertIn(scenario['expected_output'], output)
        
    def test_djm(self):
        # Simulate a network exception
        with patch('project.requests.get') as mock_requests_get:
            mock_requests_get.side_effect = requests.exceptions.RequestException("Network error")
            
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                djm()
                output = mock_stdout.getvalue().strip()
                    
                # Check if the network error message is printed
                self.assertIn("Failed to fetch a joke. Please check your internet connection.", output)
                # Ensure that "Thanks for playing!" is still printed
                self.assertIn("Thanks for playing!", output)

if __name__ == "__main__":
    unittest.main()
