import pytest
from core.emoji_codec import encode_to_emoji, decode_from_emoji


def test_emoji_encode_decode_success():
    data = "sample-data-123"
    key = "emoji-key"

    emoji = encode_to_emoji(data, key)
    decoded = decode_from_emoji(emoji, key)

    assert decoded == data


def test_emoji_decode_with_wrong_key_fails():
    data = "important"
    key1 = "key-one"
    key2 = "key-two"

    emoji = encode_to_emoji(data, key1)

    with pytest.raises(Exception):
        decode_from_emoji(emoji, key2)


def test_tampered_emoji_fails():
    data = "attack-test"
    key = "securekey"

    emoji = encode_to_emoji(data, key)

    # Tamper with emoji
    tampered = emoji[:-1] + "😀"

    with pytest.raises(Exception):
        decode_from_emoji(tampered, key)
