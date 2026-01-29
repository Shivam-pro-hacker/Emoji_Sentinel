import time
import streamlit as st

from ui.styles import load_styles
from core.crypto import encrypt_message, decrypt_message
from core.emoji_codec import encode_to_emoji, decode_from_emoji

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="EmojiSentinel",
    page_icon="🛡️",
    layout="centered"
)

load_styles()

# -------------------- HEADER --------------------
st.markdown("<h1>🛡️ EMOJISENTINEL</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='color:#9CA3AF;'>Covert, time-bound emoji encryption</p>",
    unsafe_allow_html=True
)

st.divider()

# -------------------- MODE SELECTOR --------------------
mode = st.radio(
    "Select Mode",
    ["Create Emoji Message", "Decode Emoji Message"],
    horizontal=True
)

# ====================================================
# 🧑‍💻 CREATE MODE (SENDER)
# ====================================================
if mode == "Create Emoji Message":

    st.subheader("🔐 Create Emoji Message")

    message = st.text_area(
        "Enter Message",
        placeholder="Meet me at 10 PM"
    )

    secret_key = st.text_input(
        "Secret Key",
        type="password",
        placeholder="Shared secret"
    )

    expiry_minutes = st.selectbox(
        "Message Expiry (minutes)",
        [1, 5, 10, 30, 60]
    )

    if st.button("Generate Emoji Cipher"):

        if not message.strip() or not secret_key.strip():
            st.error("Message and secret key are required.")
        else:
            try:
                encrypted_payload = encrypt_message(
                    message=message,
                    password=secret_key,
                    expiry_minutes=expiry_minutes
                )

                emoji_cipher = encode_to_emoji(
                    encrypted_payload,
                    secret_key
                )

                st.success("Emoji message generated successfully.")

                st.text_area(
                    "Encrypted Emoji Message",
                    value=emoji_cipher,
                    height=120
                )

                st.caption("⚠️ Share ONLY the emojis with the receiver.")

            except Exception as e:
                st.error("Failed to generate emoji message.")

# ====================================================
# 🧑‍💻 DECODE MODE (RECEIVER)
# ====================================================
else:

    st.subheader("🔓 Decode Emoji Message")

    emoji_input = st.text_area(
        "Paste Emoji Message",
        placeholder="😀😈🔒🔥🧠"
    )

    secret_key = st.text_input(
        "Secret Key",
        type="password",
        placeholder="Same key used by sender"
    )

    if st.button("Decode Message"):

        if not emoji_input.strip() or not secret_key.strip():
            st.error("Emoji message and secret key are required.")
        else:
            try:
                encrypted_payload = decode_from_emoji(
                    emoji_text=emoji_input,
                    key=secret_key
                )

                data = decrypt_message(
                    encoded_data=encrypted_payload,
                    password=secret_key
                )

                message = data.get("message")
                expiry_seconds = data.get("expiry")

                if message is None or expiry_seconds is None:
                    st.error("Invalid or corrupted message.")
                else:
                    st.success("Message decoded successfully.")

                    st.text_area(
                        "Decrypted Message",
                        value=message,
                        height=120
                    )

            except Exception:
                st.error(
                    "Access denied: wrong key, modified emojis, or expired message."
                )

# -------------------- FOOTER --------------------
st.markdown(
    "<hr style='border:0.5px solid #1f2937'>"
    "<p style='text-align:center; color:#9CA3AF; font-size:12px;'>"
    "MIT License © Shivam"
    "</p>",
    unsafe_allow_html=True
)
