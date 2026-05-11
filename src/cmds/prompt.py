import discord
from discord.ext import commands
from discord import app_commands
from local_llm import Local_LLM

class Prompt(commands.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    def create_llm_embed(self, input_prompt: str) -> discord.Embed:
        """Generates a Discord embed for the LLM prompt.

        Args:
            input_prompt (str): The user prompt to the LLM.

        Returns:
            discord.Embed: The Discord embed containing the LLM response.
        """
        print(f"LLM Prompt triggered: {input_prompt}")
        response, title = self.get_response(input_prompt)
        return discord.Embed(
            title=title, 
            description=response, 
            color=discord.Color.green()
        )
    
    def get_response(self, input_prompt: str) -> tuple[str, str]:
        """Gets the response and prompt summary from the LLM.

        Args:
            input_prompt (str): The user prompt to the LLM.

        Returns:
            tuple[str, str]: The LLM response and prompt summary.
        """
        llm = Local_LLM()
        return llm.generate_response(input_prompt), llm.generate_prompt_summary(input_prompt)
    
    # This is for slash commands
    @commands.hybrid_command(name="prompt", description="Prompt the llm boi")
    @app_commands.describe(input_prompt="The prompt to the LLM.")
    async def prompt_llm(self, ctx: commands.Context, *, input_prompt: str):
        embed = self.create_llm_embed(input_prompt)
        await ctx.send(embed=embed)

    # This is for @ing the bot
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return
        if self.bot.user.mentioned_in(message):
            ctx = await self.bot.get_context(message)
            if ctx.valid:
                return
            mention_raw = f'<@{self.bot.user.id}>'
            mention_nick = f'<@!{self.bot.user.id}>'
            clean_input = message.content.replace(mention_raw, '').replace(mention_nick, '').strip()
            if clean_input:
                embed = self.create_llm_embed(clean_input)
                await message.reply(embed=embed)

async def setup(bot):
    await bot.add_cog(Prompt(bot))