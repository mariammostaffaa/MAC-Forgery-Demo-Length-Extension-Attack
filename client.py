import hashpumpy # type: ignore
import hashlib
import hmac  
from urllib.parse import quote
from colorama import Fore, Style, init  # type: ignore

init(autoreset=True)

# Server's verify function (copied for testing)
SECRET_KEY = b'supersecretkey'  # For testing; attacker doesn't know this

def generate_mac(message: bytes) -> str:
    return hashlib.md5(SECRET_KEY + message).hexdigest()

def verify(message: bytes, mac: str) -> bool:
    expected_mac = generate_mac(message)
    return hmac.compare_digest(mac.encode(), expected_mac.encode())

def perform_attack():
    print(f"\n{Fore.YELLOW}=== LENGTH EXTENSION ATTACK DEMO ===")
    print(f"{Style.DIM}Demonstrating why hash(secret||message) is vulnerable{Style.RESET_ALL}")
    
    # Intercepted values
    intercepted_message = b"amount=100&to=alice"
    intercepted_mac = input(f"{Fore.CYAN}Enter intercepted MAC from server.py: {Style.RESET_ALL}").strip()
    data_to_append = b"&admin=true"

    print(f"\n{Fore.WHITE}Attempting attack with key length guess: 14 bytes")
    
    try:
        new_mac, new_message = hashpumpy.hashpump(
            intercepted_mac,
            intercepted_message,
            data_to_append,
            14  # Correct length for 'supersecretkey'
        )
    except Exception as e:
        print(f"{Fore.RED}Error: {e}")
        print(f"Ensure hashpumpy is installed (pip install hashpumpy){Style.RESET_ALL}")
        return

    print(f"{Style.BRIGHT}Original message: {Fore.WHITE}{intercepted_message.decode()}")
    print(f"{Style.BRIGHT}Original MAC: {Fore.WHITE}{intercepted_mac}")
    print(f"\n{Style.BRIGHT}Forged message: {Fore.WHITE}{quote(new_message.decode('latin1'))}")
    print(f"{Style.BRIGHT}Forged MAC: {Fore.WHITE}{new_mac}")

    # Verify the attack
    if verify(new_message, new_mac):
        print(f"\n{Fore.GREEN}✓ Server accepted forged message!")
        print(f"{Style.DIM}This proves the MAC implementation is vulnerable{Style.RESET_ALL}")
    else:
        print(f"\n{Fore.RED}✗ Attack failed (unexpected)")

    print(f"\n{Fore.YELLOW}=== NEXT STEPS ===")
    print(f"1. Copy these values into server.py")
    print(f"2. Compare with secure_server.py's resistance")

if __name__ == "__main__":
    perform_attack()