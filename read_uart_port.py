import serial
from serial.tools.list_ports import comports

if __name__ == "__main__":

    # List available serial ports
    available_ports = comports()
    list_of_port_names = []
    print("Available ports:")
    for port in available_ports:
        list_of_port_names.append(port.device)
        print(f"\t{port.device}")

    # Confirm UART port is available
    expected_uart_port = "/dev/ttyS0"
    if not list_of_port_names.__contains__(expected_uart_port):
        raise ValueError(f"Expected UART Port {expected_uart_port} not found!")

    # Create serial port object
    baud_rate = 9600
    ser = serial.Serial(expected_uart_port, baudrate=baud_rate)

    # Begin reading serial port
    print("\nBeginning to read GP1818MK GPS Module data...\n")
    while True:
        value = ser.readline()
        value_string = str(value, 'UTF-8').strip()
        print(value_string)