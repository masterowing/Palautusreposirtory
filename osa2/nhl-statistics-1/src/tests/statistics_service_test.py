import unittest
from statistics_service import StatisticsService
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_existing_name_returns_player(self):
        player = self.stats.search("Yzerman")

        self.assertEqual(player.name, "Yzerman")

    def test_search_unknown_name_returns_none(self):
        player = self.stats.search("Wahlgren")

        self.assertIsNone(player)

    def test_team_edm_returns_edm_players(self):
        players = self.stats.team("EDM")
        names = [player.name for player in players]

        self.assertEqual(names, ["Semenko", "Kurri", "Gretzky"])

    def test_top_two_returns_best_first(self):
        players = self.stats.top(2)

        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Lemieux")