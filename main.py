from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json, glob
from datetime import datetime
from pathlib import Path
import random
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior


from matplotlib.style import available

Builder.load_file("design.kv")

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current="sign_up_screen"

    def login(self, uname, pword):
        with open("users.json") as file:
            users= json.load(file)
        if uname in users and users[uname]['password'] == pword:
            self.manager.current="login_screen_success"
        else:
            self.ids.wrong_details.text="Wrong credentials, please try again!"    

class SignUpScreen(Screen):
    def add_user(self, uname, pword):
        with open("users.json") as file:
            users= json.load(file)
        users[uname]={'username': uname, 'password': pword,
        'created': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        with open("users.json",'w') as file:
            json.dump(users, file)
        self.manager.current="sign_up_screen_success"    

class SignUpScreenSuccess(Screen):
    def login(self):
        self.manager.transition.direction='right'
        self.manager.current="login_screen"   

class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction='right'       
        self.manager.current="login_screen" 

    def get_quote(self, feel):     
        feel=feel.lower()
        available_feel=glob.glob("quotes/*")
        available_feel=[Path(filename).stem for filename in available_feel]
        
        quotes={}
        if feel in available_feel:
            if feel=="happy":
                quotes_happy=["“Happiness is when what you think, what you say, and what you do are in harmony.” - Mahatma Gandhi",
    "“Happiness is not something ready made. It comes from your own actions.” - Dalai Lama",
    "“If more of us valued food and cheer and song above hoarded gold, it would be a merrier world.” - J.R.R. Tolkien",
    "“The Way Get Started Is To Quit Talking And Begin Doing.” – Walt Disney",
    "“People Who Are Crazy Enough To Think They Can Change The World, Are The Ones Who Do.” – Rob Siltanen",
    "“It's a beautiful day. Give yourself a treatment. Go out. Taste a cup of tea or a coffee. Enjoy the monent!” - Unknown",
    "“Develop An ‘Attitude Of Gratitude’. Say Thank You To Everyone You Meet For Everything They Do For You.” – Brian Tracy"]
            
                self.ids.quote.text= random.choice(quotes_happy)

            if feel=="sad":
                quotes_sad=["“Some days are just bad days, that's all. You have to experience sadness to know happiness, and I remind myself that not every day is going to be a good day, that's just the way it is!” - Dita Von Teese",
    "“Life is 10% what happens to you and 90% how you react to it.” - Charles R. Swindoll",
    "“It’s Not Whether You Get Knocked Down, It’s Whether You Get Up.” – Vince Lombardi ",
    "“Failure Will Never Overtake Me If My Determination To Succeed Is Strong Enough.” – Og Mandino",
    "“In the egoic state, your sense of self, your identity, is derived from your thinking mind - in other words, what your mind tells you about yourself: the storyline of you, the memories, the expectations, all the thoughts that go through your head continuously and the emotions that reflect those thoughts. All those things make up your sense of self.” - Eckhart Tolle",
    "“Wherever you are, be there totally. If you find your here and now intolerable and it makes you unhappy, you have three options: remove yourself from the situation, change it, or accept it totally. If you want to take responsibility for your life, you must choose one of those three options, and you must choose now. Then accept the consequences.” - Eckhart Tolle",
    "“Narrow your life down to this moment. Your life situation may be full of problems - most life situations are - but find out if you have a problem at this moment. Do you have a problem now?” - Eckhart Tolle"]
                self.ids.quote.text= random.choice(quotes_sad)

            if feel=="unloved":
                quotes_unloved=["“Sometimes we find ourselves feeling unwanted or unloved. Remember you were born of love, you are love, it exists inside you, that's where it begins. When you know this you will have a happier life.” - Angel Karan",
    "“Don’t Let Yesterday Take Up Too Much Of Today.” - Will Rogers",
    "“The Man Who Has Confidence In Himself Gains The Confidence Of Others.” – Hasidic Proverb",
    "“Love is a state of Being. Your love is not outside; it is deep within you. You can never lose it, and it cannot leave you. It is not dependent on some other body, some external form.” - Eckhart Tolle",
    "“In the stillness of your presence, you can feel your own formless and timeless reality as the unmanifested life that animates your physical form. You can then feel the same life deep within every other human and every other creature. You look beyond the veil of form and separation. This is the realization of oneness. This is love.” - Eckhart Tolle",
    "“The weak can never forgive. Forgiveness is the attribute of the strong.” - Eckhart Tolle",
    "“You must not lose faith in humanity. Humanity is an ocean; if a few drops of the ocean are dirty, the ocean does not become dirty.” - Mahatma Gandhi"]    
                self.ids.quote.text= random.choice(quotes_unloved)

        else:
            self.ids.quote.text="Please try another feeling!"

            #name=f"quotes/{feel}.txt"
           # with open(name) as file:
           #     quotes=file.readlines()
           # self.ids.quote.text= random.choice(quotes)
        #else:
        #    self.ids.quote.text="Please try another feeling!"  

class ImageButton(ButtonBehavior, HoverBehavior, Image):
    pass            

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()



#Shift-Alt-F to format json file 