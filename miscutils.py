class MiscUtils:
    @staticmethod
    def Loop(num, min, max):
        difference = max - min
        num -= min
        num %= difference
        num += min
        return num


if __name__ == "__main__":
    for x in range(1000):
        print(MiscUtils.Loop(x, -100, 400))
