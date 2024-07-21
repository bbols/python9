#test
#import unittest


#class TestLoto(unittest.TestCase):
from loto_my import game_loto,user_game
class TestLoto:
    def test_user(self):
        user=user_game()
        assert user.user_name=='Anon'

    def test_game(self):
        game = game_loto()
        assert game.user == []
        user_b = user_game()
        user_a = user_game()
        game.user_add(user_a)
        game.user_add(user_b)
        assert len(game.user) == 2
        game.users_clear()
        assert len(game.user) == 0

#123