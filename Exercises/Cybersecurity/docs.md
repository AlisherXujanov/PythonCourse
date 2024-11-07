# Cybersecurity with python

## Introduction
Cybersecurity is the practice of protecting systems, networks, and programs from digital attacks. These cyberattacks are usually aimed at accessing, changing, or destroying sensitive information; extorting money from users; or interrupting normal business processes.



## Common Attack Types

### 1. Password Attacks
- Brute Force
- Dictionary Attacks
- Rainbow Table Attacks

Python Protection Example:
```python
import bcrypt

def secure_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

password = 'password123'
hashed = secure_password(password)
print(hashed)
# By doing so, we can store the hashed password in the database and when retrieving the password, we can check if the password is correct by using the check_password function.
```

### 2. Network Attacks
Network attacks are focused on disrupting the network infrastructure and services. Some common network attacks include:

- DDoS Attacks - Which means Distributed Denial of Service attacks. This is when an attacker floods a network with an overwhelming amount of traffic to make the network unavailable
- Man-in-the-Middle Attacks - This is when an attacker intercepts communication between two parties
- Packet Sniffing   - This is when an attacker intercepts and logs network traffic


Python Protection Example:
```python
from scapy.all import sniff

def detect_packet(packet):
    if packet.haslayer('TCP'):
        # Monitor suspicious traffic patterns
        return packet.summary()

# Start packet monitoring
sniff(prn=detect_packet)
```

### 3. Social Engineering
- Phishing
- Spear Phishing
- Pretexting

Python Protection Example:
```python
import re

def detect_phishing_email(email_content):
    suspicious_patterns = [
        r'urgent.*action.*required',
        r'verify.*account.*details',
        r'banking.*security'
    ]
    for pattern in suspicious_patterns:
        if re.search(pattern, email_content.lower()):
            return True
    return False
```

### 4. Protection Strategies

1. **Input Validation**
    - Sanitize all user inputs
    - Use parameterized queries
    - Implement rate limiting

2. **Encryption**
    - Use strong cryptographic libraries
    - Implement SSL/TLS
    - Secure data at rest and in transit

3. **Monitoring**
    - Log suspicious activities
    - Implement intrusion detection
    - Regular security audits

4. **Access Control**
    - Implement proper authentication
    - Use role-based access control
    - Regular permission reviews