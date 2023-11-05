import argparse
import PyPDF2
import pyttsx3

# Set up argument parser
parser = argparse.ArgumentParser(description='Convert PDF to speech with customizable options.')
parser.add_argument('--rate', type=int, default=150, help='Speech rate (words per minute)')
parser.add_argument('--volume', type=float, default=1.0, help='Volume (min=0.0, max=1.0)')
parser.add_argument('--voice', type=str, help='Voice ID to use')
parser.add_argument('pdf_file', type=str, help='Path to the PDF file')

# Parse command-line arguments
args = parser.parse_args()

# Initialize the reader and the speaker
reader = PyPDF2.PdfReader(open(args.pdf_file, 'rb'))
speaker = pyttsx3.init()

# Set customizable speech parameters
speaker.setProperty('rate', args.rate)
speaker.setProperty('volume', args.volume)

# Set the voice
if args.voice:
    voices = speaker.getProperty('voices')
    for voice in voices:
        if voice.id == args.voice:
            speaker.setProperty('voice', voice.id)
            break
    else:
        print(f"Voice ID {args.voice} not found. Using default voice.")

# Process the PDF and convert to speech
cleanText = ''
for page in range(len(reader.pages)):
    text = reader.pages[page].extract_text()
    cleanText += text.strip().replace('\n', ' ')

# Save the spoken text to a file
output_file = args.pdf_file.replace('.pdf', '.mp3')
speaker.save_to_file(cleanText, output_file)

# Add a closing statement to the speech (optional)
speaker.say('The end')

# Process all the speech commands
speaker.runAndWait()

# Stop the speaker if needed
speaker.stop()

print(f"Conversion complete. The audio file has been saved as {output_file}")
