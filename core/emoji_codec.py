import random
import hashlib

EMOJI_POOL = [
    "😀","😃","😄","😁","😆","😅","😂","🤣","😊","😇",
    "🙂","🙃","😉","😌","😍","🥰","😘","😗","😙","😚",
    "🤗","🤔","😐","😑","😶","🙄","😏","😣","😥","😮",
    "🤐","😯","😪","😫","🥱","😴","😛","😜","😝","🤤",
    "😒","😓","😔","😕","🫠","🤫","🫡","🫥","🧠","🔐"
]

BASE = len(EMOJI_POOL)


def _shuffled_emojis(key: str):
    seed = int(hashlib.sha256(key.encode()).hexdigest(), 16)
    rng = random.Random(seed)
    emojis = EMOJI_POOL.copy()
    rng.shuffle(emojis)
    return emojis


def encode_to_emoji(data: str, key: str) -> str:
    emojis = _shuffled_emojis(key)
    encoded = []

    for byte in data.encode():
        high = byte // BASE
        low = byte % BASE
        encoded.append(emojis[high])
        encoded.append(emojis[low])

    return "".join(encoded)


def decode_from_emoji(emoji_text: str, key: str) -> str:
    emojis = _shuffled_emojis(key)
    index_map = {e: i for i, e in enumerate(emojis)}

    if len(emoji_text) % 2 != 0:
        raise ValueError("Invalid emoji length")

    bytes_out = bytearray()

    for i in range(0, len(emoji_text), 2):
        high = index_map.get(emoji_text[i])
        low = index_map.get(emoji_text[i+1])

        if high is None or low is None:
            raise ValueError("Invalid emoji detected")

        bytes_out.append(high * BASE + low)

    return bytes_out.decode()
