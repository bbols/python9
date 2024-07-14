#card loto
import random
class game_loto():
    def __init__(self):
        self.user = []
        self.game_numbers = []
        self.game_succes=False

    def start(self):
        self.game_numbers=self.game_genearator_card()
        print(f"\nИгра началась!")
        i=0
        while True:
            i+=1
            if self.game_succes:
                break

            try:
                print(f"Выпало число: {self.game_numbers[i]} || {i} из {90} чисел")
                [user.user_close_card(self.game_numbers[i]) for user in self.user]
                [user.user_card_view() for user in self.user]
                self.check_X_user()
            except:
                break
        print("Игра завершена")

    def game_genearator_card(self):
        return [card for card in random.sample(range(1,91),90)]
    def number_close(self,number):
        self.number_black_list.append(number)
    def number_clear(self):
        self.number_black_list=[]

    def user_add(self,Player):
        self.user.append(Player)

    def users_clear(self):
        self.user=[]

    def users_check(self):
        print(f"Количество игроков {len(self.user)}")
        print([player.user_name for player in self.user])

    def users_card_view(self):
        print([player.user_card_view() for player in self.user])

    def check_X_user(self):
        for i in range(len(self.user)):
            if self.user[i].user_cards.count('X')==25:
                print(f"Победил пользователь {self.user[i].user_name}")
                self.game_succes=True




class user_game:
    def __init__(self):
        self.user_name='Anon'
        self.user_cards=self.user_genearator_card()

    def user_name_set(self,custom_name):
        self.user_name=custom_name

    def user_genearator_card(self):
        return [card for card in random.sample(range(1,91),25)]

    def user_card_view(self):
        print(f"Карты игрока: {self.user_name} \n{'\n'.join([f'{line}' for line in [self.user_cards[count*5:(count+1)*5] for count in range(5)]])}\n {'*'*15}")

    def user_close_card(self,number):
        try:
            index=self.user_cards.index(number)
            self.user_cards[index]='X'
        except:
            pass


def main():
    user_one = user_game()
    user_one.user_name_set('Pupa')

    user_two = user_game()
    user_two.user_name_set('Lupa')

    game=game_loto()
    game.user_add(user_one)
    game.user_add(user_two)
    game.users_check()
    #game.users_card_view()
    game.start()
main()
