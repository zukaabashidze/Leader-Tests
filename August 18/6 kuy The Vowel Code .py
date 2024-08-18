def encode(st):
        str_num = {'a': '1', 'e': '2', 'i': '3', 'o': '4', 'u': '5'}
        en_str = ''.join(str_num.get(char, char) for char in st)
        return en_str
        
    def decode(st):
        str_num = {'1':'a','2':'e','3':'i','4':'o','5':'u'}
        en_str = ''.join(str_num.get(char, char) for char in st)
        return en_str