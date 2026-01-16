def validate_entry(entry):
    if not entry["name"] or entry["name"].isspace():
        return False, "Name is required"
    if not entry["activity"] or entry["activity"].isspace():
        return False, "Activity is required"
    if entry["age"] < 5 or entry["age"] > 100:
        return False, "Age must be between 5 and 100"
    if entry["hours"] <= 0 or entry["hours"] > 24:
        return False, "Hours must be between 0 and 24"
    return True, ""
    