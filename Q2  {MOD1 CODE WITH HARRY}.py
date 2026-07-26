# Q (2)install a external module and use it
# i intall pyttsx in terminal
import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("i am no longer surrounded with darkness,i am the bloody darkness myself")
engine.runAndWait()