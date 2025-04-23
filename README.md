# PythonAI
A python AI bot in discord using Ollama. To utilize this, view the comments in the Python file, or read a summary here.
https://discord.gg/venGcddV3H (Testing Server)

To start, install Ollama and install the bot you'd like to use by typing it in the terminal. (Something like `ollama pull llama3.3`) 
Once it loads, close the terminal window so it stops the bot. (Make sure the Ollama app is still running.)
Next, create a bot with all possible intents.
Grab the token and put it in the botkey variable.
Replace the `userdefmodel` variable with a string for the bot you choose to use. (Use the same model from the above `ollama pull llama3.3` string. You'd insert `"llama3.3"`
On the Oauth page, only check the bot tab.
Next invite it to your server with admin permissions.

Set the botkey variable to your bots token (the secret code you get upon creation.)
Now, make sure the Ollama app is still running. Don't start any models just make sure it shows in task manager. 
Then finally, run the Python file!

> [!CAUTION]
> Do **NOT** share your bot token with anyone! This is very important!

> [!TIP]
> The Ollama application may automatically start due to how I wrote the code.
