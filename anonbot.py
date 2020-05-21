import discord
import hashlib
import os

user_channel = {}   #유저 채널 저장 장소
password_token = "12390usadnlfnlsdn98fne23fn9sdh9fho23h9efdystn23ohrft78eswye2h9o" #서버 비밀번호 생성 토큰

def enc_def(message,contents):  #비밀번호 생성 함수
    enc = hashlib.sha256()
    created_at = str(message.created_at)
    enc.update(created_at.encode('utf-8'))
    enc.update(contents.encode('utf-8'))
    enc.update(password_token.encode('utf-8'))
    encText = enc.hexdigest()
    return encText

class MyClient(discord.Client):
    async def on_message(self, message):
        if(str(message.channel)[:14] == 'Direct Message'and message.author.bot == False):   #만일 메세지가 DM이라면.
            
            cmd = message.content.split(' ')[0]     #공백으로 명령어를 구분한다.
            sender = message.author     #보낸사람을 저장한다
            
            if cmd == 'select':     #선택명령어
                if len(message.content.split())==2:
                    try:
                        target = int(message.content.split()[1])
                        target_channel = client.get_channel(target)
                        if target_channel != None:      #정상
                            if message.author in target_channel.members:    #타겟 채널에 들어와있음
                                user_channel[f"{sender.name}#{sender.discriminator}"] = target  #유저 닉네임 딕셔너리에 타겟추가
                                await message.channel.send("```OK```")
                            else:   #타겟 채널에 들어와있지 않음
                                await message.channel.send("```sorry, we can't find your channel```") 
                        else:   #타겟 채널 없음
                            await message.channel.send("```sorry, we can't find your channel```")
                    except:     #숫자를 입력하지 않아 오류
                        await message.channel.send("```error, channel id is number```")
                else:   #메세지가 2형식이 아님
                    await message.channel.send("```sorry, i can't understand your command```")
            
            #유저의 select가 등록되있다면
            elif f"{sender.name}#{sender.discriminator}" in user_channel.keys():
                
                if message.content == '':           #메세지가 파일이라면
                    for i in message.attachments:   #모든파일을 포문
                        sended_m = await client.get_channel(user_channel[f"{sender.name}#{sender.discriminator}"]).send(file = await i.to_file())   #파일형식으로 전송
                        encText = enc_def(sended_m,i.filename)   #비밀번호 발급
                        await message.channel.send(f"```delete {sended_m.id} {encText}```")   #비밀번호 출력

                elif cmd == 'delete':
                    if len(message.content.split())==3:
                        try:
                            target = int(message.content.split()[1])    #사용자 문자의 id
                            password = message.content.split()[2]       #사용자 문자의 pw
                            select_m = await client.get_channel(user_channel[f"{sender.name}#{sender.discriminator}"]).fetch_message(target)    #삭제할 메세지 선택
                            if select_m.content == '':  #메세지가 파일이라면
                                encText = enc_def(select_m,select_m.attachments[0].filename)
                            else:                       #일반메세지라면
                                encText = enc_def(select_m,select_m.content)
                            if password == encText:     #비밀번호 통일하다면
                                await select_m.delete()
                                await message.channel.send("```OK```")
                            else:
                                await message.channel.send("```PASSWORD WRONG```")
                        except:   #문자 검색시 None 혹은 target 이 문자열
                            await message.channel.send("```sorry, i can't find message```")
                    else:   #문자가 3형식으로 되지 않음
                        await message.channel.send("```sorry, i can't understand your command```")
                
                else:   #아무런 수식어도 붙이지 않음
                    sended_m = await client.get_channel(user_channel[f"{sender.name}#{sender.discriminator}"]).send(message.content)    #메세지를 보낸후 변수에 저장
                    encText = enc_def(sended_m,sended_m.content)    #비밀번호 발급
                    await message.channel.send(f"```delete {sended_m.id} {encText}```")   #비밀번호 출력
            
            #유저의 select 등록이 되있지 않고 select 하지도 않음
            else:
                await message.channel.send("```please select channel```")

client = MyClient()
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)