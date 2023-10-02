class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.value = None
        return cls._instance

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value


if __name__ == "__main__":
    s1 = Singleton()
    s1.set_value("Значение из s1")

    s2 = Singleton()
    print(f"Значение в s2: {s2.get_value()}")

    print(s1 is s2)
