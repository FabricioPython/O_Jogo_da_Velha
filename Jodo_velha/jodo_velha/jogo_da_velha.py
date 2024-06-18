import sys
from functools import wraps

import keyboard
import numpy as np
from layout import render_lay
from rich.columns import Columns
from rich.console import Console
from rich.prompt import Prompt

# jogo da velha 1.0 - em Desenvolvimento
# by Fabricio


# display e set valor do array
def display(func):
    # shape(3,3)
    array = np.array([['', '', ''], ['', '', ''], ['', '', '']])

    @wraps(func)
    def wrapper(*args, **kwargs):
        pos, valor = func(*args, **kwargs)
        a, b = mapa_pos[pos]
        array[a][b] = valor

        a = array[0][0]
        b = array[0][1]
        c = array[0][2]
        d = array[1][0]
        e = array[1][1]
        f = array[1][2]
        g = array[2][0]
        h = array[2][1]
        i = array[2][2]

        render_lay(a, b, c, d, e, f, g, h, i)

    return wrapper


# Pega Posição e valor
@display
def jogar(*args, **kwargs):
    prompt = Prompt()
    pos = (
        prompt.ask(
            '[b yellow]Escolha a Posição:[/]',
            choices=['1', '2', '3', '4', '5', '6', '7', '8', '9'],
        )
        .upper()
        .strip()
    )

    valor = (
        prompt.ask('[b yellow]Símbolo: [/]', choices=['x', 'o'])
        .upper()
        .strip()
    )
    return pos, valor


# mapa de posições
mapa_pos = {
    '1': (0, 0),
    '2': (0, 1),
    '3': (0, 2),
    '4': (1, 0),
    '5': (1, 1),
    '6': (1, 2),
    '7': (2, 0),
    '8': (2, 1),
    '9': (2, 2),
}
# a fazer
mapa_wins = {...}


# display inicial
d = ['' for i in range(9)]

# execução
print(render_lay(*d))

while True:
    if keyboard.is_pressed('Ctrl'):
        jogar()

    elif keyboard.is_pressed('space'):
        console = Console()
        Columns(
            console.print(
                '### Até a próxima noob :snake: :thumbsup:',
                style='red  blink',
                justify='center',
            ),
            align='center',
        )
        sys.exit()


# ver possivel solução para o tratamento da strings do display <- Em andamento
# contador de vitoria e derrotas
# colorir caso o jogo termine
# talvez mensagens de motivaçãos ofensiva kk:
# vove é muito ruim, o jogador x é seu fregues?
