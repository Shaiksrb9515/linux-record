import pygame

def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

if __name__ == "__main__":
    audio_file = "C:\\Users\\shaik\\OneDrive\\Desktop\\py\\1.mp3"  # Replace with your audio file path
    play_audio(audio_file)
