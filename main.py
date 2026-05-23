import screen as t

t.screen()

while True:
    t.options()
    choice=input('➜ ')
    if not choice.strip():
        print('ERROR. TYPE SOMETHING.\n')
        continue
    try:
        choice=int(choice)
        if choice<1 or choice>3:
            print('ERROR. TYPE ONLY 1, 2 OR 3.\n')
            continue
    except ValueError:
        print('ERROR. ENTER A NUMBER\n')
        continue
    else:
        break

option={
    1: t.start,
    2: t.about,
    3: t.exitt
}

option[choice]()