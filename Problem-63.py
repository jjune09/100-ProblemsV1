def calculate_number_of_songs(hours: float, avg_song_length: float = 3.5) -> int:

    if hours < 0 or avg_song_length <= 0:
        raise ValueError("hours must be >=0 and avg_song_length > 0")
    total_minutes = hours * 60.0
    return int(total_minutes // avg_song_length)
print(calculate_number_of_songs(2, 4))

