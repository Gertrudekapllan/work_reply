# Создайте класс Playlist, представляющий плейлист с песнями. Переопределите метод __str__,
# чтобы он выводил список песен в читаемом виде, и метод __len__, чтобы можно было узнать
# количество песен в плейлисте.

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


# 2)Создайте класс, который будет представлять собой неизменяемый объект, и переопределите методы
# __hash__ и __eq__, чтобы можно было использовать его в множествах и как ключи в словарях.

class ImmutableObject:
    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        if isinstance(other, ImmutableObject):
            return self.value == other.value
        return False


# Пример использования
if __name__ == "__main__":
    obj1 = ImmutableObject(42)
    obj2 = ImmutableObject(42)
    obj3 = ImmutableObject(100)

    # Проверка на равенство и хеширование
    print(obj1 == obj2)  # True
    print(obj1 == obj3)  # False

    # Использование в множестве
    my_set = set()
    my_set.add(obj1)
    my_set.add(obj2)
    my_set.add(obj3)

print(my_set)  # Множество содержит только obj1 и obj3

# Использование в словаре
my_dict = {obj1: "значение 1", obj3: "значение 2"}

print(my_dict)  # Словарь содержит две пары ключ-значение
