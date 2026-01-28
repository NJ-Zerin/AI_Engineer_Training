import speech_recognition as sr
import webbrowser
import pyttsx3
import time
import os
import datetime
import sys
import random
import threading

r = sr.Recognizer()
engine = pyttsx3.init()

# Configure speech engine for better performance
engine.setProperty('rate', 150)    # Speed of speech
engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

def speak(text):
    global engine
    print("[JARVIS SPEAKING]: " + text)
    try:
        engine.say(text)
        engine.runAndWait()
        time.sleep(0.3)
        print("[SPEECH COMPLETED]")
    except Exception as e:
        print("[SPEECH ERROR]: " + str(e))
        try:
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()
        except:
            print("[SPEECH REINITIALIZATION FAILED]")

def reminder_alert(message, minutes):
    """Function to handle reminder in a separate thread"""
    time.sleep(minutes * 60)
    speak("Reminder: " + message)
    print("[REMINDER ALERT]: " + message)

def processCommand(c):
    print("[PROCESSING COMMAND]: '" + c + "'")
    c = c.lower()
    
    # Exit commands - CHECK THIS FIRST
    if any(word in c for word in ['stop listening', 'exit', 'quit', 'goodbye', 'shutdown']):
        print("[EXIT COMMAND DETECTED]")
        speak("Goodbye! Have a great day!")
        time.sleep(1)
        return "EXIT"
    
    # Stop music command
    elif 'stop music' in c or 'pause music' in c or 'stop playing' in c:
        print("[STOP MUSIC COMMAND]")
        speak("Stopping music")
        try:
            os.system("osascript -e 'tell application \"Music\" to pause'")
            print("[STOPPED]: Apple Music")
        except Exception as e:
            print("[ERROR]: Could not stop music - " + str(e))
        return True
    
    # Music commands - Play on Apple Music and YouTube Music
    elif 'play' in c and not 'display' in c:
        song = c.replace('play', '').replace('music', '').replace('song', '').replace('the', '').strip()
        
        if song and len(song) > 2:
            print("[MATCH FOUND]: Play music - " + song)
            speak("Playing " + song)
            time.sleep(0.5)
            
            try:
                print("[ATTEMPTING]: Apple Music playback")
                applescript = 'tell application "Music" to activate'
                os.system("osascript -e '{}'".format(applescript))
                time.sleep(1)
                
                applescript = 'tell application "Music" to play (search playlist 1 for "{}")'.format(song)
                os.system("osascript -e '{}'".format(applescript))
                print("[PLAYING]: " + song + " on Apple Music")
                
            except Exception as e:
                print("[ERROR]: Apple Music playback failed - " + str(e))
            
            time.sleep(1)
            webbrowser.open("https://music.youtube.com/search?q=" + song.replace(' ', '+'))
            print("[OPENED]: YouTube Music search for " + song)
            
        else:
            speak("What song would you like me to play?")
        return True
    
    # Reminder System
    elif 'remind me' in c:
        try:
            words = c.split()
            minutes = None
            reminder_text = c
            
            # Extract minutes from command
            for i, word in enumerate(words):
                if word.isdigit():
                    if i + 1 < len(words) and 'minute' in words[i + 1]:
                        minutes = int(word)
                        # Extract reminder message
                        reminder_text = c.split('to')[1].split('in')[0].strip() if 'to' in c else "your reminder"
                        break
            
            if minutes:
                speak("I will remind you in " + str(minutes) + " minutes about " + reminder_text)
                print("[REMINDER SET]: " + str(minutes) + " minutes - " + reminder_text)
                # Run reminder in separate thread so it doesn't block
                reminder_thread = threading.Thread(target=reminder_alert, args=(reminder_text, minutes))
                reminder_thread.daemon = True
                reminder_thread.start()
            else:
                speak("Please specify the time in minutes")
        except Exception as e:
            print("[ERROR]: Reminder failed - " + str(e))
            speak("Sorry, I couldn't set the reminder")
        return True
    
    # Open Applications
    elif 'open' in c and not any(site in c for site in ['youtube', 'google', 'stackoverflow']):
        if 'notes' in c:
            os.system('open -a Notes')
            speak("Opening Notes")
            print("[OPENED]: Notes app")
        elif 'calculator' in c:
            os.system('open -a Calculator')
            speak("Opening Calculator")
            print("[OPENED]: Calculator app")
        elif 'calendar' in c:
            os.system('open -a Calendar')
            speak("Opening Calendar")
            print("[OPENED]: Calendar app")
        elif 'safari' in c:
            os.system('open -a Safari')
            speak("Opening Safari")
            print("[OPENED]: Safari")
        elif 'chrome' in c:
            os.system('open -a "Google Chrome"')
            speak("Opening Chrome")
            print("[OPENED]: Chrome")
        elif 'vscode' in c or 'visual studio' in c or 'vs code' in c:
            os.system('open -a "Visual Studio Code"')
            speak("Opening VS Code")
            print("[OPENED]: VS Code")
        elif 'finder' in c:
            os.system('open -a Finder')
            speak("Opening Finder")
            print("[OPENED]: Finder")
        elif 'terminal' in c:
            os.system('open -a Terminal')
            speak("Opening Terminal")
            print("[OPENED]: Terminal")
        else:
            return False
        return True
    
    # Take Screenshot
    elif 'screenshot' in c or 'capture screen' in c or 'take picture' in c:
        try:
            import pyautogui
            speak("Taking screenshot")
            time.sleep(0.5)
            screenshot = pyautogui.screenshot()
            filename = "screenshot_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".png"
            screenshot.save(filename)
            speak("Screenshot saved as " + filename)
            print("[SAVED]: " + filename)
        except ImportError:
            speak("Screenshot feature requires pyautogui. Please install it using pip install pyautogui pillow")
            print("[ERROR]: pyautogui not installed")
        except Exception as e:
            speak("Sorry, I couldn't take the screenshot")
            print("[ERROR]: Screenshot failed - " + str(e))
        return True
    
    # Create Folder
    elif 'create folder' in c or 'make folder' in c:
        folder_name = c.replace('create folder', '').replace('make folder', '').replace('named', '').replace('called', '').strip()
        if folder_name and len(folder_name) > 1:
            try:
                os.makedirs(folder_name, exist_ok=True)
                speak("Folder " + folder_name + " created successfully")
                print("[CREATED]: Folder - " + folder_name)
            except Exception as e:
                speak("Sorry, I couldn't create the folder")
                print("[ERROR]: Folder creation failed - " + str(e))
        else:
            speak("Please specify a folder name")
        return True
    
    # Create File
    elif 'create file' in c or 'make file' in c:
        file_name = c.replace('create file', '').replace('make file', '').replace('named', '').replace('called', '').strip()
        if file_name and len(file_name) > 1:
            try:
                if '.' not in file_name:
                    file_name += '.txt'
                open(file_name, 'w').close()
                speak("File " + file_name + " created successfully")
                print("[CREATED]: File - " + file_name)
            except Exception as e:
                speak("Sorry, I couldn't create the file")
                print("[ERROR]: File creation failed - " + str(e))
        else:
            speak("Please specify a file name")
        return True
    
    # Volume Control
    elif 'volume up' in c or 'increase volume' in c or 'raise volume' in c:
        try:
            os.system("osascript -e 'set volume output volume (output volume of (get volume settings) + 10)'")
            speak("Volume increased")
            print("[ACTION]: Volume increased")
        except Exception as e:
            speak("Sorry, I couldn't change the volume")
            print("[ERROR]: Volume control failed - " + str(e))
        return True
    
    elif 'volume down' in c or 'decrease volume' in c or 'lower volume' in c:
        try:
            os.system("osascript -e 'set volume output volume (output volume of (get volume settings) - 10)'")
            speak("Volume decreased")
            print("[ACTION]: Volume decreased")
        except Exception as e:
            speak("Sorry, I couldn't change the volume")
            print("[ERROR]: Volume control failed - " + str(e))
        return True
    
    elif 'mute' in c and 'unmute' not in c:
        try:
            os.system("osascript -e 'set volume output muted true'")
            speak("Muted")
            print("[ACTION]: Muted")
        except Exception as e:
            speak("Sorry, I couldn't mute")
            print("[ERROR]: Mute failed - " + str(e))
        return True
    
    elif 'unmute' in c:
        try:
            os.system("osascript -e 'set volume output muted false'")
            speak("Unmuted")
            print("[ACTION]: Unmuted")
        except Exception as e:
            speak("Sorry, I couldn't unmute")
            print("[ERROR]: Unmute failed - " + str(e))
        return True
    
    # Brightness Control
    elif 'brightness up' in c or 'increase brightness' in c:
        try:
            # For macOS, use brightness command line tool
            os.system("brightness 1")  # Increase brightness
            speak("Brightness increased")
            print("[ACTION]: Brightness increased")
        except Exception as e:
            speak("Sorry, I couldn't change the brightness. You may need to install brightness control tool")
            print("[ERROR]: Brightness control failed - " + str(e))
        return True
    
    elif 'brightness down' in c or 'decrease brightness' in c:
        try:
            os.system("brightness 0.5")  # Decrease brightness
            speak("Brightness decreased")
            print("[ACTION]: Brightness decreased")
        except Exception as e:
            speak("Sorry, I couldn't change the brightness. You may need to install brightness control tool")
            print("[ERROR]: Brightness control failed - " + str(e))
        return True
    
    # Battery Status
    elif 'battery' in c or 'battery status' in c or 'power' in c:
        try:
            battery_info = os.popen('pmset -g batt').read()
            if '%' in battery_info:
                # Extract percentage
                percentage = battery_info.split('\t')[1].split(';')[0]
                status = "charging" if "charging" in battery_info.lower() else "discharging"
                speak("Battery is at " + percentage + " and " + status)
                print("[BATTERY]: " + percentage + " - " + status)
            else:
                speak("Could not get battery status")
        except Exception as e:
            speak("Sorry, I couldn't check the battery status")
            print("[ERROR]: Battery check failed - " + str(e))
        return True
    
    # Wikipedia search
    elif 'wikipedia' in c:
        query = c.replace('wikipedia', '').replace('search', '').strip()
        if query and len(query) > 2:
            print("[MATCH FOUND]: Wikipedia - " + query)
            speak("Searching Wikipedia for " + query)
            time.sleep(0.5)
            wiki_query = query.replace(' ', '_')
            webbrowser.open("https://en.wikipedia.org/wiki/" + wiki_query)
            print("[OPENED]: Wikipedia - " + query)
        else:
            speak("What would you like to search on Wikipedia?")
        return True
    
    # Website commands
    elif 'youtube' in c and 'music' not in c:
        print("[MATCH FOUND]: YouTube")
        speak("Opening YouTube")
        time.sleep(0.5)
        webbrowser.open("https://www.youtube.com")
        print("[OPENED]: YouTube")
        return True
        
    elif 'google' in c:
        print("[MATCH FOUND]: Google")
        speak("Opening Google")
        time.sleep(0.5)
        webbrowser.open("https://www.google.com")
        print("[OPENED]: Google")
        return True
        
    elif 'stackoverflow' in c or 'stack overflow' in c:
        print("[MATCH FOUND]: Stack Overflow")
        speak("Opening Stack Overflow")
        time.sleep(0.5)
        webbrowser.open("https://stackoverflow.com")
        print("[OPENED]: Stack Overflow")
        return True
    
    # Search on Google
    elif 'search' in c:
        query = c.replace('search', '').replace('google', '').replace('for', '').strip()
        if query and len(query) > 2:
            print("[MATCH FOUND]: Google Search - " + query)
            speak("Searching for " + query)
            time.sleep(0.5)
            webbrowser.open("https://www.google.com/search?q=" + query.replace(' ', '+'))
            print("[OPENED]: Google search for " + query)
        else:
            speak("What would you like me to search?")
        return True
    
    # Time command
    elif 'time' in c:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        print("[MATCH FOUND]: Time")
        speak("The current time is " + current_time)
        return True
    
    # Date command
    elif 'date' in c or 'today' in c:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        print("[MATCH FOUND]: Date")
        speak("Today is " + current_date)
        return True
    
    # News command
    elif 'news' in c:
        print("[MATCH FOUND]: News")
        speak("Opening latest news")
        time.sleep(0.5)
        webbrowser.open("https://news.google.com")
        print("[OPENED]: Google News")
        return True
    
    # Weather command
    elif 'weather' in c:
        print("[MATCH FOUND]: Weather")
        speak("Opening weather forecast")
        time.sleep(0.5)
        webbrowser.open("https://www.google.com/search?q=weather")
        print("[OPENED]: Weather")
        return True
    
    # Email command
    elif 'email' in c or 'gmail' in c or 'mail' in c:
        print("[MATCH FOUND]: Email")
        speak("Opening Gmail")
        time.sleep(0.5)
        webbrowser.open("https://mail.google.com")
        print("[OPENED]: Gmail")
        return True
    
    else:
        print("[NO MATCH FOUND]")
        speak("Command not recognized. Please try again.")
        return False

