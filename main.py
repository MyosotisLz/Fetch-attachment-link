@bot.command(name='getlink')
async def download_attachments(ctx):
    replied_message_reference = ctx.message.reference
    if replied_message_reference:
        replied_message = await ctx.fetch_message(replied_message_reference.message_id)
        if replied_message.attachments:
            files = replied_message.attachments
            embed = discord.Embed(title='Attachment Links', color=0x0080ff)

            for index, file in enumerate(files, start=1):
                attachment_url = file.url  
                attachment_filename = file.filename
                download_link = attachment_url  
                embed.add_field(name=f'File {index}: {attachment_filename}', value=f'[attachment link]({download_link})', inline=False)

            await ctx.send(embed=embed)
            return

    await ctx.send('No attachments found in the target message.')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  

    if bot.user.mentioned_in(message):
        await message.channel.send('To get attachment links, use the command `!getlink`.')

    await bot.process_commands(message)
