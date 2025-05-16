import hashlib

SECRET_KEY = b'supersecretkey'  # Unknown to attacker

def generate_mac(message: bytes) -> str:
    return hashlib.md5(SECRET_KEY + message).hexdigest()

def verify(message: bytes, mac: str) -> bool:
    expected_mac = generate_mac(message)
    return mac == expected_mac

def main():
    # Example message
    message = b"amount=100&to=alice"
    mac = generate_mac(message)
    print("=== Server Simulation ===")
    print(f"Original message:{message.decode()}")
    print(f"Original MAC:{mac}")
    print("\n----Verifying legitimate message----\n")
    if verify(message, mac):
        print("MAC verified successfully. Message is authentic.\n")
    # Simulated attacker-forged message:

    forged_message = b"amount=100&to=alice" + b"&admin=true"
    #we will paste here the forged message from client.py
    #forged_message = b'amount=100&to=alice\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x01\x00\x00\x00\x00\x00\x00&admin=true'

    forged_mac = mac
    #we will paste here the forged mac from client.py
    #forged_mac = "97312a73075b6e1589117ce55e0a3ca6"
    print("----Verifying forged message----:\n")
    if verify(forged_message, forged_mac):
        print("MAC verified successfully (UNEXPECTED)")
    else:
        print("MAC verification failed (EXPECTED)")

if __name__ == "__main__":
    main()