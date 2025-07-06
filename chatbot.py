# 💫 MahiNova 
import datetime
import random

#  TIME-BASED GREETING
def time_based_greeting():
    hour = datetime.datetime.now().hour
    if hour < 12:
        print("🌅 Good Morning! Subah ho gayi MahiNova ke saath!")
    elif hour < 18:
        print("🌞 Good Afternoon! Aaj kya seekhenge hum?")
    else:
        print("🌙 Good Evening! Ready ho MahiNova ke saath chill karne?")

#  RULE-BASED CHATBOT
def rule_based_chat():
    print("💬 Type something! (type 'exit' to stop)")
    while True:
        msg = input("You: ").lower()
        if 'exit' in msg:
            break
        elif 'hello' in msg or 'hi' in msg:
            print("MahiNova: Hello ji! Kaise ho?")
        elif 'name' in msg:
            print("MahiNova: Mera naam hai MahiNova, aapki digital dost!")
        elif 'how are you' in msg:
            print("MahiNova: Main ek chatbot hoon, emotions nahi par code toh mast hai 😎")
        else:
            print("MahiNova: Mujhe ye samajh nahi aaya 😅")

#  TO-DO LIST 
def todo_list():
    try:
        with open("tasks.txt", "r") as f:
            tasks = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        tasks = []

    while True:
        print("\n📋 To-Do Options:\n1. Add Task\n2. View Tasks\n3. Remove Task\n4. Back")
        choice = input("Choose: ")

        if choice == '1':
            task = input("➕ Enter task: ")
            tasks.append(task)
            with open("tasks.txt", "w") as f:
                for t in tasks:
                    f.write(t + "\n")
            print("✅ Task added!")
        elif choice == '2':
            if not tasks:
                print("📭 Koi task nahi hai abhi.")
            else:
                for i, t in enumerate(tasks, 1):
                    print(f"{i}. {t}")
        elif choice == '3':
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
            try:
                num = int(input("❌ Enter task number to remove: "))
                removed = tasks.pop(num - 1)
                with open("tasks.txt", "w") as f:
                    for t in tasks:
                        f.write(t + "\n")
                print(f"✅ Removed: {removed}")
            except:
                print("⚠️ Invalid input")
        elif choice == '4':
            break
        else:
            print("⚠️ Invalid choice")

#  MOOD TRACKER 
def mood_tracker():
    mood = input("🧠 Aaj aapka mood kaisa hai? (happy/sad/angry/ok): ").lower()
    responses = {
        "happy": "😁 Mast! Aise hi khush raho!",
        "sad": "😢 Koi baat nahi, sab theek ho jayega.",
        "angry": "😠 Gussa thoda control karo, deep breath lo.",
        "ok": "🙂 Theek hai, chal aage badhte hain!"
    }
    print("MahiNova:", responses.get(mood, "Main samajh nahi payi, par main yahin hoon ❤️"))
    note = input("📝 Kuch note karna chahoge? (optional): ")
    with open("mood_log.txt", "a") as f:
        f.write(f"{datetime.datetime.now().strftime('%Y-%m-%d')} - Mood: {mood}\n")
        if note:
            f.write(f"   Note: {note}\n")
        f.write("\n")
    print("✅ Mood saved!")

# MENTAL HEALTH SUPPORT
def mental_health():
    print("🧘‍♀️ Let’s relax together. Breathe in... Breathe out...")
    affirmations = [
        "✨ Main strong hoon.",
        "🌈 Main deserve karta/ti hoon khushi.",
        "🌟 Har din ek nayi shuruaat hai.",
        "💖 Main apne liye enough hoon."
    ]
    print(random.choice(affirmations))

#  HOROSCOPE 
def horoscope():
    month = input("🔮 Birth month? (jan/feb/...): ").lower()
    facts = {
        "jan": "🧠 Intelligent and strong-willed!",
        "feb": "💘 Romantic and deep thinkers!",
        "mar": "🔥 Full of passion and energy!",
        "apr": "💪 Natural born leaders!",
        "may": "🌸 Artistic and charming!",
        "jun": "😄 Always cheerful and curious!",
        "jul": "🌊 Emotional and intuitive!",
        "aug": "👑 Confident and fearless!",
        "sep": "📚 Perfectionist and wise!",
        "oct": "⚖️ Balanced and fair!",
        "nov": "🕵️‍♀️ Mysterious and intense!",
        "dec": "🎉 Fun-loving and ambitious!"
    }
    print(facts.get(month, "😅 Sorry, galat month dala kya?"))

#  LANGUAGE TRANSLATOR 
def language_translator():
    word = input("🌐 Enter English word: ").lower()
    dictionary = {
        "hello": "नमस्ते",
        "bye": "अलविदा",
        "love": "प्यार",
        "friend": "दोस्त",
        "food": "खाना",
        "happy": "खुश"
    }
    print("🗣️ Hindi Translation:", dictionary.get(word, "❌ Word not found."))

#  RANDOM JOKE 
def random_joke():
    jokes = [
        "😂 Teacher: Why are you late?\nStudent: Sir, I saw a board 'School Ahead', so I went home!",
        "😆 What’s a computer’s favorite snack? Microchips!",
        "🤣 Why don’t scientists trust atoms? Because they make up everything!",
    ]
    print(random.choice(jokes))

#  FAKE CUSTOMER SUPPORT
def fake_support():
    print("📞 Welcome to MahiNova Customer Support")
    print("1. Order status\n2. Refund\n3. Talk to agent")
    opt = input("Select: ")
    if opt == '1':
        print("📦 Your order is on the way, expected in 2-3 days.")
    elif opt == '2':
        print("💸 Refund initiated. Amount will be credited soon.")
    elif opt == '3':
        print("🎧 All agents are busy. Please wait... forever 😅")
    else:
        print("❌ Invalid option")

# MAIN MENU 
def main():
    time_based_greeting()
    while True:
        print("\n📜 MahiNova Menu:")
        print("1. Rule-Based Chat")
        print("2. To-Do List")
        print("3. Mood Tracker")
        print("4. Mental Health Support")
        print("5. Horoscope")
        print("6. Language Translator")
        print("7. Joke Bot")
        print("8. Fake Customer Support")
        print("9. Time-Based Greeting")
        print("0. Exit")
        choice = input("🔢 Choose (0-9): ")

        if choice == '1':
            rule_based_chat()
        elif choice == '2':
            todo_list()
        elif choice == '3':
            mood_tracker()
        elif choice == '4':
            mental_health()
        elif choice == '5':
            horoscope()
        elif choice == '6':
            language_translator()
        elif choice == '7':
            random_joke()
        elif choice == '8':
            fake_support()
        elif choice == '9':
            time_based_greeting()
        elif choice == '0':
            print("👋 Bye from MahiNova! Phir milenge. Keep Coding 🚀")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

# Run the chatbot
main()
