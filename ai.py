# -*- coding: utf-8 -*-
import unirest
import random
from time import sleep
import enum


API_URL = "http://localhost:8080/"
SESSION_ID = ""


class Direction(enum.Enum):
    up = 0
    right = 1
    down = 2
    left = 3


def start_request():
    return unirest.get(API_URL + "hi/start/json")


def move_request(direction):
    return unirest.get(API_URL + "hi/state/" + SESSION_ID + "/move/%d/json" % (direction.value,))


def simulate_move(grid, direction):
    new_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    
    if direction == Direction.up:
        for i in xrange(0, 4):
            column = map(lambda row: row[i], grid)
            merged = merge_list(column)
            for j in xrange(0, 4):
                new_grid[j][i] = merged[j]
    elif direction == Direction.down:
        for i in xrange(0, 4):
            column = map(lambda row: row[i], grid)
            merged = list(reversed(merge_list(reversed(column))))
            for j in xrange(0, 4):
                new_grid[j][i] = merged[j]
    elif direction == Direction.left:
        for i in xrange(0, 4):
            row = grid[i]
            merged = merge_list(row)
            for j in xrange(0, 4):
                new_grid[i][j] = merged[j]
    elif direction == Direction.right:
        for i in xrange(0, 4):
            row = grid[i]
            merged = list(reversed(merge_list(reversed(row))))
            for j in xrange(0, 4):
                new_grid[i][j] = merged[j]

    return new_grid


def merge_list(ls):
    ls = filter(lambda x: x != 0, ls)
    for i in xrange(0, len(ls) - 1):
        if ls[i] == 0:
            continue
        elif ls[i] == ls[i + 1]:
            ls[i] = ls[i] * 2
            ls[i + 1] = 0
    ls = filter(lambda x: x != 0, ls)
    return ls + ([0] * (4 - len(ls)))


def opt_direction(grid):
    pass


if __name__ == "__main__":
    result = start_request().body;
    SESSION_ID = result["session_id"]
    while not result["over"]:
        direction = opt_direction(result["grid"])
        result = move_request(direction).body
        sleep(0.1)
    if result["won"]:
        print "Won."
    else:
        print "Lost."
    print "score: %d" % (result["score"],)