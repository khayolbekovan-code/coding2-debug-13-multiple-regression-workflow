"""Display your Homework 2 mark: uv run python show_grade.py."""

from hashlib import sha256

SALT = "609b9415248eb5f690be27ad48f24cc0"
GRADE_HASH = "311b7fbcd1e6e4af10fc1e98a16f7fe6402a4a4514e98a68717e7b3a2a630da5"

# Match the stored hash against each possible whole-number mark.
for mark in range(101):
    candidate = sha256(f"{SALT}:{mark}".encode("utf-8")).hexdigest()
    if candidate == GRADE_HASH:
        print(f"Homework 2: {mark}/100")
        break
else:
    raise RuntimeError("The mark could not be verified. Please contact the instructor.")
