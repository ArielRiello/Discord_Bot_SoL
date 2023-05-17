import requests
from bs4 import BeautifulSoup

def get_campeao_rank(campeao, rota, elo):

    elo_ptbr = {
        'iron': 'ferro',
        'bronze': 'bronze',
        'prata': 'silver',
        'ouro': 'gold',
        'platina': 'platinum',
        'diamante': 'diamond',
        'mestre': 'master',
        'granmestre': 'grandmaster',
        'desafiante': 'challenger'
        }
    
    chave = elo
    if chave in elo_ptbr:
        valor_elo = elo_ptbr[chave]

    url = f"https://u.gg/lol/champions/{campeao}/build/{rota}?rank={valor_elo}&region=br1"
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, "html.parser")

    win_rate = soup.find('div', attrs={'class': 'win-rate'})
    if win_rate is not None:
        win_rate_fomatado = win_rate.text
    else:
        win_rate_fomatado = "Não encontrado"

    rank = soup.find('div', attrs={'class': 'overall-rank'})
    if rank is not None:
        rank_formatado = rank.text
    else:
        rank_formatado = "Não encontrado"

    rank_tier = soup.find('div', attrs={'class': 'champion-tier media-query media-query_MOBILE_LARGE__DESKTOP_LARGE'})
    if rank_tier is not None:
        if rank_tier.text[1] == '+':
            rank_tier_formatado = rank_tier.text[:2]
        else:
            rank_tier_formatado = rank_tier.text[:1]
    else:
        rank_tier_formatado = "Não encontrado"
    
    return f'{campeao}/{rota}/{elo}: |     Tier {rank_tier_formatado}   |   {rank_formatado}    |   {win_rate_fomatado}    |'
