from copy import deepcopy
import pygame
from Tabuleiro import *
from constantes import *

def minmax(tabuleiro, profundidade, vez):
  if profundidade == 0 or tabuleiro.vencedor() != None:
    return tabuleiro.pontos(), tabuleiro

  if vez:
    lmt_pts = float('-inf')
    m_mov = None
    for mov in todos_movs(tabuleiro, VERMELHO):
      pts = minmax(mov, profundidade-1, False)[0]
      lmt_pts = max(lmt_pts, pts)
      if lmt_pts == pts: m_mov = mov
    return lmt_pts, m_mov
  else:
    lmt_pts = float('inf')
    m_mov = None
    for mov in todos_movs(tabuleiro, BRANCO):
      pts = minmax(mov, profundidade-1, True)[0]
      lmt_pts = min(lmt_pts, pts)
      if lmt_pts == pts: m_mov = mov
    return lmt_pts, m_mov


  #lmt_pts = float('inf') * vez
  #m_mov = None

  #if(vez > 0): cor = BRANCO
  #else: cor = VERMELHO

  #for mov in todos_movs(tabuleiro, cor):
  #  pts = minmax(mov, profundidade -1, vez * -1)[0]
  #  if(vez > 0): lmt_pts = min(lmt_pts, pts)
  #  else: lmt_pts = max(lmt_pts, pts)
  #  if lmt_pts == pts: m_mov = mov


def sim_mov(peca, mov, tabuleiro, pulo):
  if pulo:
    print(f'Mov: {peca.posicao[::-1]} -> {mov[::-1]}\nPulo: ',end='')
  tabuleiro.movimenta(peca, mov[0], mov[1])
  if pulo:
    #tabuleiro.mata_pecas(pulo)
    for i in pulo:
      tabuleiro.tabuleiro[i.posicao[0]][i.posicao[1]] = None
      i.morte = True
      #if peca.cor == BRANCO: tabuleiro.peca2 -= 1
      #else: tabuleiro.peca1 -= 1

      print(f'{i.posicao[::-1]} -> {i.morte}', end='')
    print('\n')
  print('-- Dps do kill --')
  for _ in tabuleiro.pecas_por_cor(BRANCO): print(_.posicao[::-1])
  print('--  --')



  return tabuleiro


def todos_movs(tabuleiro, cor):
  movs = []
  for peca in tabuleiro.pecas_por_cor(cor):
    mov_v = tabuleiro.pega_movimentos_validos(peca)
    for mov, pulo in mov_v.items():
      tmp_tab = Tabuleiro(480, 480)
      for i in range(len(tabuleiro.tabuleiro)):
        tmp_tab.tabuleiro.append([])
        for j in range(len(tabuleiro.tabuleiro[i])):
          p = tabuleiro.tabuleiro[i][j]
          if p != None:
            tmp_tab.tabuleiro[i].append(Peca(p.cor, p.posicao, p.linha_transforma_dama, p.direcao))
          else:
            tmp_tab.tabuleiro[i].append(None)
      tmp_tab.altura = deepcopy(tabuleiro.altura)
      tmp_tab.largura = deepcopy(tabuleiro.largura)
      tmp_tab.linhas = deepcopy(tabuleiro.linhas)
      tmp_tab.colunas = deepcopy(tabuleiro.colunas)
      tmp_tab.peca1 = deepcopy(tabuleiro.peca1)
      tmp_tab.peca2 = deepcopy(tabuleiro.peca2)
            
      tmp_p = tmp_tab.pega_peca(peca.posicao[0], peca.posicao[1])
      n_tab = sim_mov(tmp_p, mov, tmp_tab, pulo)
      movs.append(n_tab)
  

  return movs
