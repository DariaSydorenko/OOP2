class FileProcessing:
    def __init__(self, file):
        self.file = file

    def count_symbols(self):
        try:
            f = open(self.file, 'r')
            count = 0
            while True:
                char = f.read(1)
                if not char:
                    break
                if char.isspace():
                    continue
                count += 1
            return count
        except FileNotFoundError:
            print('File is not exists!')

    def count_words(self):
        try:
            f = open(self.file, 'r')
            count = 0
            ending = False
            while True:
                char = f.read(1)
                if not char:
                    break
                if char not in [',', '.', ':', ';', '!', '?'] and not char.isspace() and not ending:
                    ending = True
                if (char in [',', '.', ':', ';', '!', '?'] or char.isspace()) and ending:
                    count += 1
                    ending = False
            return count
        except FileNotFoundError:
            print('File is not exists!')

    def count_sentences(self):
        try:
            f = open(self.file, 'r')
            count = 0
            ending = False
            while True:
                char = f.read(1)
                if not char:
                    break
                if char not in ['.', '!', '?'] and not ending:
                    ending = True
                if char in ['.', '!', '?'] and ending:
                    count += 1
                    ending = False
            return count
        except FileNotFoundError:
            print('File is not exists!')


result = FileProcessing('text2-4.txt')
print(f'Symbols: {result.count_symbols()}\n'
      f'Words: {result.count_words()}\n'
      f'Sentences: {result.count_sentences()}')
