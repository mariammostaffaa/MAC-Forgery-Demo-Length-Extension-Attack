# MAC Forgery Attack Demonstration & Mitigation  
**Course**: Data Integrity and Authentication  
**Team Members**:  
- Mariam Mostafa Amin (2205084)  
- Hannah Emad Eldin (2205123)  
- Nada Mohamed Abdelsatar (2205173)  

---

## Assignment Overview  
This project demonstrates:  
1. **Length Extension Attacks** on naive MAC implementations (`hash(secret || message)`).  
2. **Mitigation** using HMAC-SHA256 with secure key management.  

---

## Files  
| File | Purpose |  
|------|---------|  
| `server.py` | Vulnerable server using `MD5(secret + message)` |  
| `client.py` | Attack script performing length extension |  
| `secure_server.py` | Secure server with HMAC-SHA256 and key rotation |  

---

##  Setup  

### Prerequisites  
```bash
pip install hmac hashlib python-dotenv

```
## Usage

- Run Vulnerable Server
```bash
python server.py
# Output: Shows MAC for "amount=100&to=alice"
```
- Execute Attack
```bash
python client.py
# Enter intercepted MAC when prompted
# Output: Forged message with admin privileges
```
- Test Secure Server
```bash
python secure_server.py
# Output: Rejects tampered messages
```
## Key Security Features
### Secure Server (secure_server.py)
#### Feature	                      Implementation
HMAC-SHA256	                   hmac.new(key, message, hashlib.sha256)
Key Rotation	                Auto-rotates keys every 90 days
Input Validation	             Blocks malformed messages (e.g., &admin=true)
Constant-Time Compare	       hmac.compare_digest() prevents timing attacks

## Vulnerabilities Addressed
#### Attack Type	      Vulnerable Code	         Secure Fix
Length Extension	      MD5(secret + message)	   HMAC nested hashing
Timing Attacks	         mac == expected_mac	      hmac.compare_digest()


## References

    RFC 2104 (HMAC)

    NIST SP 800-107

    OWASP Cryptographic Storage