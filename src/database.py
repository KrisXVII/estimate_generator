import sqlite3
import os
import sys
from pathlib import Path


class SettingsDB:
    def __init__(self):
        self.db_path = self.get_db_path()
        self.init_db()

    def get_db_path(self):

        if getattr(sys, 'frozen', False):
            base_path = Path(sys.executable).parent
        else:
            base_path = Path(__file__).parent.parent
        return base_path / "estimates.db"

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
                ('company', 'La Tua Azienda'),
                ('address', 'Il Tuo Indirizzo'),
                ('city', 'Torino'),
                ('tax_code', 'CODICEFISCALE'),
                ('vat_id', 'IT01234567890'),
                ('email', 'example@gmail.com')
            ]
            cursor.executemany(
                'INSERT INTO business_settings (setting_key, setting_value) VALUES (?, ?)',
                defaults
            )
            print("Default settings inserted")

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
