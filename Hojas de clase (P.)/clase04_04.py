# def reverse_list(list_1):
#     output = []
#     for i in range(len(list_1), 0, -1):
#         output.append(list_1[i])
#     return output

# def reverse_list_optimized(list_1):
#     left = 0
#     right = len(list_1)-1
    
#     while left <= right:
#         aux = list_1[right]
#         list_1[right] = list_1[left]
#         list_1[left] = aux
    
#         left +=1
#         right -=1
    
#     return list_1

# def main():
#     list_1 = [1,2,3,4]
#     list_1 = reverse_list_optimized(list_1)
#     print(list_1)    
    
# if __name__ == "__main__":
#     main()


def psr ():
    player1 = 0
    player2 = 0
    action_p1 = input("Accion (j1):")
    action_p2 = input("Accion (j2):") 
    
    while player1 == 3 or player2 == 3:    
        win_cond(action_p1, action_p2, player2)
        win_cond(action_p2, action_p1, player1)
        
        if player1 == 3:
            print ("player1 wins!")
        if player2 == 3:
            print ("player2 wins!")    
        pass
    
 
def win_cond (action_win, action_los, winner):
    if action_los == "s" and action_win == "r":
        winner += 1
    if action_los == "r" and action_win == "p":
        winner += 1
    if action_los == "p" and action_win == "s":
        winner += 1
    elif action_los == action_win:
        winner += 0
        
psr()