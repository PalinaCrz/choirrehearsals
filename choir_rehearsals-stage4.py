# === Stage 4: Редактирование записей ===
# Project: ChoirRehearsals
from datetime import date

ALLOWED_FIELDS = ("name", "role", "phone", "join_date")


def edit_singer(singer, field_name, new_value, singers):
    singers = dict(singers)
    singer = singers.get(singer["id"])
    if singer is None:
        raise KeyError(f"Певец {singer} не найден")
    if field_name not in ALLOWED_FIELDS:
        raise ValueError(f"Поле '{field_name}' недоступно для редактирования")
    singer[field_name] = new_value
    singers[singer["id"]] = singer
    return singers
