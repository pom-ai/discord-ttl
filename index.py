import iridi 
import discord
import requests 
import os

# Text Color
gradient = iridi.preset(["#8A2387", "#E94057", "#F27121"])
soft = iridi.preset(["#D3959B", "#BFE6BA"])
succes = iridi.preset(["#57C84D", "#ABE098"])

# Menu 
def menu():
    gradient.print(f'''
        ██████  ██ ███████  ██████  ██████  ██████  ██████      ████████ ████████ ██      
        ██   ██ ██ ██      ██      ██    ██ ██   ██ ██   ██        ██       ██    ██      
        ██   ██ ██ ███████ ██      ██    ██ ██████  ██   ██        ██       ██    ██      
        ██   ██ ██      ██ ██      ██    ██ ██   ██ ██   ██        ██       ██    ██      
        ██████  ██ ███████  ██████  ██████  ██   ██ ██████         ██       ██    ███████ 
                                                                                  
                                       Github: Pom-AI               
''', bold=True)

# Discord token checker
def token_checker(token):
    headers = {'Authorization': token}
    url = "https://discord.com/api/v10/users/@me"
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        return True
    else:
        return False

# Discord bot
class TTL():
    def __init__(self, token, time):
        self.token = token
        self.time = time
        self.client = discord.Client()
        self.client.event(self.on_message)

    async def on_message(self, message):
        if message.author.id == self.client.user.id:
            await message.delete(delay=self.time)
            succes.print(f"Deleted message: {message.content} in {message.channel.name} in {message.guild.name}")

    def run(self):
        self.client.run(self.token)

# Main Thing
def main():
    menu()
    
    token = gradient.input("Please enter your account token (https://dar.vin/discord-token): ")
    while not token_checker(token):
        gradient.print("Invalid token. Please try again.")
        token = gradient.input("Please enter your account token (https://dar.vin/discord-token): ")
    time = None
    while time is None:
        try:
            time = int(soft.input("Please enter the time (in seconds) to delete: "))
        except ValueError:
            gradient.print("Invalid input. Please enter a valid integer.")

    sure = gradient.input("Are you sure you want to delete all your messages? (y/n): ")
    while sure.lower() not in ["y", "n"]:
        sure = gradient.input("Invalid input. Please enter either y or n: ")
    if sure.lower() == "y":
        succes.print("Deleting messages...")

        TTL(token, time).run()
    elif sure.lower() == "n":
        gradient.print("Exiting...")
        exit()
    else :
        gradient.print("Invalid input. Just type y or n.")

if __name__ == "__main__":
	main()