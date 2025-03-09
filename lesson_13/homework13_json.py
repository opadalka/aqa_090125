from pathlib import Path
import logging
import json

file1_path = Path(__file__).parent / "swagger.json"
file2_path = Path(__file__).parent / "login.json"
file3_path = Path(__file__).parent / "localizations_ru.json"
file4_path = Path(__file__).parent / "localizations_en.json"

def log_event(status: str, file_path):
    log_message = f"Login event - json in {file_path} has wrong format"
    # Створення та налаштування логера
    logging.basicConfig(
        filename='json_Padalka.log',
        level=logging.ERROR,
        format='%(asctime)s - %(message)s'
        )
    logger = logging.getLogger("log_event")

    # Логування події
    if status == "Invalid":
        logger.error(log_message)
    
def validate_json(filepath):
    with open(filepath, 'r', encoding='utf8') as file:
        try:
            data = json.load(file) # put JSON-data to a variable
            print("Valid JSON")    # in case json is valid
            return data
        except json.decoder.JSONDecodeError:
            print("Invalid JSON")
            log_event("Invalid", filepath)

validate_json(file1_path)
validate_json(file2_path)
validate_json(file3_path)
validate_json(file4_path)