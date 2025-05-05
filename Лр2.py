def draw_board(board):
    print("-" * 13)
    for i in range(3):
        print(f"| {board[i * 3]} | {board[i * 3 + 1]} | {board[i * 3 + 2]} |")
        print("-" * 13)


def take_input(player_token, board):
    while True:
        player_answer = input(f"Куда поставим {player_token}? (1-9): ")
        try:
            player_answer = int(player_answer)
        except ValueError:
            print("Некорректный ввод. Введите число от 1 до 9.")
            continue

        if 1 <= player_answer <= 9:
            index = player_answer - 1
            if board[index] not in ("X", "0"):
                board[index] = player_token
                break
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")


def check_win(board):
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # горизонтали
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # вертикали
        (0, 4, 8), (2, 4, 6)              # диагонали
    ]
    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c]:
            return board[a]
    return None


def choose_player_symbol():
    while True:
        choice = input("Игрок 1, выберите X или 0: ").upper()
        if choice in ("X", "0"):
            return choice, "0" if choice == "X" else "X"
        print("Неверный выбор. Пожалуйста, введите X или 0.")


def main():
    board = list(range(1, 10))
    move_count = 0

    player1, player2 = choose_player_symbol()
    print(f"Игрок 1 играет за {player1}, Игрок 2 играет за {player2}.")

    while True:
        draw_board(board)
        current_player = player1 if move_count % 2 == 0 else player2
        take_input(current_player, board)
        move_count += 1

        winner = check_win(board)
        if winner:
            draw_board(board)
            print(f"{winner} выиграл!")
            break

        if move_count == 9:
            draw_board(board)
            print("Ничья!")
            break


if __name__ == "__main__":
    main()