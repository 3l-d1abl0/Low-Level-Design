class Notes:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.entries.append(f"{self.count}: {text}")
        self.count += 1

    def __str__(self):
        return "\n".join(self.entries)

    ''' breaks SRP
    def save(self, filename):
        file = open(filename, "w")
        file.write(str(self))
        file.close()
    '''


class FileSystem:
    @staticmethod
    def save_to_file(notes, filename):
        file = open(filename, "w")
        file.write(str(notes))
        file.close()

if __name__ == "__main__":

    take_notes = Notes()
    take_notes.add_entry("Learning Design Principles")
    take_notes.add_entry("This is Sinple responsibility Principle")
    print(f"My Notes:\n{take_notes}\n")

    file = "My-Notes.txt"
    #Breaks SRP
    #take_notes.save(file)
    
    #Seperating the responsibility of interacting with the file System
    p = FileSystem()
    p.save_to_file(take_notes, file)

    # verify!
    with open(file) as f:
        print(f.read())