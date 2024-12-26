class TextCleaner:
    @staticmethod
    def clean(text):
        return ''.join(c.lower() for c in text if c.isalnum())

class PalindromeChecker:
    def __init__(self, text):
        self.text = text

    def is_palindrome(self):
        cleaned_text = TextCleaner.clean(self.text)
        return self._check_palindrome(cleaned_text)

    def _check_palindrome(self, text):
        return text == text[::-1]


user_input = input("Please enter a word to check if it's a palindrome: ")
palindrome_checker = PalindromeChecker(user_input)

if palindrome_checker.is_palindrome():
    print(f"'{user_input}' is a palindrome.")
else:
    print(f"'{user_input}' is not a palindrome.")
