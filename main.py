import random

def print_board(board, qr, qc): # for the UI
    rows = len(board)
    cols = len(board[0])
    print("\ncurrent board:")
    for r in range(rows-1, -1, -1): #from top row to bottom
        row = "|"
        for c in range(cols):
            if r == qr and c == qc: #if the queen is at this cell
                row += " Q |"
            else:
                row += " . |"
        print(row)
        print("-" * (4 * cols + 1)) #for the seperator line
    labels = "  "
    for c in range(cols):
        labels += f"{c}   "
    print(labels)
    print() #put it just for spacing



def get_int(msg, minv, maxv): # get input, used more like a helper function to check validity of inputs
    while True:#repeat until valid
        try:
            v = int(input(msg))
            if v < minv or v > maxv:
                raise ValueError
            return v
        except ValueError:
            print('invalid input, try agian')



def get_board_size():
    r = get_int('enter board rows (>=2): ', 2, 100)
    c = get_int('enter board cols (>=2): ', 2, 100)
    return r, c




def get_init_pos(rows, cols): #the first player chooses the initial pos
    while True:
        qr = get_int('enter initial row: ', 0, rows-1)
        qc = get_int('enter initial col: ', 0, cols-1)
        if qr == 0 and qc == 0:
            print('cant place in winning corner, choose another')
        else:
            return qr, qc




#(current row of the queen, current column of the queen, total number of rows, tot num of cols)
def human_move(qr, qc, rows, cols):
    print('human move:')
    while True:
        nr = get_int('row: ', 0, rows-1) #new row
        nc = get_int('col: ', 0, cols-1) #new coloum
        dr = qr - nr
        dc = qc - nc

        #the constraints of the game
        if dr < 0 or dc < 0:
            print('movment must be left/down/diag-left-down')
        elif dr == 0 and dc == 0:
            print('must move at least 1')
        elif dr != 0 and dc != 0 and dr != dc:
            print('invalid diagonal')
        else:
            return nr, nc



def get_moves(qr, qc):# generates all legal queen moves from current queen row and column
    moves = []
    for step in range(1, max(qr, qc)+1):
        if qc-step >= 0:
            moves.append((qr, qc-step))
        if qr-step >= 0:
            moves.append((qr-step, qc))
        if qr-step >= 0 and qc-step >= 0:
            moves.append((qr-step, qc-step))
    return moves



# global counters for nodes visited by minimax and alpha-beta searches
tree_count = 0  # counts nodes in minimax
alpha_beta_count = 0  # counts nodes in alpha-beta pruning



#minmax algo
def minimax(qr, qc, rows, cols, maximizing):
    global tree_count
    tree_count += 1  # count this node

    if qr == 0 and qc == 0:  # check if both qr and qc are 0 - terminal
        if maximizing:# maximizing = True; meaning it was going to AI turn--> so it has lost
            return -1 # AI lost
        else:
            return 1 # AI won

    if maximizing: #No winner yet --> AI turn
        best = -float('inf')
        for nr, nc in get_moves(qr, qc):
            best = max(best, minimax(nr, nc, rows, cols, False))# maximize
        return best


    else:
        worst = float('inf')
        for nr, nc in get_moves(qr, qc):
            worst = min(worst, minimax(nr, nc, rows, cols, True)) # minimize
        return worst



#alpha beta algo
def alphabeta(qr, qc, rows, cols, alpha, beta, maximizing):
    global alpha_beta_count
    alpha_beta_count += 1

    #samee explanation as minmax
    if qr == 0 and qc == 0:
        if maximizing:
            return -1
        else:
            return 1

    if maximizing:
        val = -float('inf')
        for nr, nc in get_moves(qr, qc):
            val = max(val, alphabeta(nr, nc, rows, cols, alpha, beta, False))
            alpha = max(alpha, val) # update alpha - The extra step over minmax
            if alpha >= beta:# prune
                break
        return val

    else:
        val = float('inf')
        for nr, nc in get_moves(qr, qc):
            val = min(val, alphabeta(nr, nc, rows, cols, alpha, beta, True))
            beta = min(beta, val)# update beta
            if beta <= alpha: # prune
                break
        return val




def ai_move(qr, qc, rows, cols):
    global tree_count, alpha_beta_count
    tree_count =0
    alpha_beta_count= 0
    use_alphabeta = rows * cols >= 49
    best_move= None,
    best_score= -float('inf')
    if use_alphabeta:
        for m in get_moves(qr, qc): # test each move
            score = alphabeta(m[0], m[1], rows, cols, -float('inf'), float('inf'), False)
            if score > best_score:
                best_score = score
                best_move =  m
        print('nodes this move:', alpha_beta_count)

    else:
        for m in get_moves(qr, qc):
            score = minimax(m[0], m[1], rows, cols, False)
            if score > best_score:
                best_score, best_move = score, m
        print('nodes this move:', tree_count)
    return best_move, use_alphabeta # returns move and whether alphabeta was used




def main():
    while True:
        rows, cols = get_board_size()
        mode = get_int('choose mode: 1 human-vs-human, 2 human-vs-ai: ', 1, 2)

        # determine who goes first
        if mode == 1:
            first = random.choice([1, 2]) # human-vs-human: random start

        else:
            choice = get_int('first? 1 you,2 ai: ', 1, 2) # human-vs-ai: ask player if they go first
            if choice == 1:
                first = 1
            else:
                first = 2
        print(f'player {first} starts')


        # initial placement by first player
        if mode == 2 and first == 2:
            while True:# AI places randomly
                qr = random.randint(0, rows-1)
                qc = random.randint(0, cols-1)
                if qr != 0 or qc != 0:
                    print(f'AI places initial queen at {qr},{qc}')
                    break
        else:
            print(f'player {first} chooses initial position')
            qr, qc = get_init_pos(rows, cols)

        # total counts of nodes visited across the wholle game for each AI algorithm
        total_mm = total_ab = 0  # mm = minimax total, ab = alpha-beta total

        if first == 2:
            turn = 1
        else:
            turn = 2
        # game loop
        while True:
            print_board([[None]*cols for _ in range(rows)], qr, qc)
            if mode == 2 and turn == 2:
                (nr, nc), used_ab = ai_move(qr, qc, rows, cols)
                if used_ab:
                    total_ab += alpha_beta_count
                else:
                    total_mm += tree_count
                print(f'ai moves to {nr},{nc}')
            else:
                nr, nc = human_move(qr, qc, rows, cols)
                print(f'player {turn} moves to {nr},{nc}')
            qr, qc = nr, nc
            if qr == 0 and qc == 0:
                print_board([[None]*cols for _ in range(rows)], qr, qc)
                print(f'player {turn} wins! total mm: {total_mm}, ab: {total_ab}')
                break
            turn = 1 if turn == 2 else 2

        again = input('play again? (y/n): ').strip().lower()
        if again != 'y':
            print('goodbye!')
            break

if __name__ == '__main__':
    main()
