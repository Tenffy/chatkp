import openai
class WhisperChat:
    openai.api_key = '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'
    def trans2Text(self,audio_file):
        open_file = audio_file

        print(open_file)
        # open_file2= open("E:/GPT/Chatkp/chatkp/audio/test.m4a", "rb")
        # print(open_file2)
        transcript = openai.Audio.transcribe_raw("whisper-1", open_file,'recorder.mp3')
        
        return transcript.text
    
    # audio_file= open("E:/GPT/Chatkp/chatkp/audio/test.m4a", "rb")
    # transcript = openai.Audio.transcribe("whisper-1", audio_file)
    # print(transcript.text)