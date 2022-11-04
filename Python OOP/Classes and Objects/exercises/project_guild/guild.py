from classes_and_objects.exercise.project_guild.player import Player


class Guild:

    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."

        if player.guild != Player.DEFAULT_GUILD:
            return f"Player {player.name} is in another guild."

        self.players.append(player.name)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                self.players.remove(player)
                player.guild = Player.DEFAULT_GUILD
                return f"Player {player_name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        result = f'Guild: {self.name}\n'
        for player in self.players:
            result += player.player_info() + '\n'

        return result.strip()
