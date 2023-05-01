import discord
from lol_ws import *

async def on_bot_message(bot, message):
    if message.author == bot.user:
        return
    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------#   

    if message.content.startswith('>help'):
        await message.channel.send(f"""
        {message.author} 
        :saluting_face: AQUI ESTÃO MEUS COMANDOS SENHOR(a)!!! :saluting_face:

        --------------------------------------------------------------------
        
        -> Comandos de Servidor

        Comando: ">on" - Verifica se estou online
        Comando: ">ping" - Verifica a latência atual do Servidor SoL
        Comando: ">tp" "@nick" "sala" - Teleporta alguem de sala!

        --------------------------------------------------------------------
        
        -> Comandos LoL
        comando: ">loltier <campeão> <rota> <elo>" # Ex: garen top gold
        Exibe o Tier | Rank | Win Rate do Campeao # Ex: S+ | 1/50 | 99%
        
        --------------------------------------------------------------------
        """)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
    if message.content.startswith('>on'):
        await message.channel.send(f'{message.author}, Estou sim ! :stuck_out_tongue_winking_eye: ')

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

    if message.content.startswith('>ping'):
        latency = bot.latency * 1000
        await message.channel.send(f':ping_pong: Pong! Latência Servidor SoL: {latency:.2f}ms')

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

    if message.content.startswith('>tp'):
        # Verifica se a mensagem foi enviada em um canal de voz
        if not message.author.voice:
            await message.channel.send('Você precisa estar em um canal de voz para usar esse comando!')
            return
        
        # Verifica se o membro mencionado está em um canal de voz
        if not message.mentions:
            await message.channel.send('Você precisa escolher um alvo para o feitiço!')
            return
        
        member = message.mentions[0]
        voice_channel = member.voice.channel
        
        # Verifica se a sala de áudio especificada existe
        requested_channel = message.content.split()[-1]
        channel = discord.utils.get(message.guild.voice_channels, name=requested_channel)
        
        if not channel:
            await message.channel.send(f'O destino do feitiço: "{requested_channel}" não existe!')
            return
        
        # Move o membro para a sala de áudio especificada
        await member.move_to(channel)
        await message.channel.send(f'{message.author} lançou o Feitiço: :scroll: Teleporte em {member} com destino para: "{requested_channel}"!')

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

    if message.author == bot.user:
        return

    if message.content.startswith('>loltier'):
            comando = message.content.split(' ')

            if len(comando) != 4:
                await message.channel.send('Comando inválido. Digite ">rank <campeão> <rota> <elo>"')
            else:
                campeao = comando[1]
                rota = comando[2]
                elo = comando[3]
                
                resultado = get_campeao_rank(campeao, rota, elo)
                
                await message.channel.send(resultado)
    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------#    
