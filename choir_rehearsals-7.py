# === Stage 7: Связи между сущностями ===
# Project: ChoirRehearsals
from datetime import date


class ChoirRehearsal:
    def __init__(self, rehearsal_id, singer_id, scheduled_date):
        self.rehearsal_id = rehearsal_id
        self.singer_id = singer_id
        self.scheduled_date = scheduled_date


class ChoirRehearsalsRepository:
    def __init__(self, rehearsals):
        self._rehearsals = list(rehearsals)

    def get_singer_rehearsals(self, singer_id):
        return [
            rehearsal
            for rehearsal in self._rehearsals
            if rehearsal.singer_id == singer_id
        ]

    def validate_relationship(self, singer_id):
        rehearsals = self.get_singer_rehearsals(singer_id)
        if not rehearsals:
            return True
        for rehearsal in rehearsals:
            if not isinstance(rehearsal.scheduled_date, date):
                raise ValueError(
                    "Неверный тип даты репетиции для певца "
                    f"с id={singer_id}."
                )
        return True


def build_singer_profile(singer_id, repository):
    rehearsals = repository.get_singer_rehearsals(singer_id)
    repository.validate_relationship(singer_id)
    return {
        "singer_id": singer_id,
        "rehearsals_count": len(rehearsals),
        "rehearsals": [
            {
                "rehearsal_id": rehearsal.rehearsal_id,
                "scheduled_date": rehearsal.scheduled_date,
            }
            for rehearsal in rehearsals
        ],
    }


if __name__ == "__main__":
    sample_rehearsals = [
        ChoirRehearsal(1, 101, date(2024, 1, 15)),
        ChoirRehearsal(2, 101, date(2024, 1, 22)),
        ChoirRehearsal(3, 102, date(2024, 1, 29)),
    ]
    repository = ChoirRehearsalsRepository(sample_rehearsals)
    profile = build_singer_profile(101, repository)
    print(profile)
