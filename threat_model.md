# 🧠 Threat Model — EMOJISENTINEL

> Security analysis for a covert, emoji-based encrypted communication prototype.

---

## 🔎 Overview

**EMOJISENTINEL** is a **client-side security prototype** that converts plaintext messages into **encrypted emoji sequences**.  
Only a receiver with the **correct secret key** and **within the expiry window** can decode the message.

This document defines:
- What is protected
- Who is considered an attacker
- What attacks are mitigated
- What is explicitly out of scope

---

## 🎯 Assets We Protect

| Asset | Description |
|------|-------------|
| 📩 Message Content | Plaintext message entered by sender |
| 🔑 Secret Key | Pre-shared key between sender & receiver |
| 🕒 Message Validity | Expiry & integrity of the message |
| 😀 Emoji Cipher | Encrypted emoji representation |

---

## 🧑‍💻 Threat Actors (In Scope)

| Actor | Capability |
|-----|-----------|
| 👀 Curious Observer | Can see emojis only |
| 📡 Passive Interceptor | Can copy emojis from chat |
| 🧪 Semi-Technical Attacker | Can attempt tampering or guessing |
| 😈 Opportunistic Insider | Has emoji access, no key |

---

## 🚫 Out-of-Scope Threat Actors

The following are **explicitly NOT protected against**:

- Nation-state attackers
- Advanced Persistent Threats (APT)
- Endpoint malware / keyloggers
- Physical device compromise
- Memory inspection attacks

> EMOJISENTINEL is a **prototype**, not a hardened production system.

---

## ⚠️ Attack Surface

Potential attack vectors considered:

1. Emoji message interception
2. Emoji modification or injection
3. Brute-force key guessing
4. Replay of expired messages
5. Emoji frequency / pattern analysis

---

## 🔐 Security Controls & Mitigations

### 🔒 Confidentiality
**Threat:** Unauthorized message reading  
**Mitigation:**
- AES-GCM authenticated encryption
- PBKDF2 key derivation
- Emojis contain no plaintext data

---

### 🛡️ Integrity
**Threat:** Emoji tampering or manipulation  
**Mitigation:**
- AES-GCM authentication tag
- Any modification → decryption fails
- No partial or corrupted output is shown

---

### 🔑 Key Guessing / Brute Force
**Threat:** Attacker attempts to guess secret key  
**Mitigation:**
- PBKDF2 with high iteration count
- No online oracle or feedback
- Uniform failure behavior

---

### ⏳ Replay Attacks
**Threat:** Reuse of old emoji messages  
**Mitigation:**
- Encrypted expiry metadata
- Automatic invalidation after expiry

---

### 🧩 Pattern Analysis
**Threat:** Emoji frequency or pattern detection  
**Mitigation:**
- Key-dependent emoji shuffling
- Same message ≠ same emoji output with different keys

---

## 🕵️ Abuse & Misuse Considerations

This tool **can be misused** for covert communication.

Mitigations:
- Message length limits
- No anonymity guarantees
- Clear educational disclaimer
- No bulk or automated messaging

---

## ⚠️ Known Limitations (IMPORTANT)

EMOJISENTINEL does **NOT** protect against:

- Secret key leakage
- Compromised sender/receiver devices
- Screen recording or screenshots
- Social engineering attacks
- Advanced cryptanalysis

---

## 🧠 Security Philosophy

- Emojis are **transport**, not security
- Cryptography is the real defense
- Fail securely and explicitly
- No data storage or logging
- Avoid overclaiming guarantees

---

## ✅ Conclusion

EMOJISENTINEL is designed to:

- Resist casual and semi-technical interception
- Detect tampering reliably
- Enforce time-bound message access
- Demonstrate **secure system design principles**

This project intentionally prioritizes **clarity, correctness, and honesty** over false claims.

---

**Status:** Threat-modeled security prototype  
**License:** MIT  
**Author:** Shivam
