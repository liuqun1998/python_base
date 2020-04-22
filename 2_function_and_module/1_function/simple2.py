#函数的形参
def print_verse(verse_name, is_show_title):
    if is_show_title == 1:
        print(verse_name)
    if verse_name == '悯农':
        print('锄禾日当午')
        print('汗滴禾下土')
    if verse_name == '静夜思':
        print('床前明月光')
        print('疑是地上霜')

print_verse('静夜思',1)