import time
def intro():
    print('=====================================')
    print('\tTHE LOST ADVENTURE')
    print('=====================================\n')


    print('\n-------------------------------------')
    print('\tINTRODUCTION')
    print('-------------------------------------')
    print("You wake up in a dark, unfamiliar place...")
    time.sleep(2)
    print("The air is cold. The silence is unsettling.")
    time.sleep(2)
    player_name = input("A voice whispers: 'What is your name? ")
    time.sleep(2)
    print(f"{player_name}...")
    time.sleep(1)
    print("The voice grows silent.")
    time.sleep(2)
    print('...')
    time.sleep(1)
    print('.....')
    time.sleep(1)
    print(f"{player_name}, your journey begins now.")
    return player_name

def first_choice(player_name):
    print('\n-------------------------------------')
    print('You slowly stand up.')
    time.sleep(2)
    print('Your heart begins to race.')
    time.sleep(2)
    print('In front of you are two options:\n')
    time.sleep(1)

    print('1. Explore the darkness')
    print('2. Look for a way out\n')

    choice = input('What do you do? (1 or 2): ').strip()

    if choice == '1':
        print(f"\n{player_name} steps into the darkness...")
        time.sleep(2)
        print("The light behind you fades.")
        time.sleep(2)
        print("You hear breathing — but it isn't yours.")
        time.sleep(2)
        print("Your hands start to shake.")
    elif choice == '2':
        print(f"\n{player_name} searches desperately for a way out...")
        time.sleep(2)
        print("Your footsteps echo too loudly.")
        time.sleep(2)
        print("Something scrapes against the wall behind you.")
        time.sleep(2)
        print("You don't dare turn around.")
    else:
        print("\nFear freezes you in place.")
        time.sleep(2)


if __name__ == '__main__':
    player_name = intro()
    first_choice(player_name)