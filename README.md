# PDF to MP3 Converter in Python

## Overview
This Python-based PDF to MP3 Converter is a utility that automates the conversion of text in PDF files into spoken words in the MP3 format. Utilizing the PyPDF2 library to extract text from PDFs and the pyttsx3 library for the text-to-speech process, this tool is particularly useful for those who need or prefer to consume written content audibly.

## Features
- Extract text from PDFs using `PyPDF2`.
- Convert text to speech and save as MP3 using `pyttsx3`.

## Prerequisites
- Python 3.x
- pip

## Installation
To set up the environment for the PDF to MP3 Converter, follow these steps:

- Clone the repository or download the source code to your local machine.
- Navigate to the project directory.
- Install the required dependencies:

```sh
pip install PyPDF2 pyttsx3
```
## Usage
To convert a PDF to an MP3 file, execute the script from the command line:

```sh
python pdf_to_mp3.py <path_to_pdf> [options]
```
Where <path_to_pdf> should be replaced with the path to your PDF file.

## Code Structure
- pdf_to_mp3.py: The main script that includes functions for extracting text and converting it to speech.
- requirements.txt: A file that lists the Python dependencies for this project.