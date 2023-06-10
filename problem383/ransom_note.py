def can_construct_ransom_note(ransom_note, magazine):
    if len(ransom_note) > len(magazine):
        return False

    unique_characters = set(ransom_note)

    for unique_char in unique_characters:
        ransom_note_count = ransom_note.count(unique_char)
        magazine_count = magazine.count(unique_char)

        if ransom_note_count > magazine_count:
            return False
    return True


print(can_construct_ransom_note("aa", "aab"))
