import random

def run_bot():
    print("🤖 Welcome to AI Language Assistant v3!")
    
    name = input("Hi! What's your name? ")
    print(f"Nice to meet you, {name}! 😊")

    mood = input("How are you today? ")
    print("Thanks for sharing! 💬")

    start = input("Shall we start practicing? (yes / no): ").lower()

    if start != "yes":
        print("No problem! Come back anytime 👋")
        return

    language = input("Which language do you want to practice? (English / Korean): ").lower()

    print("\nChoose a topic:")
    print("1. Family")
    print("2. Hobbies")
    print("3. Work")

    topic = input("Enter 1, 2 or 3: ")

    questions = []

    if language == "english":
        if topic == "1":
            questions = [
                "Can you tell me about your family?",
                "Who are you closest to in your family?",
                "Do you live with your family?"
            ]
        elif topic == "2":
            questions = [
                "What is your favorite hobby?",
                "How often do you do your hobby?",
                "Why do you like this hobby?"
            ]
        elif topic == "3":
            questions = [
                "What do you do for work or study?",
                "What do you like about your work or studies?",
                "What are your future career plans?"
            ]
        else:
            print("Invalid choice.")
            return

    elif language == "korean":
        if topic == "1":
            questions = [
                "가족에 대해 말해 주세요.",
                "가족 중에 누구와 가장 친해요?",
                "가족과 같이 살고 있어요?"
            ]
        elif topic == "2":
            questions = [
                "취미가 뭐예요?",
                "취미를 얼마나 자주 해요?",
                "왜 그 취미를 좋아해요?"
            ]
        elif topic == "3":
            questions = [
                "무슨 일을 하세요? 또는 무엇을 공부해요?",
                "일이나 공부에서 무엇이 좋아요?",
                "미래에 어떤 일을 하고 싶어요?"
            ]
        else:
            print("선택이 잘못됐어요.")
            return

    else:
        print("Sorry, this language is not supported yet.")
        return

    print("\n🎯 Let's start!\n")

    answers = []
    for q in random.sample(questions, 2):
        print("Question:", q)
        ans = input("Your answer: ")
        answers.append(ans)

    print("\n📊 IELTS-style feedback:")

    score = random.randint(5, 7)
    print(f"Estimated speaking band: {score}.0")

    print("\n✅ Feedback:")
    print("- Try to speak a bit longer in your answers.")
    print("- Use more examples and details.")
    print("- Pay attention to grammar and pronunciation.")

    print("\n💡 Sample better answer:")
    print("I enjoy my hobby because it helps me relax and develop new skills. "
          "For example, I practice it several times a week and it makes me feel motivated.")

    print("\n🔥 Great job! You're improving every day.")
    print("Come back soon — I'll be waiting for you 🤝")
    
