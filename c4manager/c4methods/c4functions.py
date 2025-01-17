def check_hv(rows, colour):
    for row in rows:
      for i in range(len(row) - 4 + 1):
        winner = True
        for j in range(4):
          if(row[i + j] != colour):
            winner = False
            break
        if winner:
          return True
    return False

def check_diag(rows, colour):
    for y in range(len(rows) - 4 + 1):
        for x in range(len(rows[0])):
          winner = True
          # RIGHT TO LEFT
          for j in range(4):
            if((x - j < 0) or (y + j > len(rows) - 1)):
              winner = False
              break
            if(rows[y + j][x - j] != colour):
              winner = False
              break
          
          if winner:
            return True
          
          # LEFT TO RIGHT
          winner = True
          for j in range(4):
            if((x + j > len(rows[0]) - 1) or (y + j > len(rows) - 1)):
              winner = False
              break
            if(rows[y + j][x + j] != colour):
              winner = False
              break

          if winner:
            return True
    return False

def get_rows(contents):
    return(contents.split(","))
    
def get_winner(contents):
    # check horizontals 
    rows = get_rows(contents)
    if(check_hv(rows, 'X')):
      return 'X'
    elif(check_hv(rows, 'O')):
      return 'O'
    
    # check verticals 
    cols = []
    # get columns
    for i in range(7):
      col = []
      for j in range(len(rows)):
        col.append(rows[j][i])
      cols.append(col)
    
    if(check_hv(cols, 'X')):
      return 'X'
    elif(check_hv(cols, 'O')):
      return 'O'
    
    # check diagonals
    if(check_diag(rows, 'X')):
      return 'X'
    elif(check_diag(rows, 'O')):
      return 'O'

    return None
    
def get_successors(state, player):
    # go from left to right
    successors = []
    for x in range(7):
      copy_rows = get_rows(state)
      changed = False
      for y in range(6):
        if(copy_rows[y][x] == '.'):
          row = list(copy_rows[y])
          row[x] = player
          copy_rows[y] = "".join(row)
          changed = True
          break
      if(changed):
        successors.append((",".join(copy_rows), x))
      
    return successors 