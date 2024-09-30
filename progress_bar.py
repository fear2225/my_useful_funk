__author__ = "https://github.com/fear2225"

# Libs
import shutil

# Modules


# ========================================
class Bar:
    """
    progress bar usage:
    bar = Bar(3)
    next(bar)
    del bar
    """
    fill = '#'
    empty = '_'

    colour_default = '\033[0m'
    color_complete = '\033[34m'
    color_normal = '\033[33m'
    color_error = '\033[31m'

    count: int = 0
    limit: int

    def __init__(self, limit: int):
        self.limit: int = limit
        print('\n', end='')

    def _paint(self, text, color) -> str:
        """ add escape color codes """
        return color + text + self.colour_default

    @staticmethod
    def _line_length() -> int:
        """ console length [symbols] """
        return shutil.get_terminal_size().columns

    def __str__(self) -> str:
        """ draw progress bar """
        right_part = ' [%s/%s]' % (self.count, self.limit)
        left_part_len = self._line_length() - len(right_part)
        left_part = self.fill * (left_part_len * self.count//self.limit)
        return left_part.ljust(left_part_len, self.empty) + right_part

    def __next__(self) -> None:
        """ next step """
        if self.count <= self.limit:
            self.count += 1
        print('\r' + self._paint(str(self), self.color_normal), end='')

    def __del__(self):
        """ log result """
        if self.limit > self.count:
            print('\r' + self._paint(str(self), self.color_error), end='')
        else:
            print('\r' + self._paint(str(self), self.color_complete), end='')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__del__()


# ========================================
def main():
    import time

    bar = Bar(4)
    for _ in range(4):
        next(bar)
        time.sleep(.5)
    time.sleep(1)
    del bar

    # ====OR====
    with Bar(5) as bar:
        for _ in range(4):
            time.sleep(.5)
            next(bar)


# ========================================
if __name__ == '__main__':
    main()
    pass
