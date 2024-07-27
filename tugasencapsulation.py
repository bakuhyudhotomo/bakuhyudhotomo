class Person:
    def __init__(self, name, age):
        self.__name = name  # Properti private
        self.__age = age    # Properti private

    # Getter untuk name
    def get_name(self):
        return self.__name

    # Setter untuk name
    def set_name(self, name):
        self.__name = name

    # Getter untuk age
    def get_age(self):
        return self.__age

    # Setter untuk age
    def set_age(self, age):
        self.__age = age

# Membuat objek baru dari kelas Person
person = Person("John", 25)

# Mengakses variabel private menggunakan method getter
print("Name:", person.get_name())
print("Age:", person.get_age())

# Mengubah nilai variabel private menggunakan method setter
person.set_name("Jane")
person.set_age(30)

# Mengakses kembali variabel private yang telah diubah
print("Updated Name:", person.get_name())
print("Updated Age:", person.get_age())