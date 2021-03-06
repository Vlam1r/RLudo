import random


class RandomPlayer(object):

    def __init__(self, seed=None):
        if seed:
            self.random = random.Random(seed)
        else:
            self.random = random.Random()
        return

    def play(self, _, num_actions):
        return self.random.randrange(0, num_actions)

    def recalculate_step(self, *args):
        return

    def recalculate_end(self):
        return

    def reset(self):
        return