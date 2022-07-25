import re
import os


def password_check(letters):
    pattern = re.compile(r"^[0-9a-zA-Z]+")
    answer = [{"success": "Password valid"}, {"failure": "Passwords not valid"}]
    processed_letters = "".join(re.findall(pattern, letters))
    return answer[0] if len(letters) <= 8 and processed_letters == letters else answer[1]


def string_generation(num):
    return os.urandom(num).hex()
