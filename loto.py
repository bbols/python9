import random

class LotoGame:
    def __init__(self):
        # Генерация карточки игрока: 5 строк по 5 номеров от 1 до 90
        self.player_card = self.generate_card()
        self.called_numbers = []
        self.game_over = False

    def generate_card(self):
        card = []
        for _ in range(5):
            row = random.sample(range(1, 91), 5)
            card.append(row)
        return card

    def draw_number(self):
        if self.game_over:
            print("Игра уже завершена.")
            return

        while True:
            number = random.randint(1, 90)
            if number not in self.called_numbers:
                self.called_numbers.append(number)
                print(f"Выпавшее число: {number}")
                self.check_number(number)
                break

    def check_number(self, number):
        for row in self.player_card:
            if number in row:
                row[row.index(number)] = 'X'

        self.print_card()

        if self.check_winner():
            print("Поздравляем! Вы выиграли!")
            self.game_over = True

    def check_winner(self):
        for row in self.player_card:
            if any(isinstance(num, int) for num in row):
                return False
        return True

    def print_card(self):
        for row in self.player_card:
            print(" ".join(str(num).rjust(2) for num in row))
        print()

def main():
    game = LotoGame()
    print("Ваша карточка:")
    game.print_card()

    while not game.game_over:
        input("Нажмите Enter, чтобы вытянуть число...")
        game.draw_number()


main()
