from setup import DEFAULT_SETTINGS
from read_modify_write import use_settings_and_process


if __name__ == "__main__":
    print("Settings:")
    print(DEFAULT_SETTINGS.get_value("hostname"))  # → "{"hostname":"192.168.1.1","port_number":8080}"
    print(DEFAULT_SETTINGS.get_value("port_number"))  
    use_settings_and_process()
    print("Settings now:")
    print(DEFAULT_SETTINGS.get_value("hostname"))  # → "{"hostname":"192.168.1.1","port_number":3000}"
    print(DEFAULT_SETTINGS.get_value("port_number"))  
    use_settings_and_process() 
    print("Settings now:")
    print(DEFAULT_SETTINGS.get_value("hostname"))  # → "{"hostname":"192.168.1.1","port_number":3000}"
    print(DEFAULT_SETTINGS.get_value("port_number"))


