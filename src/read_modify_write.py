from setup import DEFAULT_SETTINGS
import time


def use_settings_and_process():
    # Get port number from settings
    port_number = DEFAULT_SETTINGS.get_value("port_number")
    portnum_ok = port_number is not None and isinstance(port_number, int) and 0 < port_number < 5000
    # If port number is valid, do some processing (placeholder)
    if portnum_ok:
        print(f"Port number {port_number} is valid. Proceeding with processing...")
    else:
        print(f"Port number {port_number} is INVALID (not set or >5000). Forcing to 3000.")
        DEFAULT_SETTINGS.set_value("port_number", 3000)
    # Process data with the (possibly updated) port number:
    print(f"Processing with port number: {DEFAULT_SETTINGS.get_value('port_number')}")
    time.sleep(3)  # Simulate processing time
    print("Processing complete.")

