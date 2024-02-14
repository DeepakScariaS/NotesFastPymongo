def individual_serial(note) -> dict:
    return {
        "id": str(note["_id"]),
        "title": note["title"],
        "description": note["description"],
    }


def list_serial(notes) -> list:
    return [individual_serial(note) for note in notes]