if __name__ == "__main__":
    print("[STARTING JARVIS]")
    print("=" * 60)
    print("JARVIS - Your Personal Voice Assistant")
    print("=" * 60)
    speak("Initializing Jarvis")
    jarvis_active = False
    
    while True:
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.5)
                
                if jarvis_active:
                    print("\n[JARVIS ACTIVE]: Listening for command...")
                else:
                    print("\n[LISTENING]: Waiting for wake word...")
                
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
            
            word = r.recognize_google(audio)
            print("[RECOGNIZED]: '" + word + "'")
            
            # Check if Jarvis wake word is detected
            if 'jarvis' in word.lower():
                print("[WAKE WORD DETECTED]")
                jarvis_active = True
                
                # Check if command is in same sentence
                command_after_jarvis = word.lower().replace('jarvis', '').strip()
                print("[TEXT AFTER JARVIS]: '" + command_after_jarvis + "'")
                
                if len(command_after_jarvis) > 3:
                    print("[COMMAND IN SAME SENTENCE]")
                    success = processCommand(command_after_jarvis)
                    if success == "EXIT":
                        print("[EXITING JARVIS]")
                        sys.exit(0)
                    if success:
                        jarvis_active = False
                else:
                    print("[WAITING FOR COMMAND]")
                    speak("Yes, how can I help you?")
            
            # If Jarvis is active, process any command (even without wake word)
            elif jarvis_active:
                print("[PROCESSING AS ACTIVE COMMAND]")
                success = processCommand(word)
                if success == "EXIT":
                    print("[EXITING JARVIS]")
                    sys.exit(0)
                if success:
                    jarvis_active = False
                else:
                    jarvis_active = False
            
            else:
                print("[WAKE WORD NOT DETECTED - Ignoring]")
                
        except sr.WaitTimeoutError:
            print("[TIMEOUT]: No speech detected")
            if jarvis_active:
                speak("I didn't hear anything.")
                jarvis_active = False
            
        except sr.UnknownValueError:
            print("[UNKNOWN]: Could not recognize speech")
            if jarvis_active:
                speak("Sorry, I didn't understand that.")
                jarvis_active = False
            
        except sr.RequestError as e:
            print("[API ERROR]: " + str(e))
            
        except KeyboardInterrupt:
            print("\n[KEYBOARD INTERRUPT]")
            speak("Shutting down Jarvis")
            sys.exit(0)
            
        except Exception as e:
            print("[UNEXPECTED ERROR]: " + str(e))
    
  