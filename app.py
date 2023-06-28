from src.client import DiscordClient
import logging

def setup():
    client = DiscordClient()
    client.run()

if __name__ == "__main__":
    setup()