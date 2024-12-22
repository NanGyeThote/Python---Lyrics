import time
from colorama import Fore, Style

# Predefined lines for the chorus (in the desired order)
chorus_templates = [
    "Cause I like, Bad Girls like you",
    "Bad Girls like you",
    "Tham Pen Mai Ru",
    "Wa Khuen Ni Chan Mai Yak Sia Thoe Pai",
    "Bad Girls like you, Bad Girls like you",
    "Bad Girls like you",
    "I like Bad Girls like you"
]


text_colors = [Fore.RED, Fore.BLUE, Fore.GREEN, Fore.YELLOW, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]

def print_with_color(text, delay=0.1):
    color = text_colors[chorus_templates.index(text) % len(text_colors)] 
    print(color, end="")
    for word in text.split():
        print(word, end=" ", flush=True)
        time.sleep(delay)
    print(Style.RESET_ALL)
    print()

def generate_chorus(delay=0):
    for line in chorus_templates: 
        print_with_color(line, delay)

# Main function
if __name__ == "__main__":
    print("🎵 The Chorus for 'Bad Girls Like U' 🎵\n")
    generate_chorus(delay=0.5)  # Display the chorus with a typing effect
