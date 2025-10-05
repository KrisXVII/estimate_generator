import json
import sys
from pathlib import Path

def get_config_path():
    if getattr(sys, 'frozen', False):
        base_path = Path(sys.executable).parent
    else:
        base_path = Path(__file__).parent.parent
    return base_path / "business_config.json"


class ConfigManager:
    def __init__(self):
        self.config_path = get_config_path()
        self.default_config = {
            "company_name": "Nome Azienda",
            "address": "Indirizzo",
            "phone": "Telefono",
            "tax_code": "Codice Fiscale",
            "email": "email@azienda.com"
        }

    def load_config(self):
        if self.config_path.exists():
            try:
                with open(self.config_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                print(f"Error loading config: {e}")
                return self.default_config.copy()
        return self.default_config.copy()

    def save_config(self, config_data):
        try:
            with open(self.config_path, 'w', encoding='utf-8') as f:
                json.dump(config_data, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error saving config: {e}")
            return False
