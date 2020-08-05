import argparse
import math


"""
VUWG: Valid User Wordlist Generator

Generates username and password wordlists to brute-force test against a
specific user given a valid username and password. The intent of this script
is to provide an easy-to-use wordlist generator to test applications with
account lock mechanisms that reset themselves after a valid login attempt.

Disclaimer: for educational purposes only.
Do not use this script for illegal activities.
"""


def load_args():
    parser = argparse.ArgumentParser(prog='vuwg.py')
    parser.add_argument('username', type=str, help='Valid userame')
    parser.add_argument('password', type=str, help='Valid password')
    parser.add_argument('target_username', type=str, help='Username to bruteforce')
    parser.add_argument('password_list', type=str, help='Password list')
    parser.add_argument(
        '-m', '--max-attempts', type=int, default=2,
        help='Max number of attempts before account lock'
    )
    return parser.parse_args()


def load_passwords_from_file(passwords_filename):
    with open(passwords_filename) as passwords_file:
        lines = passwords_file.read().splitlines()
        passwords = [password for password in lines if password]
    return passwords


def create_username_list(target_user, valid_user, max_attempts, length):
    username_wordlist = []
    attempt = 1

    while len(username_wordlist) < length:
        if attempt > max_attempts:
            username_wordlist.append(valid_user)
            attempt = 1
        username_wordlist.append(target_user)
        attempt += 1

    write_wordlist_to_file('generated_username_list.txt', username_wordlist)
    return


def create_password_list(passwords, valid_password, max_attempts):
    password_wordlist = []
    attempt = 1

    for password in passwords:
        if attempt > max_attempts:
            password_wordlist.append(valid_password)
            attempt = 1
        password_wordlist.append(password)
        attempt += 1

    write_wordlist_to_file('generated_password_list.txt', password_wordlist)
    return


def write_wordlist_to_file(output_filename, wordlist):
    with open(output_filename, 'w') as output_file:
        for word in wordlist:
            output_file.write(word + '\n')
    print('[*] Generated file: {}'.format(output_filename))


if __name__ == '__main__':
    print('VUWG: Valid User Wordlist Generator\n')

    args = load_args()
    passwords = load_passwords_from_file(args.password_list)
    new_length = len(passwords) + math.floor(len(passwords)/args.max_attempts)

    print('Target username: {}'.format(args.target_username))
    print('Valid credentials to be used: {}:{}'.format(
        args.username, '*' * len(args.password)
    ))
    print('Max attempts before account lock: {}'.format(args.max_attempts))
    print('Initial wordlist length: {}'.format(len(passwords)))
    print('New wordlist length: {}\n'.format(new_length))

    create_password_list(passwords, args.password, args.max_attempts)
    create_username_list(
        args.target_username, args.username, args.max_attempts, new_length
    )

    print('\nDone!\n')

