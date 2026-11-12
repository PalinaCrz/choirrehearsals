# === Stage 1: Каркас модуля ===
# Project: ChoirRehearsals
from dataclasses import dataclass
from datetime import date


@dataclass
class Singer:
    name: str
    part: str
    phone: str
    join_date: date


def make_demo_singers() -> list[Singer]:
    return [
        Singer(name="Анна", part="сопрано", phone="+79001112233", join_date=date(2023, 1, 15)),
        Singer(name="Иван", part="тенор", phone="+79004445566", join_date=date(2022, 8, 3)),
        Singer(name="Мария", part="альто", phone="+79007778899", join_date=date(2024, 3, 21)),
        Singer(name="Пётр", part="бас", phone="+79001234567", join_date=date(2021, 11, 9)),
    ]


def main() -> None:
    singers = make_demo_singers()
    print("Демонстрационные певцы:")
    for singer in singers:
        print(f"  {singer.name} — {singer.part} (телефон: {singer.phone}, вступил(а): {singer.join_date})")


if __name__ == "__main__":
    main()
