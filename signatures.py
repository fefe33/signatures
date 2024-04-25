#file signature identifier program
#this is the only code for this project written by @fefe33
#supposed to be very simple
import json, sys, os

help_text = '''
        this program only takes 1 arg max.
        use it like this:

            python3 signatures.py <extension type>
            use keyword 'all' to print all mime types and signatures

        i didnt make the list
        original JSON file signature list available at: https://gist.github.com/Qti3e/6341245314bf3513abb080677cd1c93b#file-extensions-json
    '''



try:
    q = sys.argv[1]
except:
    print('no search term specified')
    exit(0)

if len(sys.argv) > 2 or len(sys.argv) < 2 or sys.argv[1] == '-h' or sys.argv[1] == '--help':
    print(help_text)
    exit(0)

with open(os.path.dirname(os.path.realpath(__file__)) + '/signatures.json', 'r') as file:
    x = ''''''
    for i in file:
        x+=i
#create the object
obj = json.loads(x)

#if the user wants to just read all of them
if sys.argv[1].lower() == ('all'):
    for i in obj:
        print('{}\nsigns:'.format(obj[i]["mime"]))
        for j in obj[i]['signs']:
            s = j.split(',')
            print(f'-- -- -- --\n\toffset: {s[0]}\n\tsign: {s[1]}\n-- -- -- --\n')
    exit(0)

elif sys.argv[1] in list(obj.keys()):
    for i in obj:
        if i == q:
            x = obj[i]
        else:
            continue

    print('-- -- -- --\n')
    print('mime:\n\t{}\n\nsignatures:'.format(x["mime"]))
    for i in x['signs']:
        offset_and_sig = i.split(',')
        print(f'\toffset: {offset_and_sig[0]}\n\tsign: {offset_and_sig[1]}\n\n\t-- -- -- --')
else:
    print(f'filetype {sys.argv[1]} not found')
