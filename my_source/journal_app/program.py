def main():
    print_header()
    run_event_loop()


def print_header():
    print('----------------------')
    print('      JOURNAL APP')
    print('----------------------')


def run_event_loop():
    print('What do you want to do with your journal?')
    cmd = None
    journal_data = [] # list()

    while cmd != 'x':
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ')
        cmd = cmd.lower().strip()           

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x':
            print("Sorry, we don't understand '{}' command.".format(cmd))
    print('Done, goodbye.')


def list_entries(data):
    if data == []:
        print("It seems you don't have any entries in your journal, use 'a' to add an entry.")
    for each in data:
        print(each)


def add_entry(data):
    text = input('Type your entry, <enter> to exit: ')
    data.append(text)

main()
