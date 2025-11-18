hash_table = list([0 for i in range(8)])

def get_key(data):
    return hash(data)

def get_hash(key):
    return key % 8

def insert_data(data, value):
    key = get_key(data)
    hash_address = get_hash(key)
    hash_table[hash_address] = value

def get_hashData(data):
    key = get_key(data)
    hash_address = get_hash(key)
    return hash_table[hash_address]


insert_data('Dave', '01012341234')
insert_data('Minji', '01045684568')

print(hash_table)
print(get_hashData('Minji'))