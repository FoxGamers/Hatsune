import json
import os

class CargoController:
    def __init__(self):
        self.path = "database/config.json"
        self._create_file_if_not_exists()

    # Cria pasta e arquivo se não existir
    def _create_file_if_not_exists(self):
        if not os.path.exists("database"):
            os.makedirs("database")

        if not os.path.isfile(self.path):
            with open(self.path, "w") as f:
                json.dump({}, f, indent=4)

    # Lê dados
    def load_data(self):
        with open(self.path, "r") as f:
            return json.load(f)

    # Salva dados
    def save_data(self, data):
        with open(self.path, "w") as f:
            json.dump(data, f, indent=4)

    # Define cargo por servidor
    def set_cargo(self, guild_id: int, cargo_id: int):
        data = self.load_data()
        guild_id = str(guild_id)

        if guild_id not in data:
            data[guild_id] = {}

        data[guild_id]["cargo_verificacao"] = cargo_id
        self.save_data(data)