# I am a student.
# student. a am I

def revecovt(str):
    if len(str) <= 1:
        return str
    new_str = str.split(' ')
    return ' '.join(new_str[::-1])

print(revecovt('I am a student.'))

