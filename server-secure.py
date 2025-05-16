import hmac
import hashlib

SECRET_KEY = b'supersecretkey'

def generate_secure_mac(message: bytes) -> str:
    return hmac.new(SECRET_KEY, message, hashlib.sha256).hexdigest()

def verify_secure(message: bytes, mac: str) -> bool:
    #Secure verification with constant-time comparison
    expected_mac = generate_secure_mac(message)
    return hmac.compare_digest(expected_mac.encode(), mac.lower().encode())


def main():
    print("=== Secure Server ===")
    message = b"amount=100&to=alice"
    mac = generate_secure_mac(message)
    print(f"HMAC: {mac}")

if __name__ == "__main__":
    main()