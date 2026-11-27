# === Stage 9: Текстовый поиск ===
# Project: ChoirRehearsals
import re


def highlight_matches(text, needles):
    """Подсвечивает совпадения игнорируя регистр и возвращает строку с метками.

    text - строка для поиска
    needles - список слов, которые нужно выделить
    """
    if not text:
        return ""

    pattern = re.compile(
        "|".join(re.escape(word) for word in needles),
        re.IGNORECASE,
    )
    return pattern.sub(r"\1\2\1", pattern.sub(r"\1\3\1", text))


def find_singers_by_text(singers, field, needle):
    """Находит певцов, у которых указанное поле содержит needle без учёта регистра.

    singers - список объектов певца
    field - имя текстового поля для поиска
    needle - искомое слово
    """
    if not needle:
        return []

    pattern = re.compile(re.escape(needle), re.IGNORECASE)
    return [
        singer
        for singer in singers
        if pattern.search(getattr(singer, field, ""))
    ]


def format_singer(singer):
    """Форматирует певца в строку для вывода."""
    name = getattr(singer, "name", "")
    role = getattr(singer, "role", "")
    return f"{name} [{role}]"


def search_singers(singers, field, needle):
    """Поиск по текстовому полю певца без учёта регистра с подсветкой.

    singers - список объектов певца
    field - имя текстового поля для поиска
    needle - искомое слово
    Возвращает строку вывода с подсветкой совпадений.
    """
    if not needle:
        return "Поиск не задан"

    matches = find_singers_by_text(singers, field, needle)
    if not matches:
        return f"Ничего не найдено по запросу: {needle}"

    highlighted = [
        highlight_matches(format_singer(singer), [needle])
        for singer in matches
    ]
    return "\n".join(highlighted)
