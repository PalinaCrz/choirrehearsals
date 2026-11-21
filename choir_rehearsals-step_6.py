# === Stage 6: Связанная сущность ===
# Project: ChoirRehearsals
from datetime import date


class Rehearsal:
    def __init__(self, rehearsal_id, date, location, description=""):
        self.rehearsal_id = rehearsal_id
        self.date = date
        self.location = location
        self.description = description
        self.attendees = []


def add_rehearsal(rehearsals, rehearsal_id, date, location, description="", singer_ids=None):
    if not isinstance(rehearsal_id, int):
        raise TypeError("rehearsal_id должен быть целым числом")
    if isinstance(date, str):
        date = date_to_date(date)
    rehearsal = Rehearsal(rehearsal_id, date, location, description)
    if singer_ids:
        for singer_id in singer_ids:
            for singer in rehearsees:
                if singer.singer_id == singer_id:
                    rehearsal.attendees.append(singer)
    rehearsees.append(rehearsal)
    return rehearsal


def date_to_date(date_str):
    return date.fromisoformat(date_str)
