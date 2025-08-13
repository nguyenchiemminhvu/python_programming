from collections import Counter, defaultdict, deque, namedtuple, OrderedDict, ChainMap, UserDict, UserList, UserString

# Counter example
def counter_example():
    words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    word_count = Counter(words)
    print("Word Count:", word_count)

counter_example()

# defaultdict example
def defaultdict_example():
    dd = defaultdict(int)
    dd['apple'] += 1
    dd['banana'] += 2
    print("DefaultDict:", dict(dd))

defaultdict_example()

# deque example
def deque_example():
    d = deque(['apple', 'banana', 'orange'])
    d.append('grape')
    d.appendleft('kiwi')
    print("Deque:", d)

deque_example()

# namedtuple example
def namedtuple_example():
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(10, 20)
    print("NamedTuple:", p)
    print("Point x:", p.x, "y:", p.y)

namedtuple_example()

# OrderedDict example
def ordered_dict_example():
    od = OrderedDict()
    od['apple'] = 1
    od['banana'] = 2
    od['orange'] = 3
    od['a'] = 0
    od['apple'] = 4
    print("OrderedDict:", od)

ordered_dict_example()

# ChainMap example
def chainmap_example():
    defaults = {'theme': 'dark', 'font_size': 12}
    user_settings = {'font_size': 14, 'language': 'en'}
    settings = ChainMap(user_settings, defaults)
    print(settings['font_size'])  # Output: 14 (from user_settings, as it's first)
    print(settings['theme'])     # Output: dark (from defaults)
    settings['language'] = 'fr'  # Adds/updates in user_settings
    print(user_settings)         # Output: {'font_size': 14, 'language': 'fr'}

chainmap_example()

# UserDict example
def userdict_example():
    class MyDict(UserDict):
        def __setitem__(self, key, value):
            super().__setitem__(str(key).upper(), value)
        def __missing__(self, key):
            return "Not Found"

    my_dict = MyDict({'apple': 1, 'banana': 2})
    print("UserDict:", my_dict['apple'.upper()])  # Output: 1
    print("UserDict:", my_dict['orange'])  # Output: Not Found

userdict_example()

# UserList example
def userlist_example():
    class MyList(UserList):
        def append(self, item):
            super().append(item * 2)  # Double the item before appending

    my_list = MyList([1, 2, 3])
    my_list.append(4)
    print("UserList:", my_list)  # Output: [1, 2, 3, 8]

userlist_example()

# UserString example
def userstring_example():
    class MyString(UserString):
        def __add__(self, other):
            return MyString(self.data + " " + other.data)

    my_str1 = MyString("Hello")
    my_str2 = MyString("World")
    combined_str = my_str1 + my_str2
    print("UserString:", combined_str)  # Output: Hello World

userstring_example()