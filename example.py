#!/usr/bin/env python3
from pypop import compose, Player


def main():
    song = compose()
    player = Player()
    player.play(song)


if __name__ == '__main__':
    main()
