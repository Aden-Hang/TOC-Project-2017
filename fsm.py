from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_hi(self, update):
        text = update.message.text
        return text.lower() == 'hi'

    def is_going_to_hello(self, update):
        text = update.message.text
        return text.lower() == 'hello'

    def is_going_to_goodmorning(self, update):
        text = update.message.text
        return text.lower() == 'goodmorning'

    def is_going_to_sleep(self, update):
        text = update.message.text
        return text.lower() == 'i am going to go to sleep'

    def is_going_to_no_plan(self, update):
        text = update.message.text
        return text.lower() == 'i have no plan'

    def is_going_to_study(self, update):
        text = update.message.text
        return text.lower() == 'i am going to study'

    def is_going_to_n_d(self, update):
        text = update.message.text
        return text.lower() == 'outside is raining, i prefer to stay inside'

    def is_going_to_n_o(self, update):
        text = update.message.text
        return text.lower() == 'ok, see you soon'

    def is_going_to_s_d(self, update):
        text = update.message.text
        return text.lower() == 'no, i do not like to read comic books'

    def is_going_to_s_o(self, update):
        text = update.message.text
        return text.lower() == 'good idea'

    def on_enter_hi(self, update):
        update.message.reply_text("Hi! What are the plans for today?")
        update.message.reply_photo(open("img/blackman_question_mark.jpg","rb"))
        self.go_plan(update)

    def on_exit_hi(self, update):
        print('Leaving hi')

    def on_enter_hello(self, update):
        update.message.reply_text("Hello! What are the plans for today?")
        update.message.reply_photo(open("img/blackman_question_mark.jpg","rb"))
        self.go_plan(update)

    def on_exit_hello(self, update):
        print('Leaving hello')

    def on_enter_goodmorning(self, update):
        update.message.reply_text("Goodmorning! What are the plans for today?")
        update.message.reply_photo(open("img/blackman_question_mark.jpg","rb"))
        self.go_plan(update)

    def on_exit_goodmorning(self, update):
        print('Leaving goodmorning')

    def on_enter_sleep(self, update):
        update.message.reply_text("Alright, goodbye")
        self.go_back(update)

    def on_exit_sleep(self, update):
        print('Leaving hi')

    def on_enter_no_plan(self, update):
        update.message.reply_text("How about go outside and have fun with friends?")

    def on_exit_no_plan(self, update):
        print('Leaving no_plan')

    def on_enter_study(self, update):
        update.message.reply_text("Are you kidding me!?")
        update.message.reply_text("There is no word call \"study\" in your dictionary><")
        update.message.reply_photo(open("img/laugh.jpg","rb"))
        update.message.reply_text("Do you want to get some comics for yourself?")

    def on_exit_study(self, update):
        print('Leaving study')

    def on_enter_n_d(self, update):
        update.message.reply_text("So, what do you want to do?")
        self.go_plan(update)

    def on_exit_n_d(self, update):
        print('Leaving n_d')

    def on_enter_n_o(self, update):
        update.message.reply_text("Have fun! See you soon~")
        self.go_back(update)

    def on_exit_n_o(self, update):
        print('Leaving n_o')

    def on_enter_s_d(self, update):
        update.message.reply_text("So, what do you want to do")
        self.go_plan(update)

    def on_exit_s_d(self, update):
        print('Leaving s_d')

    def on_enter_s_o(self, update):
        update.message.reply_text("You can get them on the third floor")
        self.go_back(update)

    def on_exit_s_o(self, update):
        print('Leaving s_o')
