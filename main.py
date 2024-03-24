import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import pyscreeze as pz

engine = pyttsx3.init()


def speak(audio: str) -> None:
    engine.say(audio)
    engine.runAndWait()


def time() -> None:
    time = datetime.datetime.now().strftime("%I:%M")
    speak('Current Time: '+time)


def date() -> None:
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    speak("Day: " + str(day))
    speak("Month: " + str(month))
    speak("Year: " + str(year))


def wishme() -> None:
    speak("Hello sir, how may i assist you today?")


def take_command() -> str | None:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        r.energy_threshold = 4000
        audio = r.listen(source)

    try:
        print('Recognising....')
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        print('Say that again please....')
        return None

    return query


def screenshot():
    ss = pz.screenshot()
    ss.save('../AI-bot/Screenshots/ss.png')


if __name__ == '__main__':
    wishme()
    # take_command()

    while True:
        query = take_command().lower()

        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'search web for' in query:
            search_term = query.split("for",1)[1]
            print(search_term)
            url = "https://www.google.com.tr/search?q={}".format(search_term)
            wb.open(url)

        elif 'remember' in query:
            speak('What do you want me to remember?')
            note = take_command()
            with open('data.txt', 'w') as f:
                f.write(note)

        elif 'remind' in query:
            with open('data.txt', 'r') as f:
                speak('You told me to remember that: ' + f.read())

        elif 'screenshot' in query:
            screenshot()
            speak('Screenshot taken')

        elif 'offline' in query:
            speak('Going offline, have a good day sir!')
            quit()
