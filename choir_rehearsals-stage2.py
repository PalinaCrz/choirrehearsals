# === Stage 2: Проверка полей ===
# Project: ChoirRehearsals
import datetime

VALID_VOICES = {
    "сопрано",
    "меццо-сопрано",
    "альто",
    "тенор",
    "баритон",
    "бас",
}

FIRST_NAMES = {
    "анна", "мария", "елена", "ольга", "наталья", "ирина", "таатьяна", "светлана",
    "алексей", "дмитрий", "сергей", "иван", "пётр", "андрей", "виктор", "борис",
}

def normalize_name(text):
    cleaned = text.strip()
    for candidate in FIRST_NAMES:
        if cleaned.lower() == candidate:
            return candidate.capitalize()
    return cleaned


def normalize_voice(text):
    cleaned = text.strip()
    for candidate in VALID_VOICES:
        if cleaned.lower() == candidate:
            return candidate.capitalize()
    return cleaned


def normalize_phone(text):
    cleaned = text.strip().replace("-", "").replace(" ", "").replace("+7", "7").replace("8", "7")
    if not cleaned.isdigit():
        raise ValueError("Телефон должен содержать только цифры.")
    if len(cleaned) < 10 or len(cleaned) > 11:
        raise ValueError("Телефон должен содержать от 10 до 11 цифр.")
    return cleaned


def normalize_date(text):
    cleaned = text.strip()
    for format in ("%d.%m.%Y", "%d.%m.%y", "%Y-%m-%d"):
        try:
            parsed = datetime.datetime.strptime(cleaned, format)
            return parsed.strftime("%Y-%m-%d")
        except ValueError:
            continue
    raise ValueError("Дата должна быть в формате ДД.ММ.ГГГГ.")


class SingerError(Exception):
    pass


def validate_singer(raw):
    name = normalize_name(raw["name"])
    if not name:
        raise SingerError("Имя не может быть пустым.")

    voice = normalize_voice(raw["voice"])
    if voice not in VALID_VOICES:
        raise SingerError(
            "Неизвестная партия. Допустимые партии: "
            + ", ".join(sorted(VALID_VOICES))
        )

    phone = normalize_phone(raw["phone"])

    date = normalize_date(raw["join_date"])

    return {
        "name": name,
        "voice": voice,
        "phone": phone,
        "join_date": date,
    }
