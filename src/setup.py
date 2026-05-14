
from pickledb import PickleDB


SETTINGS_FILENAME = "settings.json"     # Default filename for settings storage.


class Settings:
    def __init__(self, filename: str = SETTINGS_FILENAME):
        self.db = PickleDB(filename)  
        self.db.load()

    def set_value(self, key: str, value: any):
        self.db.set(key, value)
        self.db.save()

    def get_value(self, key: str):
        return self.db.get(key)
    

DEFAULT_SETTINGS = Settings()   # Global instance of Settings for use across the application. 
                                # NOTE: will create "settings.json" in the current directory if it doesn't exist.


# ********************** Functional test **********************
if __name__ == "__main__":
    settings = Settings("test_settings.json")  # Use a test file to avoid overwriting real settings.
    settings.set_value("hostname", "192.168.1.120")
    settings.set_value("port_number", 8080)
    # Readback
    print(settings.get_value("hostname"))  # → "192.168.1.120"
    print(settings.get_value("port_number"))  # → 8080


