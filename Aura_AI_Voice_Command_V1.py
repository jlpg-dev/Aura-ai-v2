import speech_recognition as sr
import pyttsx3
import webbrowser
import subprocess
import os
import datetime
import time

# =============================
# AURA AI - VOICE COMMAND V1
# =============================

engine = pyttsx3.init()
engine.setProperty("rate", 175)
engine.setProperty("volume", 1.0)

recognizer = sr.Recognizer()


def speak(text):
    print("Aura:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        print("\n🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        try:
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

            print("🔄 Processing...")
            command = recognizer.recognize_google(
                audio,
                language="en-IN"
            )

            command = command.lower()
            print("You:", command)
            return command

        except sr.WaitTimeoutError:
            return ""

        except sr.UnknownValueError:
            speak("Sorry, I didn't understand.")
            return ""

        except sr.RequestError:
            speak("Speech recognition service is unavailable.")
            return ""


def execute_command(command):

    if "hello" in command or "hi aura" in command:
        speak("Hello! I am Aura AI. How can I help you?")

    elif "who are you" in command:
        speak("I am Aura AI, your personal voice assistant.")

    elif "your name" in command:
        speak("My name is Aura AI.")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak("The time is " + current_time)

    elif "date" in command:
        today = datetime.datetime.now().strftime("%d %B %Y")
        speak("Today is " + today)

    elif "open chrome" in command:
        speak("Opening Chrome.")
        chrome_paths = [
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        ]
        opened = False
        for path in chrome_paths:
            if os.path.exists(path):
                subprocess.Popen(path)
                opened = True
                break
        if not opened:
            speak("Chrome was not found on your computer.")

    elif "open youtube" in command:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")

    elif "open google" in command:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")

    elif "search google for" in command:
        query = command.replace("search google for", "").strip()
        if query:
            speak("Searching Google for " + query)
            url = "https://www.google.com/search?q=" + query.replace(" ", "+")
            webbrowser.open(url)
        else:
            speak("What should I search for?")

    elif "open notepad" in command:
        speak("Opening Notepad.")
        subprocess.Popen("notepad.exe")

    elif "open calculator" in command:
        speak("Opening Calculator.")
        subprocess.Popen("calc.exe")

    elif "open file explorer" in command or "open explorer" in command:
        speak("Opening File Explorer.")
        subprocess.Popen("explorer.exe")

    elif "open command prompt" in command or "open cmd" in command:
        speak("Opening Command Prompt.")
        subprocess.Popen("cmd.exe")

    elif "open settings" in command:
        speak("Opening Windows settings.")
        os.system("start ms-settings:")

    elif "open discord" in command:
        speak("Opening Discord.")
        webbrowser.open("https://discord.com/app")

    elif "open chatgpt" in command:
        speak("Opening ChatGPT.")
        webbrowser.open("https://chatgpt.com")

    elif "open minecraft" in command:
        speak("Opening Minecraft.")
        os.system("start minecraft:")

    elif "shutdown computer" in command or "shutdown pc" in command:
        speak("Shutdown command detected. Shutting down in ten seconds.")
        os.system("shutdown /s /t 10")

    elif "cancel shutdown" in command:
        os.system("shutdown /a")
        speak("Shutdown cancelled.")

    elif "restart computer" in command or "restart pc" in command:
        speak("Restarting the computer in ten seconds.")
        os.system("shutdown /r /t 10")

    elif "lock computer" in command or "lock pc" in command:
        speak("Locking the computer.")
        os.system("rundll32.exe user32.dll,LockWorkStation")

    elif (
        "exit aura" in command
        or "close aura" in command
        or "stop aura" in command
        or "goodbye" in command
    ):
        speak("Goodbye. Aura AI is shutting down.")
        return False

    else:
        speak("I don't know that command yet.")

    return True


def main():
    print("=" * 45)
    print("        AURA AI - VOICE COMMAND V1")
    print("=" * 45)

    speak("Aura AI is online.")

    while True:
        command = listen()

        if command:
            running = execute_command(command)
            if not running:
                break

        time.sleep(0.3)


if __name__ == "__main__":
    main()
