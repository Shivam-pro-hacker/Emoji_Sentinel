import pytest
from core.crypto import encrypt_message, decrypt_message


def test_encrypt_decrypt_success():
    message = "Secret message"
    key = "strongpassword"
    expiry = 5

    encrypted = encrypt_message(message, key, expiry)
    decrypted = decrypt_message(encrypted, key)

    assert decrypted["message"] == message
    assert decrypted["expiry"] == expiry * 60


def test_decrypt_with_wrong_key_fails():
    message = "Top secret"
    correct_key = "correctkey"
    wrong_key = "wrongkey"

    encrypted = encrypt_message(message, correct_key, 5)

    with pytest.raises(Exception):
        decrypt_message(encrypted, wrong_key)
