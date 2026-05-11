# Gaslight Discord LLM Bot

A simple Discord bot that uses Gemma 4 to generate responses that always agree with the user.

## Getting Started

### Dependencies

* A [Discord Developer](https://discord.com/developers/applications) account
* A dedicated GPU (Tested on an RTX 5070 Ti with 16GB of VRAM)
* Python 3.13

### Installing

1. Clone this GitHub repository.
2. Create a `.env` file in the root directory of the project.
3. Generate your bot token:
   * Go to the [Discord Developer Portal](https://discord.com/developers/applications) and create a new application.
   * Navigate to the **Bot** tab and copy your bot's Token.
4. Add the token to your `.env` file like this:
   ```env
   DISCORD_BOT_KEY=your_copied_token_here
   ```

5. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```

6. Invite the Discord bot to a server of your choice using the OAuth2 URL generator in the Developer Portal.

### Executing Program

1. Navigate to the `src` directory:
   ```bash
   cd src
    ```

2. Run the main Python script:
    ```
    python main.py
    ```

3. Prompt the bot either using `/prompt <prompt>` or `@<bot_name> <prompt>`. 
    ![Example usage of @ command](imgs/at_usage_example2.png)
    ![Example usage of / command](imgs/slash_usage_example.png)
## Acknowledgments

* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)
* [DomPizzie](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)
