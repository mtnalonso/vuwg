# VUWG: Valid User Wordlist Generator

The intent behind this tool is to provide an easy-to-use wordlist generator that will help test applications with IP lock mechanisms that reset themselves after a valid login attempt.

By providing a password wordlist, a target username and valid credentials, the tool generates a username and a password wordlists. In both wordlist the valid user's credentials are inserted after **X** number of words, being **X** the max number of invalid attempts an attacker might check before getting the attacker's IP locked. The default max number of attempts is set to two but it can be also modified by using the parameter `-m` or `--max-attempts`.


#### Disclaimer
For educational purposes only. Do not use this script for illegal activities.
