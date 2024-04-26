from collections import deque
import re

def is_palindrome(s):
    # Перетведення рядка у нижній регістр та видалення всіх символів окрім літер 
    normalized_str = re.sub(r'[\W_]', '', s.lower())
    
    # створення deque з символів нормалізованого рядка
    char_deque = deque(normalized_str)
    
    # Перевірка, чи збігаються символи з обох кінців
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True


print(is_palindrome("A man, a plan, a canal, Panama"))  #  True
print(is_palindrome("Was it a car or a cat I saw?"))  #  True
print(is_palindrome("No 'x' in Nixon"))  #  True
print(is_palindrome("Hello, World"))  #  False
