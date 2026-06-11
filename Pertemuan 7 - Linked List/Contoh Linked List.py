class SongNode:
    def __init__(self, title):
        self.title = title
        self.next = None

class Playlist:
    def __init__(self):
        self.head = None

    def add_song(self, title):
        new_song = SongNode(title)
        if not self.head:
            self.head = new_song
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_song
        print(f"Lagu '{title}' telah ditambahkan ke playlist.")

    def show_playlist(self):
        current = self.head
        if not current:
            print("Playlist kosong.")
            return
        print("Playlist:")
        while current:
                print(f"- {current.title}")
                current = current.next

    def play_all(self):
        current = self.head
        if not current:
            print("Tidak ada lagu untuk diputar.")
            return
        print("Memutar semua lagu dalam playlist:")
        while current:
            print(f"Memutar: {current.title}")
            current = current.next
        
playlist = Playlist()

playlist.add_song("Lagu 1 - Problematic")
playlist.add_song("Lagu 2 - Renegades")     
playlist.add_song("Lagu 3 - Toxic")
playlist.add_song("Lagu 4 - Contigo")
playlist.add_song("Lagu 5 - Bad Things")

print()
playlist.show_playlist()

print()
playlist.play_all()