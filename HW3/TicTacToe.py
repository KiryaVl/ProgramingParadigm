# Контекст
# Вероятнее всего, вы с детства знакомы с этой игрой. Пришло
# время реализовать её. Два игрока по очереди ставят крестики
# и нолики на игровое поле. Игра завершается когда кто-то
# победил, либо наступила ничья, либо игроки отказались
# играть.
# ● Задача
# Написать игру в “Крестики-нолики”. Можете использовать
# любые парадигмы, которые посчитаете наиболее
# подходящими. Можете реализовать доску как угодно - как
# одномерный массив или двумерный массив (массив массивов).
# Можете использовать как правила, так и хардкод, на своё
# усмотрение. Главное, чтобы в игру можно было поиграть через
# терминал с вашего компьютера

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print("   7 | 8 | 9")
        print("   ---------")
        print("   4 | 5 | 6")
        print("   ---------")
        print("   1 | 2 | 3")
        print(f"\n _____________\n")

        for i in range(3):
            print("|", end="")
            for j in range(3):
                print(f" {board[i][j]} |", end="")
            print()
            if i < 2:
                print("------------")

        while True:
            try:
                move = input(f"Игрок {current_player}, введите номер поля (7-9, 4-6, 1-3): ")
                if move not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    print("Некорректный ход! Попробуйте снова.")
                    continue
                position = int(move)
                position_map = {7: (0, 0), 8: (0, 1), 9: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2), 1: (2, 0), 2: (2, 1), 3: (2, 2)}
                row, col = position_map[position]
                if board[row][col] != ' ':
                    print("Некорректный ход! Это поле уже занято.")
                    continue
                board[row][col] = current_player
                break
            except ValueError:
                print("Некорректный ввод! Введите номер поля от 7 до 9, 4 до 6 или 1 до 3.")

        if any(all(cell == current_player for cell in row) for row in board) or \
                any(all(board[i][j] == current_player for i in range(3)) for j in range(3)) or \
                all(board[i][i] == current_player for i in range(3)) or \
                all(board[i][2 - i] == current_player for i in range(3)):
            print(f"Игрок {current_player} победил!")
            break
        elif all(cell != ' ' for row in board for cell in row):
            print("Ничья! Никто не победил.")
            break
        else:
            current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()

