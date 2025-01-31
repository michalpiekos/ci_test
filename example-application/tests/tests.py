import pytest
import serial
import time

# Define the serial port and baud rate (update this based on your setup)
SERIAL_PORT = "/dev/ttyACM1"
BAUD_RATE = 115200
TIMEOUT = 2

@pytest.fixture(scope="module")
def serial_connection():
    """Fixture to set up and tear down the serial connection."""
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=TIMEOUT)
    time.sleep(1)
    yield ser
    ser.close()

def send_command(ser, command, expected_output, timeout=2):
    """Send a command to the Zephyr shell and check the expected output."""
    ser.write((command + "\n").encode())
    time.sleep(0.5)

    response = []
    start_time = time.time()
    while time.time() - start_time < timeout:
        line = ser.readline().decode().strip()
        if line:
            response.append(line)
            if expected_output in line:
                return response

    pytest.fail(f"Expected output '{expected_output}' not found. Response: {response}")

def test_shell_help(serial_connection):
    """Test if Zephyr shell responds correctly to the help command."""
    send_command(serial_connection, "help", "Available commands:")

if __name__ == "__main__":
    pytest.main()

