class Human:
    name = "Büşra"
    # built-in # constructor # initialize
    def __init__(self,name):
        self.name = name
        print("Bir human instance'ı üretildi.")
    def __str__(self):
        return f"STR fonksiyonundan dönen değer: {self.name}"
    def talk(self, sentence):
        print(f"{self.name}: {sentence}")  # self kullanılmazsa sadece kendi bloğundaki name ifadesini görür. self class'da name görmesini sağlar.
    def walk(self):
        print(f"{self.name} is walking..")
