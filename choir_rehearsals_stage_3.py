# === Stage 3: Хранилище в памяти ===
# Project: ChoirRehearsals
in_memory_choir.py

from collections import OrderedDict


class InMemoryChoirStore:
    def __init__(self):
        self._singers = OrderedDict()

    def add_singer(self, singer):
        self._singers[singer.identifier] = singer
        return singer

    def get_singer(self, identifier):
        return self._singers.get(identifier)

    def list_singers(self):
        return list(self._singers.values())


class Singer:
    def __init__(self, name, part, phone, join_date):
        self.name = name
        self.part = part
        self.phone = phone
        self.join_date = join_date
        self.identifier = None

    def __repr__(self):
        return f"Singer(name={self.name!r}, part={self.part!r}, phone={self.phone!r}, join_date={self.join_date!r}, identifier={self.identifier!r})"


def main():
    store = InMemoryChoirStore()

    a = Singer("Иван Иванов", "сопрано", "+79001112233", "2023-01-15")
    b = Singer("Мария Петрова", "тенор", "+79004445566", "2022-06-01")
    c = Singer("Сергей Смирнов", "бас", "+79007778899", "2024-03-20")

    store.add_singer(a)
    store.add_singer(b)
    store.add_singer(c)

    print("Список певцов:")
    for singer in store.list_singers():
        print(" ", singer)

    print("Получение по идентификатору '2':")
    print(" ", store.get_singer("2"))

    print("Получение несуществующего идентификатора '999':")
    print(" ", store.get_singer("999"))


if __name__ == "__main__":
    main()
