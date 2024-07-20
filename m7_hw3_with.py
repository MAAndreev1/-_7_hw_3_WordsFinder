class WordsFinder:
    file_names = []

    def __init__(self, *names):
        for i in names:
            self.file_names.append(i)

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, 'r', encoding='utf-8') as file:
                words = []
                for lens in file:
                    lens = lens.lower()
                    for i in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        lens = lens.replace(i, '')
                    words.extend(lens.split())
                all_words[file.name] = words
        return all_words

    def find(self, word):
        __find_words = {}
        for name, words in self.get_all_words().items():
            if word.lower() in self.get_all_words()[name]:
                __find_words[name] = self.get_all_words()[name].index(word.lower()) + 1
        return __find_words

    def count(self, word):
        __find_words = {}
        for name, words in self.get_all_words().items():
            if word.lower() in self.get_all_words()[name]:
                __find_words[name] = self.get_all_words()[name].count(word.lower())
        return __find_words


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
