import re

EMAIL_PATTERN = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")

def valid_email(email):
    return bool(EMAIL_PATTERN.match(str(email or "").strip()))

def valid_password(password):
    s = str(password or "")
    if len(s) < 8:
        return False
    has_alpha = any(ch.isalpha() for ch in s)
    has_digit = any(ch.isdigit() for ch in s)
    return has_alpha and has_digit

def bounded_text(value, max_len):
    text = str(value or "").strip()
    if len(text) > max_len:
        raise ValueError(f"Input terlalu panjang (maksimal {max_len} karakter)")
    return text