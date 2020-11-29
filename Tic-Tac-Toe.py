board = {'top_l':'','top_m':'','top_r':'','mid_l':'','mid_m':'','mid_r':'','bot_l':'','bot_m':'','bot_r':''}
count=1
s=''
choice=''
won_player=''
print("Let's start the 'Tic-Tac-Toe' game.. ")
while count<10:
    if count%2==1:
        s='o'
    else:
        s='x'
    print("Enter your position on the board, player '",s,"'"," :")
    choice=input()
    board[choice]=s
    print("After placing you, the board is: ")
    print()
    print("   ", board['top_l'], "   ", "|", "   ", board['top_m'], "   ", "|", "   ", board['top_r'], "   ")
    print("________________________________________________________________________________________________")
    print("   ", board['mid_l'], "   ", "|", "   ", board['mid_m'], "   ", "|", "   ", board['mid_r'], "   ")
    print("________________________________________________________________________________________________")
    print("   ", board['bot_l'], "   ", "|", "   ", board['bot_m'], "   ", "|", "   ", board['bot_r'], "   ")
    count+=1
    if count>4:
        if board['top_l']==s and  board['top_m']==s and  board['top_r']==s :
            won_player=s
        elif board['mid_l']==s and  board['mid_m']==s and  board['mid_r']==s :
            won_player = s
        elif board['bot_l']==s and  board['bot_m']==s and  board['bot_r']==s :
            won_player = s
        elif board['top_l']==s and  board['mid_l']==s and  board['bot_l']==s :
            won_player=s
        elif board['top_m'] == s and board['mid_m'] == s and board['bot_m'] == s:
            won_player = s
        elif board['top_r'] == s and board['mid_r'] == s and board['bot_r'] == s:
            won_player = s
        elif board['top_l'] == s and board['mid_m'] == s and board['bot_r'] == s:
            won_player = s
        elif board['top_r'] == s and board['mid_m'] == s and board['bot_l'] == s:
            won_player = s
    if won_player=='x':
        x_player=True
        print("'x' player has won this game!!!")
        break
    elif won_player=='o':
        o_player=True
        print("'o' player has won this game!!!")
        break
if won_player=='':
    print('You both were great!')
print("Hope you had fun!!!!")