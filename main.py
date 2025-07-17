
from parser import extract_text_from_pdf
from validator import is_text_valid
from gpt_extractor import extract_with_gpt
from supabase_client import insert_to_supabase
from uuid import uuid4
from datetime import datetime, timezone
import os, json

PDF_PATH = "/Users/tharukagamage/Desktop/DMS Serendia/Araliya Beach Unawatuna Summer 2025.pdf"

def main():
    pdf_filename = os.path.basename(PDF_PATH)
    text = extract_text_from_pdf(PDF_PATH)
    validation_score = sum([kw in text.lower() for kw in ["room", "rate", "season", "check-in", "child"]]) * 20
    extracted_text_length = len(text)
    method = "native"
    structured_data = {}

    if not is_text_valid(text):
        print("Using GPT-4 for extraction...")
        method = "gpt"
        gpt_output = extract_with_gpt(text)
        try:
            structured_data = json.loads(gpt_output)
        except json.JSONDecodeError:
            print("GPT-4 response is not valid JSON")
            return
    else:
        print("Native parsing not implemented. Using GPT for now.")
        method = "gpt"
        gpt_output = extract_with_gpt(text)
        structured_data = json.loads(gpt_output)

    record = {
        "id": str(uuid4()),
        "pdf_filename": pdf_filename,
        "hotel_name": structured_data.get("hotel_name"),
        "hotel_location": structured_data.get("hotel_location"),
        "hotel_contact": structured_data.get("hotel_contact"),
        "rate_seasons": structured_data.get("rate_seasons"),
        "room_categories": structured_data.get("room_categories"),
        "meal_plans": structured_data.get("meal_plans"),
        "check_in_time": structured_data.get("check_in_time"),
        "check_out_time": structured_data.get("check_out_time"),
        "child_policy": structured_data.get("child_policy"),
        "cancellation_policy": structured_data.get("cancellation_policy"),
        "processing_method": method,
        "validation_score": validation_score,
        "extracted_text_length": extracted_text_length,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "updated_at": datetime.now(timezone.utc).isoformat()
    }

    insert_to_supabase("hotels_rate_data", record)
    print("Done.")

if __name__ == "__main__":
    main()
