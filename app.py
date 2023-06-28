from src.client import DiscordClient

def setup():
    client = DiscordClient()
    client.run()
    

if __name__ == "__main__":
    setup()