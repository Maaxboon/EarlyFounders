#!/usr/bin/env python

secret = 1337
attempt = -1

while attempt != secret:
    attempt = int(input("Guess: "))
    print("You did it!")
