print("Welcome to your AI Language Assistant! 😊")

# 1. Узнаем имя пользователя
while True:
    name = input("What's your name? ").strip()
    if name != "":
        break
    print("Please enter your name! 😊")

print(f"Hi {name}! Let's practice languages together.\n")

# 2. Вопросы о языке
responses = {}

# Вопрос 1: какой язык учишь
while True:
    language = input("Which language are you learning? ").strip()
    if language != "":
        responses['language'] = language
        break
    print("Please type a language! 😄")

# Вопрос 2: сколько времени учишь
while True:
    duration = input(f"How long have you been learning {language}? ").strip()
    if duration != "":
        responses['duration'] = duration
        break
    print("Please type how long! ⏳")

# Вопрос 3: зачем учишь
while True:
    reason = input(f"Why do you want to learn {language}? ").strip()
    if reason != "":
        responses['reason'] = reason
        break
    print("Please tell me your reason! 😃")

# 3. Мини-игра: угадай слово
print("\nLet's play a mini game! Guess the Korean word for 'Hello'.")
guess = input("Your answer: ").strip().lower()
if guess == "annyeong":
    print("Correct! 🎉 You're amazing!")
else:
    print("Not quite 😅. The correct word is 'Annyeong'!")

# 4. Вывод всех ответов
print("\nHere’s a summary of your answers:")
for key, value in responses.items():
    print(f"{key.capitalize()}: {value}")

print("\nThanks for practicing today! Keep it up! 💪")
