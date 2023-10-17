import PyPDF2
import os
from gtts import gTTS


def extract_text(filepath):
    text = ""
    pdf_reader = PyPDF2.PdfReader(filepath)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text


def text_to_speech(content, filepath):
    tts = gTTS(content, lang='en')
    tts.save(filepath)


def main():
    path = "chapter1.pdf"
    output_path = "result.mp3"
    text = extract_text(filepath=path)
    text_to_speech(content=text, filepath=output_path)
    os.system("start result.mp3")


if __name__ == "__main__":
    main()
