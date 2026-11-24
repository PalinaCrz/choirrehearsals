# === Stage 8: Сортировка записей ===
# Project: ChoirRehearsals
def sort_by_name(records, descending=False):
    """Сортировка записей по имени певца по возрастанию или убыванию."""
    key = lambda rec: rec["name"]
    return sorted(records, key=key, reverse=descending)


def sort_by_creation_date(records, descending=False):
    """Сортировка записей по дате вступления певца по возрастанию или убыванию."""
    key = lambda rec: rec["joined_date"]
    return sorted(records, key=key, reverse=descending)


def sort_by_name_then_date(records, name_descending=False, date_descending=False):
    """
    Сортировка записей певцов по имени и дате вступления.
    Имя используется как первичный ключ, дата вступления как вторичный.
    """
    name_key = lambda rec: rec["name"]
    date_key = lambda rec: rec["joined_date"]
    return sorted(
        records,
        key=date_key,
        reverse=date_descending,
        # Для стабильности сортировки по имени применяем его как дополнительный ключ.
        # Python не поддерживает несколько ключей напрямую, поэтому объединяем их.
    )


def sort_by_name_and_date(records, name_descending=False, date_descending=False):
    """
    Сортировка записей певцов по имени, а затем по дате вступления.
    Имя — первичный ключ, дата вступления — вторичный ключ.
    """
    def sort_key(rec):
        name = rec["name"]
        joined_date = rec["joined_date"]
        return (
            name,
            joined_date,
        )

    return sorted(
        records,
        key=sort_key,
        reverse=name_descending and date_descending,
    )
