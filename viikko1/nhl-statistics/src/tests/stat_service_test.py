import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_wrong_name(self):
        player = self.stats.search("Selänne")
        self.assertEqual(player, None)

    def test_player_found(self):
        player = self.stats.search("Semenko")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Semenko")
        self.assertEqual(player.team, "EDM")
        self.assertEqual(player.goals, 4)
        self.assertEqual(player.assists, 12)

    def test_team_found(self):
        team = self.stats.team("EDM")
        self.assertEqual(len(team), 3)
        self.assertEqual(team[0].name, "Semenko")
        self.assertEqual(team[1].name, "Kurri")
        self.assertEqual(team[2].name, "Gretzky")

    def test_top_correct(self):
        top = self.stats.top(3)
        self.assertEqual(
            [player.name for player in top],
            ["Gretzky", "Lemieux", "Yzerman"]
        )

    def test_correct_order(self):
        top1 = self.stats.top(3,SortBy.GOALS)
        top2 = self.stats.top(3,SortBy.ASSISTS)

        self.assertEqual(
                    [player.name for player in top1],
                    ["Lemieux", "Yzerman", "Kurri"]
                )
        self.assertEqual(
                    [player.name for player in top2],
                    ["Gretzky", "Yzerman", "Lemieux"]
                )