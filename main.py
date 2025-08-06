from fastapi import FastAPI, UploadFile, File, Request
from transformers import AutoModelForImageTextToText, AutoTokenizer
from PIL import Image, ImageFilter
import os
import easyocr
import torch
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI(title="Medicine Safety for Pregnancy")

# Load Gemma 3n
model_name = "google/gemma-3n-E2b-it"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForImageTextToText.from_pretrained(model_name, torch_dtype="auto", device_map="auto")

# OCR Reader
reader = easyocr.Reader(['en'])

# Templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/analyze-image/")
async def analyze_image(request: Request, file: UploadFile = File(...), lang: str = "en"):
    with open("temp_image.jpg", "wb") as buffer:
        buffer.write(await file.read())

    # Enhanced image preprocessing
    pil_img = Image.open("temp_image.jpg").convert("L")
    pil_img = pil_img.filter(ImageFilter.MedianFilter(size=3))  # Reduce noise
    pil_img_threshold = pil_img.point(lambda x: 0 if x < 180 else 255)
    pil_img_sharp = pil_img_threshold.filter(ImageFilter.SHARPEN)
    pil_img_resized = pil_img_sharp.resize((700, 700), Image.LANCZOS)

    # Extract text with EasyOCR
    result = reader.readtext("temp_image.jpg", detail=0, paragraph=True, text_threshold=0.7)
    extracted_text = " ".join(result) if result else ""
    print(f"Extracted text: {extracted_text}")

    # Analyze with Gemma (request concise summaries)
    prompt = f"Based on the text: '{extracted_text}', identify the medicine name and provide a concise summary (2-3 sentences each) for safety for pregnant women, dosage, risks, and alternatives. Output only the analysis without repeating the prompt or instructions."
    inputs = tokenizer(prompt, return_tensors="pt", padding=True)
    outputs = model.generate(**inputs, max_new_tokens=350)
    full_description = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Improved medicine name extraction
    medicine_name = "unknown"
    if "Medicine Name:" in full_description:
        name_part = full_description.split("Medicine Name:")[1].split("\n")[0].strip()
        if name_part:
            medicine_name = name_part
    elif full_description:
        words = [w for w in full_description.split() if any(c.isupper() for c in w) and len(w) > 3]
        if words:
            medicine_name = words[0]  # Fallback

    # Clean up
    os.remove("temp_image.jpg")
    return templates.TemplateResponse("index.html", {
        "request": request,
        "medicine_name": medicine_name,
        "full_description": full_description
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)