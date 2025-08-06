# Gemma3n-Medicine-Safety-For-Pregnant-Women

A local processing tool using Gemma 3n and EasyOCR to analyze medicine images and provide safety information for pregnant women.

## Overview
This project is a submission for the "Google - The Gemma 3n Impact Challenge". It helps pregnant women assess the safety of medications (e.g., Ciproxin) using image analysis, offering concise details on safety, dosage, risks, and alternatives.

## How to Run
- Clone the repository:
  ```bash
  git clone https://github.com/Malak310/Gemma3n-Medicine-Safety-For-Pregnant-Women.git

 # Navigate to the folder:
  cd Gemma3n-Medicine-Safety-For-Pregnant-Women
  
  # Install dependencies (e.g., transformers, easyocr, fastapi) and run:
  uvicorn main:app --host 0.0.0.0 --port 8000 --reload

Access via http://localhost:8000 or your VM IP.

# Features
Analyzes medicine images .
Provides safety info, dosage, risks, and alternatives.
User-friendly HTML/CSS interface.

# Technical Details
Uses Gemma 3n for text analysis.
Employs EasyOCR for image-to-text conversion.
- see [writeup.pdf](writeup.pdf) for full documentation.
- 
# Demo
Upload an image (e.g., Ciproxin 500) to get instant safety insights.


# Acknowledgments
Built for the Gemma 3n Impact Challenge by Google.
