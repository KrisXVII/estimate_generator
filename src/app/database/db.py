import sqlite3
import os
import sys
from pathlib import Path

def get_db_path():
    if getattr(sys, 'frozen', False):
        # Running as bundled app - use ~/Library/Application Support/
        app_name = "EstimateGenerator"
        if sys.platform == "darwin":  # macOS
            app_support_dir = Path.home() / "Library" / "Application Support" / app_name
        else:
            app_support_dir = Path.home() / "AppData" / "Roaming" / app_name

    else:
        # Development - use project root
        app_support_dir = Path(__file__).parent.parent.parent

    # Create directory if it doesn't exist
    app_support_dir.mkdir(parents=True, exist_ok=True)

    return app_support_dir / "estimates.db"

class SettingsDB:
    def __init__(self):
        self.db_path = get_db_path()
        self.init_db()

    def init_db(self):

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS business_settings(
                setting_key TEXT PRIMARY KEY,
                setting_value TEXT
        );
        ''')

        cursor.execute('SELECT COUNT(*) FROM business_settings')
        if cursor.fetchone()[0] == 0:
            defaults = [
                ('company', 'Nome Azienda'),
                ('address', "Via Roma, 28, TO"),
                ('city', 'Torino'),
                ('tax_code', "NTAPQL61S01D568L"),
                ('vat_id', "IT17556120099"),
                ('email', 'example@gmail.com')
            ]
            cursor.executemany(
                'INSERT INTO business_settings (setting_key, setting_value) VALUES (?, ?)',
                defaults
            )

        conn.commit()
        conn.close()

    def get_setting(self, key):

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            'SELECT setting_value FROM business_settings WHERE setting_key = ?',
            (key,)
        )
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else ""

    def set_setting(self, key, value):

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            'INSERT OR REPLACE INTO business_settings (setting_key, setting_value) VALUES (?, ?)',
            (key, value)
        )
        conn.commit()
        conn.close()

    def get_all_settings(self):

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT setting_key, setting_value FROM business_settings')
        settings = {row[0]: row[1] for row in cursor.fetchall()}
        conn.close()
        return settings

    def update_settings(self, settings_dict):

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        for key, value in settings_dict.items():
            cursor.execute(
                'INSERT OR REPLACE INTO business_settings (setting_key, setting_value) VALUES (?, ?)',
                (key, value)
            )

        conn.commit()
        conn.close()
