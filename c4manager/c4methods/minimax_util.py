from . c4functions import *

def utility(state):
    winner = get_winner(state)
    if winner == 'X':
      return 10000
    if winner == 'O':
      return -10000

def count_hv(rows, colour, count):
    n = 0
    for row in rows:
      for i in range(len(row) - count + 1):
        winner = True
        for j in range(count):
          if(row[i + j] != colour):
            winner = False
            break
        if winner:
          n += 1
    return n
  
def count_diag(rows, colour, count):
    n = 0
    for y in range(len(rows) - count + 1):
        for x in range(len(rows[0])):
          winner = True
          # RIGHT TO LEFT
          for j in range(count):
            if((x - j < 0) or (y + j > len(rows) - 1)):
              winner = False
              break
            if(rows[y + j][x - j] != colour):
              winner = False
              break
          
          if winner:
            n += 1
          
          # LEFT TO RIGHT
          winner = True
          for j in range(count):
            if((x + j > len(rows[0]) - 1) or (y + j > len(rows) - 1)):
              winner = False
              break
            if(rows[y + j][x + j] != colour):
              winner = False
              break

          if winner:
            n += 1
    return n


def score(state, player):
  rows = get_rows(state)
  # count amount of player in board
  count_tokens = 0
  for row in rows:
    for x in row:
      if(x == player):
        count_tokens += 1
  
  # count verticals
  cols = []
  for i in range(7):
      col = []
      for j in range(len(rows)):
        col.append(rows[j][i])
      cols.append(col)

  # add em up
  count_two = count_hv(rows, player, 2) + count_hv(cols, player, 2) + count_diag(rows, player, 2)
  count_three = count_hv(rows, player, 3) + count_hv(cols, player, 3) + count_diag(rows, player, 3)
  count_two -= 2 * count_three
  
  two_in_a_row = 10 * count_two
  three_in_a_row = 100 * count_three
  
  return count_tokens + two_in_a_row + three_in_a_row

def evaluation(state):
  return score(state, 'X') - score(state, 'O')

def max_value(state, player, max_depth, depth):
    if(depth > max_depth):
      return (evaluation(state), -1, 1)
    
    if (get_winner(state) != None):
      return (utility(state), -1, 1)
    
    v = float('-inf')
    action = -1
    successors = get_successors(state, player)

    if(player == 'X'):
      next_player = 'O'
    else:
      next_player = 'X'
    
    explored = 0
    
    for s, a in successors:
      # max 
      minval = min_value(s, next_player, max_depth, depth + 1)
      explored += minval[2]
      if(minval[0] > v):
        v = minval[0]
        action = a
    return (v, action, 1 + explored)
 
def min_value(state,player, max_depth, depth):
    if(depth > max_depth):
      return (evaluation(state), -1, 1)
    
    if (get_winner(state) != None):
      return (utility(state), -1, 1)
    
    v = float('inf')
    action = -1
    successors = get_successors(state, player)
    
    if(player == 'X'):
      next_player = 'O'
    else:
      next_player = 'X'
      
    explored = 0

    for s, a in successors:
      # min 
      maxval = max_value(s, next_player, max_depth, depth + 1)
      explored += maxval[2]
      if(maxval[0] < v):
        v = maxval[0]
        action = a

    return (v, action, 1 + explored)
    

def minimax_decision(state, player, max_depth):
    v = min_value(state, player, max_depth, 1)
    return v[1]

def max_value_ab(state, player, max_depth, depth, alpha, beta):
    if (get_winner(state) != None):
      return (utility(state), -1, 1)
    
    if(depth > max_depth):
      return (evaluation(state), -1, 1)
    
    v = float('-inf')
    action = -1
    successors = get_successors(state, player)

    if(player == 'X'):
      next_player = 'O'
    else:
      next_player = 'X'
    
    explored = 0
    
    for s, a in successors:
      # max 
      minval = min_value_ab(s, next_player, max_depth, depth + 1, alpha, beta)
      explored += minval[2]
      
      if(minval[0] > v):
        v = minval[0]
        action = a

      if(v >= beta):
        return(v, action, 1 + explored)
      
      alpha = max(v, alpha)

    return(v, action, 1+explored)
    
def min_value_ab(state, player, max_depth, depth, alpha, beta):
    if (get_winner(state) != None):
      return (utility(state), -1, 1)
    
    if(depth > max_depth):
      return (evaluation(state), -1, 1)
    
    v = float('inf')
    action = -1
    successors = get_successors(state, player)
    
    if(player == 'X'):
      next_player = 'O'
    else:
      next_player = 'X'
      
    explored = 0

    for s, a in successors:
      # min 
      maxval = max_value_ab(s, next_player, max_depth, depth + 1, alpha, beta)
      explored += maxval[2]
      if(maxval[0] < v):
        v = maxval[0]
        action = a
        
      if(v <= alpha):
        return (v, action, 1 + explored)
      beta = min(beta, v)

    return (v, action, 1 + explored)

def alpha_beta_search(state, player, max_depth):
    v = min_value_ab(state, player, max_depth, 1, float('-inf'), float('inf'))
    
    return v[1]