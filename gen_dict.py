import sys
import requests

def print_progress_bar(iteration, total, prefix='', length=50, fill='█', empty='░', word=''):
    percent = ("{:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + empty * (length - filled_length)
    attachment = ''
    if not word == '':
        attachment = f'\t[{word}]'
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% Complete{attachment}')
    sys.stdout.flush()

def main():
    words = open("words", 'r')
    file = open("dict", 'a')
    current = open("curr", 'r')
    line = words.readline()
    word = line[:-1]
    t = 235976
    i = 0
    word_index_obj = current.readline()[:-1]
    word_index = word_index_obj[:-1]
    current.close()
    
    while word.lower() <= word_index.lower():
        line = words.readline() 
        word = line[:-1]
        i = i + 1
    current = open("curr", 'w')
    while line: 
        #deal with current
        current.write(word) #[:-1] removes newline character
        current.truncate()
        current.seek(0)
        if word[0].islower() and len(word) > 3:
            url=f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
            response = requests.request("GET", url)
            if response.status_code == 200:
                #write to dict
                file.write(line)
        i = i + 1
        print_progress_bar(i, t, prefix="Progress:", word=word)
        line = words.readline() 
        word = line[:-1]

if __name__ == "__main__":
    main()