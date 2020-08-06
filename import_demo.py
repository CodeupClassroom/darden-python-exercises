def a():
    return 1

def b():
    return 2

# If I import c in another file or notebook, I don't also have to import a and b
def c():
    return a() + b()


def acquire_data():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]

def prepare_data(data):
    return [str(x) for x in data if x < 8]
# If I import get_data in another notebook/file, I don't also have to import
# acquire_data or prepare_data
def get_data():
    data = acquire_data()
    data = prepare_data(data)
    return data