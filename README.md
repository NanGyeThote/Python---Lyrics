# Bad Girls Like U Chorus Visualizer

A fun Python script that visually displays the chorus of the song "Bad Girls Like U" with colored text and a typing effect. Each line of the chorus is printed in a specific color for a vibrant and engaging output.

## Features

- Displays the chorus of "Bad Girls Like U" in vibrant colors using the `colorama` library.
- Adds a typing effect with customizable delay between words.
- Utilizes predefined lines for the chorus and cycles through multiple colors for enhanced aesthetics.

## Prerequisites

This script requires Python 3 and the following Python package:

- `colorama`

You can install `colorama` using pip:

```bash
pip install colorama
```

## Usage

1. Clone or download this repository.
2. Run the script using Python:

```bash
python bad_girls_chorus.py
```

The script will display the chorus of "Bad Girls Like U" with a colorful typing effect.

## Script Overview

The script includes:

- **Chorus Templates**: A predefined list of lines from the chorus.
- **Color Customization**: Colors are chosen cyclically from a predefined palette.
- **Typing Effect**: Each word is printed with a delay to mimic a typing animation.

### Example Output

When you run the script, you will see something like this:

```plaintext
🎵 The Chorus for 'Bad Girls Like U' 🎵

Cause I like, Bad Girls like you
Bad Girls like you
Tham Pen Mai Ru
Wa Khuen Ni Chan Mai Yak Sia Thoe Pai
Bad Girls like you, Bad Girls like you
Bad Girls like you
I like Bad Girls like you
```

Each line will appear in a different color and will display with a typing effect.

## Customization

- **Delay Between Words**: Adjust the `delay` parameter in the `generate_chorus()` function call to change the typing speed.
  
  ```python
  generate_chorus(delay=0.5)  # Adjust the delay as needed
  ```

- **Text Colors**: Modify the `text_colors` list to include your preferred colors. Available colors are provided by the `colorama.Fore` module.

  ```python
  text_colors = [Fore.RED, Fore.BLUE, Fore.GREEN, Fore.YELLOW, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
  ```

## License

This script is open source and available under the MIT License. Feel free to use, modify, and share it as you like!

## Acknowledgments

- Created with Python and the `colorama` library for colorful terminal output.
- Inspired by the song "Bad Girls Like U" for its catchy chorus!
