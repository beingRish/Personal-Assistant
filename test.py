# # from datetime import datetime

# # now = datetime.now()

# # current_time = now.strftime("%H : %M : %S")
# # print("Current Time =", current_time)

# from datetime import date

# today = date.today()
# print("Today's date:", today)

from gtts import gTTS
tts = gTTS('hello')
tts.save('hello.mp3')