import pyttsx3
# audio=pyttsx3.speak('我是天才')
class TTS:
    def get_audio(self,msg):
        audio_engine=pyttsx3.init()
        rate = audio_engine.getProperty('rate')
        audio_engine.setProperty('rate', rate - 10)
       
        audio_engine.save_to_file(msg, 'speech.mp3')
        print("需要TTS的对象："+msg)
        
        audio_engine.runAndWait()
        return 'done'
    def test():
        msg='我是天才'
        audio_engine=pyttsx3.init()
        rate = audio_engine.getProperty('rate')
        audio_engine.setProperty('rate', rate - 10)
        audio_engine.say(msg)
        audio_engine.save_to_file(msg, 'speech.mp3')
        print(file)
        audio_engine.runAndWait()