from enum import Enum

class SortBy:
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

class StatisticsService:
    def __init__(self, reader):
        self.reader = reader
        self._players = self.reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, order=SortBy.POINTS):
        # metodin käyttämä apufufunktio voidaan määritellä näin
        def sorting(player):
            if order == 1:
                return player.points
            elif order == 2:
                return player.goals
            elif order == 3:
                return player.assists
            else:
                return player.points

        sorted_players = sorted(
            self._players,
            reverse=True,
            key=sorting
        )

        result = []
        i = 0
        while i < how_many:
            result.append(sorted_players[i])
            i += 1

        return result

