# Gemma3n-Medicine-Safety-For-Pregnant-Women

A local processing tool using Gemma 3n and EasyOCR to analyze medicine images and provide safety information for pregnant women.

## Overview
This project is a submission for the "Google - The Gemma 3n Impact Challenge". It helps pregnant women assess the safety of medications (e.g., Ciproxin 500) using image analysis, offering concise details on safety, dosage, risks, and alternatives.

## How to Run
### Step 1: Clone the Repository
```bash
git clone https://github.com/Malak310/Gemma3n-Medicine-Safety-For-Pregnant-Women.git
```
### Step 2: Navigate to the Folder
```bash
cd Gemma3n-Medicine-Safety-For-Pregnant-Women
```
### Step 3: Install Dependencies
Install the required Python libraries:
```
pip install transformers easyocr fastapi uvicorn Pillow torch
```
Note: Ensure Python 3.8+ and pip are installed. Use a virtual environment if possible (python -m venv venv then source venv/bin/activate on Linux/VM).
Note1: Ensure you logged in Hugging Face first, and have an access token to the "model google/gemma-3n-E2b-it".

### Step 4: Run the Application
```
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
Access via http://localhost:8000 or your VM IP (e.g., http://172.161.51.38:8000).

## Features
Analyzes medicine images to extract text.
Provides safety info, dosage, risks, and alternatives for pregnant women.
Offers a user-friendly HTML/CSS interface.

## Technical Details
Uses Gemma 3n-E2b-it for text analysis and safety insights.
Employs EasyOCR for image-to-text conversion.
- see [writeup.pdf](writeup.pdf) for full documentation.

## Project Setup Details
Dependencies: Requires transformers (Gemma 3n), easyocr (OCR), fastapi and uvicorn (server), Pillow (image processing), and torch (model inference).
Hardware: Needs at least 8GB RAM; a GPU is recommended for speed.
Image Prep: Use clear, high-res images (e.g., 700x700 pixels) for best OCR.

### Common Issues:
Slow Response: Gemma 3n may be slow; reduce max_new_tokens to 350 or use a GPU.
OCR Errors: Retry with clearer images or adjust preprocessing (threshold to 180).
Port Conflicts: Ensure port 8000 is free; change if needed (e.g., --port 8001).

## Demo
Upload an image (e.g., Ciproxin 500) to get instant safety insights.
https://youtu.be/VNSp0hg4Kag?si=wdJmxHR9akV1dtu9

### Note
The model may respond slowly due to its size and processing needs, causing inference delays. Test with small images first.

###Acknowledgments
Built for the Gemma 3n Impact Challenge by Google.



