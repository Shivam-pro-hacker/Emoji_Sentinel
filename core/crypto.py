import os
import json
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100_000,
    )
    return kdf.derive(password.encode())


def encrypt_message(message: str, password: str, expiry_minutes: int) -> str:
    salt = os.urandom(16)
    key = derive_key(password, salt)
    aesgcm = AESGCM(key)

    nonce = os.urandom(12)

    payload = {
        "message": message,
        "expiry": expiry_minutes * 60,  # seconds
    }

    plaintext = json.dumps(payload).encode()
    ciphertext = aesgcm.encrypt(nonce, plaintext, None)

    packed = {
        "salt": base64.b64encode(salt).decode(),
        "nonce": base64.b64encode(nonce).decode(),
        "ciphertext": base64.b64encode(ciphertext).decode(),
    }

    return base64.b64encode(json.dumps(packed).encode()).decode()


def decrypt_message(encoded_data: str, password: str) -> dict:
    decoded = json.loads(base64.b64decode(encoded_data).decode())

    salt = base64.b64decode(decoded["salt"])
    nonce = base64.b64decode(decoded["nonce"])
    ciphertext = base64.b64decode(decoded["ciphertext"])

    key = derive_key(password, salt)
    aesgcm = AESGCM(key)

    plaintext = aesgcm.decrypt(nonce, ciphertext, None)
    return json.loads(plaintext.decode())
