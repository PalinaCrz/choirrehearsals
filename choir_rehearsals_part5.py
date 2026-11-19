# === Stage 5: Удаление и восстановление ===
# Project: ChoirRehearsals
import datetime

# Мягкое удаление: флаг вместо удаления записи
class SoftDeletedPевец:
    def __init__(self, record):
        self.record = record
        self.deleted = False
        self.deleted_at = None

    def restore(self):
        if not self.deleted:
            return False
        self.deleted = False
        self.deleted_at = None
        self.record.deleted = False
        return True

    def delete(self):
        if self.deleted:
            return False
        self.deleted = True
        self.deleted_at = datetime.datetime.now()
        self.record.deleted = True
        return True


class ChoirRehearsalsStore:
    def __init__(self):
        self.singers = {}

    def add_singer(self, name, part, phone, joined_on):
        singer = {
            "name": name,
            "part": part,
            "phone": phone,
            "joined_on": joined_on,
            "deleted": False,
        }
        self.singers[name] = singer
        return singer

    def get_singer(self, name):
        singer = self.singers.get(name)
        if singer is None:
            return None
        if singer.get("deleted"):
            return None
        return singer

    def remove_singer(self, name):
        singer = self.singers.get(name)
        if singer is None:
            return False
        soft = SoftDeletedPевец(singer)
        soft.delete()
        return True

    def restore_singer(self, name):
        singer = self.singers.get(name)
        if singer is None:
            return False
        soft = SoftDeletedPевец(singer)
        soft.restore()
        return True

    def list_singers(self):
        return [
            singer for singer in self.singers.values()
            if not singer.get("deleted")
        ]


if __name__ == "__main__":
    store = ChoirRehearsalsStore()
    store.add_singer("Иван Иванов", "Сопрано", "+79001112233", "2024-01-05")
    store.add_singer("Мария Смирнова", "Альт", "+79004445566", "2024-02-10")
    print("Партии:", [s["part"] for s in store.list_singers()])
    store.remove_singer("Иван Иванов")
    print("После удаления:", [s["part"] for s in store.list_singers()])
    print("Удалён:", store.get_singer("Иван Иванов") is None)
    store.restore_singer("Иван Иванов")
    print("После восстановления:", [s["part"] for s in store.list_singers()])
    print("Восстановлен:", store.get_singer("Иван Иванов") is not None)
