# Создайте класс Playlist, представляющий плейлист с песнями. Переопределите метод __str__,
# чтобы он выводил список песен в читаемом виде, и метод __len__, чтобы можно было узнать
# количество песен в плейлисте.

# 2)Создайте класс, который будет представлять собой неизменяемый объект, и переопределите методы
# __hash__ и __eq__, чтобы можно было использовать его в множествах и как ключи в словарях.
class Playlist():
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)

    def __str__(self):
        if not self.songs:
            return "Плейлист пуст"
        else:
            playlist_str = "Плейлист:\n"
            for i, song in enumerate(self.songs, 1):
                playlist_str += f"{i}. {song}\n"
            return playlist_str

    def __len__(self):
        return len(self.songs)


if __name__ == "__main__":
    my_playlist = Playlist()
    my_playlist.add_song("I Don't Want To Miss A Thing")
    my_playlist.add_song("Living On My Own")
    my_playlist.add_song("I Want You, I Need You, I Love You")

    print(my_playlist)
    print(f"Количество песен в плейлисте: {len(my_playlist)}")
