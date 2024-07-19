intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def parse_date(date_str):
    formats = ['%Y/%m/%d', '%Y/%-m/%-d', '%Y年%-m月%-d日']
    for fmt in formats:
        try:
            return datetime.datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    return None

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    # ボット自身のメッセージには反応しない
    if message.author == client.user:
        return

    date = parse_date(message.content)
    if date:
        day_of_week = days_of_week_japanese[date.weekday()]
        date_str = f'{date.year}年{date.month}月{date.day}日'
        await message.channel.send(f'{date_str}のあなたは{day_of_week}生まれです。')

# Discord Botのトークンを設定
client.run('DISCORD_TOKEN')
