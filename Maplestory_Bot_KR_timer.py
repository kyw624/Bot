#!/usr/bin/env python3

import os
import time
import discord
from datetime import datetime

client = discord.Client()
channels = [640176809752920065, 640875475291602974]

@client.event
async def on_ready():
    while True:
        now = datetime.utcnow().minute
        if now == 29 or now == 59:  # 알림을 받을 시간 지정
            for i in range(len(channels)):
                await client.get_channel(channels[i]).send("경뿌 1분 전")  # 보낼 메시지 설정
            time.sleep(60)  # 60초 후 재탐색
        else:
            time.sleep(1)  # 1초 후 재탐색
            
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)  # 봇의 토큰 입력
