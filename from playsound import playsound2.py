from playsound import playsound

def play_audio(file_path):
    playsound(file_path)

if __name__ == "__main__":
    audio_file = "C:\\Users\\shaik\\OneDrive\\Desktop\\py\\Recording1.flac"  # Replace with your audio file path
    play_audio(audio_file)