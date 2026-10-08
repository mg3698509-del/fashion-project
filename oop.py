import tkinter as tk

from tkinter import ttk

from abc import ABC, abstractmethod

class Person:

    def __init__(self, name, age):

        self._name = name

        self._age = age

    def get_name(self):

        return self._name

    def get_age(self):

        return self._age

    def set_name(self, name):

        self._name = name

    def set_age(self, age):

        self._age = age

class User(Person):

    def __init__(self, name, age, style, color, budget):

        super().__init__(name, age)

        self._style = style

        self._color = color

        self._budget = budget

    def get_style(self):

        return self._style

    def get_color(self):

        return self._color

    def get_budget(self):

        return self._budget

    def set_style(self, style):

        self._style = style

    def set_color(self, color):

        self._color = color

    def set_budget(self, budget):

        self._budget = budget

class FashionItem(ABC):

    def __init__(self, name, category, price):

        self._name = name

        self._category = category

        self._price = price

    def get_name(self):

        return self._name

    def get_category(self):

        return self._category

    def get_price(self):

        return self._price

    @abstractmethod

    def get_description(self):

        pass

class Outfit(FashionItem):

    def get_description(self):

        return "Outfit: " + self._name + " " + str(self._price) + " EGP"

class Shoes(FashionItem):

    def get_description(self):

        return "Shoes: " + self._name + " " + str(self._price) + " EGP"

class Bag(FashionItem):

    def get_description(self):

        return "Bag: " + self._name + " " + str(self._price) + " EGP"

class Hairstyle(FashionItem):

    def get_description(self):

        return "Hairstyle: " + self._name + " " + str(self._price) + " EGP"

class Nails(FashionItem):

    def get_description(self):

        return "Nails: " + self._name + " " + str(self._price) + " EGP"

class Accessories(FashionItem):

    def get_description(self):

        return "Accessories: " + self._name + " " + str(self._price) + " EGP"

class Makeup(FashionItem):

    def get_description(self):

        return "Makeup: " + self._name + " " + str(self._price) + " EGP"


class Look:
    def __init__(self, occasion, weather, style, color, items):

        self._occasion = occasion

        self._weather = weather

        self._style = style

        self._color = color

        self._items = items

        self._rating = 0

    def get_occasion(self):

        return self._occasion

    def get_weather(self):

        return self._weather

    def get_style(self):

        return self._style

    def get_color(self):

        return self._color

    def get_items(self):

        return self._items

    def get_total_price(self):

        total = 0

        for item in self._items:

            total += item.get_price()

        return total

    def set_rating(self, rating):

        self._rating = rating

    def get_rating(self):

        return self._rating

class Recommendation:

    def get_top_rated(self, looks):

        if not looks:

            return []

        ratings = []

        for look in looks:

            ratings.append(look.get_rating())

        highest = max(ratings)

        top = []

        for look in looks:

            if look.get_rating() == highest:

                top.append(look)

        return top

    def search_looks(self, looks, search_text):

        results = []

        for look in looks:

            if search_text.lower() in look.get_occasion().lower():

                results.append(look)

        return results

recommendation = Recommendation()

user1 = User(

    "Marina",

    18,

    "Elegant",

    "Black",

    3000

)

outfit1 = Outfit(

    "Elegant Maxi Dress",

    "Outfit",

    1500

)

shoes1 = Shoes(

    "High Heels",

    "Shoes",

    600

)

bag1 = Bag(

    "Crystal Clutch",

    "Bag",

    300

)

hairstyle1 = Hairstyle(

    "Soft Waves",

    "Hairstyle",

    100

)

nails1 = Nails(

    "French Nails",

    "Nails",

    150

)

accessories1 = Accessories(

    "Crystal Earrings",

    "Accessories",

    200

)

makeup1 = Makeup(

    "Soft Glam Makeup",

    "Makeup",

    250

)

items1 = [

    outfit1,

    makeup1,

    nails1,

    shoes1,

    bag1,

    hairstyle1,

    accessories1

]

look1 = Look(

    "Wedding",

    "Hot",

    "Elegant",

    "Black",

    items1

)

outfit2 = Outfit(

    "Party Dress",

    "Outfit",

    900

)

shoes2 = Shoes(

    "Cute Heels",

    "Shoes",

    400

)

bag2 = Bag(

    "Mini Bag",

    "Bag",

    250

)

hairstyle2 = Hairstyle(

    "High Ponytail",

    "Hairstyle",

    80

)

nails2 = Nails(

    "Pastel Nails",

    "Nails",

    100

)

accessories2 = Accessories(

    "Heart Earrings",

    "Accessories",

    120

)

makeup2 = Makeup(

    "Pink Makeup",

    "Makeup",

    180

)

items2 = [

    outfit2,

    makeup2,

    nails2,

    shoes2,

    bag2,

    hairstyle2,

    accessories2

]

look2 = Look(

    "Birthday",

    "Mild",

    "Girly",

    "Pink",

    items2

)

outfit3 = Outfit(

    "Smart Casual Set",

    "Outfit",

    700

)

shoes3 = Shoes(

    "White Sneakers",

    "Shoes",

    450

)

bag3 = Bag(

    "Tote Bag",

    "Bag",

    250

)

hairstyle3 = Hairstyle(

    "Straight Hair",

    "Hairstyle",

    70

)

nails3 = Nails(

    "Natural Nails",

    "Nails",

    50

)

accessories3 = Accessories(

    "Simple Bracelet",

    "Accessories",

    80

)

makeup3 = Makeup(

    "Natural Makeup",

    "Makeup",

    100

)

items3 = [

    outfit3,

    makeup3,

    nails3,

    shoes3,

    bag3,

    hairstyle3,

    accessories3

]

look3 = Look(

    "University",

    "Hot",

    "Casual",

    "White",

    items3

)

outfit4 = Outfit(

    "Elegant Midi Dress",

    "Outfit",

    1000

)

shoes4 = Shoes(

    "Heeled Sandals",

    "Shoes",

    500

)

bag4 = Bag(

    "Shoulder Bag",

    "Bag",

    300

)

hairstyle4 = Hairstyle(

    "Soft Curls",

    "Hairstyle",

    100

)

nails4 = Nails(

    "Nude Nails",

    "Nails",

    100

)

accessories4 = Accessories(

    "Gold Necklace",

    "Accessories",

    180

)

makeup4 = Makeup(

    "Classic Makeup",

    "Makeup",

    200

)

items4 = [

    outfit4,

    makeup4,

    nails4,

    shoes4,

    bag4,

    hairstyle4,

    accessories4

]

look4 = Look(

    "Dinner",

    "Mild",

    "Elegant",

    "Red",

    items4

)

looks = [

    look1,

    look2,

    look3,

    look4

]

user1.get_name()

user1.get_age()

outfit1.get_description()

shoes1.get_description()

bag1.get_description()

hairstyle1.get_description()

nails1.get_description()

accessories1.get_description()

makeup1.get_description()

outfit2.get_description()

shoes2.get_description()

bag2.get_description()

hairstyle2.get_description()

nails2.get_description()

accessories2.get_description()

makeup2.get_description()

outfit3.get_description()

shoes3.get_description()

bag3.get_description()

hairstyle3.get_description()

nails3.get_description()

accessories3.get_description()

makeup3.get_description()

outfit4.get_description()

shoes4.get_description()

bag4.get_description()

hairstyle4.get_description()

nails4.get_description()

accessories4.get_description()

makeup4.get_description()

look1.get_occasion()

look1.get_weather()

look1.get_style()

look1.get_color()

look1.get_items()

look1.get_total_price()

look1.get_rating()

look2.get_occasion()

look2.get_weather()

look2.get_style()

look2.get_color()

look2.get_items()

look2.get_total_price()

look2.get_rating()

look3.get_occasion()

look3.get_weather()

look3.get_style()

look3.get_color()

look3.get_items()

look3.get_total_price()

look3.get_rating()

look4.get_occasion()

look4.get_weather()

look4.get_style()

look4.get_color()

look4.get_items()

look4.get_total_price()

look4.get_rating()

recommendation.get_top_rated(looks)

recommendation.search_looks(looks, "Wedding")

window = tk.Tk()

window.title("StyleMe")

window.geometry("650x650")

window.configure(bg="#FFF5F7")

bg = "#FFF5F7"

pink = "#E8A0BF"

dark = "#C75B86"

def clear():

    for x in window.winfo_children():

        x.destroy()

def home():

    clear()

    tk.Label(

        window,

        text="✨ StyleMe ✨",

        font=("Arial", 28, "bold"),

        bg=bg,

        fg=dark

    ).pack(pady=25)

    tk.Label(

        window,

        text="Your Personal Fashion & Beauty Advisor",

        font=("Arial", 11),

        bg=bg

    ).pack(pady=5)

    tk.Button(

        window,

        text="👤 Create User",

        command=create_user,

        width=25,

        height=2,

        bg=pink

    ).pack(pady=5)

    tk.Button(

        window,

        text="👗 Create My Look",

        command=create,

        width=25,

        height=2,

        bg=pink

    ).pack(pady=5)

    tk.Button(

        window,

        text="➕ Add Look",

        command=create,

        width=25,

        height=2,

        bg=pink

    ).pack(pady=5)

    tk.Button(

        window,

        text="👀 View Looks",

        command=view_looks,

        width=25,

        height=2,

        bg=pink

    ).pack(pady=5)

    tk.Button(

        window,

        text="🔍 Search Looks",

        command=search_looks,

        width=25,

        height=2,

        bg=pink

    ).pack(pady=5)

    tk.Button(

        window,

        text="⭐ Rate Look",

        command=rate_page,

        width=25,

        height=2,

        bg=pink

    ).pack(pady=5)

    tk.Button(

        window,

        text="🏆 Top Rated Looks",

        command=top_rated,

        width=25,

        height=2,

        bg=pink

    ).pack(pady=5)

    tk.Button(

        window,

        text="🚪 Exit",

        command=window.destroy,

        width=25,

        height=2

    ).pack(pady=10)

def create_user():

    clear()

    tk.Label(

        window,

        text="👤 Create User",

        font=("Arial", 22, "bold"),

        bg=bg,

        fg=dark

    ).pack(pady=25)

    tk.Label(

        window,

        text="Name",

        bg=bg

    ).pack()

    name_entry = tk.Entry(

        window,

        width=25

    )

    name_entry.pack(pady=5)

    tk.Label(

        window,

        text="Age",

        bg=bg

    ).pack()

    age_entry = tk.Entry(

        window,

        width=25

    )

    age_entry.pack(pady=5)

    def save_user():

        user1.set_name(name_entry.get())

        user1.set_age(int(age_entry.get()))

        create()

    tk.Button(

        window,

        text="Save User",

        command=save_user,

        width=20,

        bg=pink

    ).pack(pady=15)

    tk.Button(

        window,

        text="Back",

        command=home,

        width=20

    ).pack()

def create():

    clear()

    tk.Label(

        window,

        text="✨ Create Your Look ✨",

        font=("Arial", 22, "bold"),

        bg=bg,

        fg=dark

    ).pack(pady=15)

    global occasion

    global weather

    global style

    global color

    global budget

    data = [

        ("Occasion", ["Wedding", "Birthday", "University", "Dinner"]),

        ("Weather", ["Hot", "Cold", "Mild", "Rainy"]),

        ("Style", ["Elegant", "Glam", "Casual", "Girly"]),

        ("Color", ["Black", "White", "Pink", "Red", "Blue"])

    ]

    boxes = {}

    for name, values in data:

        tk.Label(

            window,

            text=name,

            bg=bg

        ).pack()

        box = ttk.Combobox(

            window,

            values=values,

            state="readonly",

            width=20

        )

        box.set(values[0])

        box.pack(pady=2)

        boxes[name] = box

    occasion = boxes["Occasion"]

    weather = boxes["Weather"]

    style = boxes["Style"]

    color = boxes["Color"]

    tk.Label(

        window,

        text="Budget",

        bg=bg

    ).pack(pady=(5, 0))

    budget = tk.Entry(

        window,

        width=22

    )

    budget.pack(pady=3)

    tk.Button(

        window,

        text="✨ Get My Look",

        command=generate,

        width=20,

        bg=pink

    ).pack(pady=10)

    tk.Button(

        window,

        text="Back",

        command=home,

        width=20

    ).pack()

def generate():

    user1.set_style(style.get())

    user1.set_color(color.get())

    budget_text = budget.get().strip()

    if budget_text == "":

        user1.set_budget(0)

    else:

        user1.set_budget(float(budget_text))

    selected_look = look1

    if occasion.get() == "Birthday":

        selected_look = look2

    elif occasion.get() == "University":

        selected_look = look3

    elif occasion.get() == "Dinner":

        selected_look = look4

    show_result(

        selected_look,

        user1.get_budget()

    )

def show_result(look, user_budget):

    clear()

    tk.Label(

        window,

        text="✨ Your Perfect Look ✨",

        font=("Arial", 22, "bold"),

        bg=bg,

        fg=dark

    ).pack(pady=12)

    for item in look.get_items():

        tk.Label(

            window,

            text=f"{item.get_category()}: "

                 f"{item.get_name()} - "

                 f"{item.get_price()} EGP",

            bg=bg

        ).pack(pady=2)

    total = look.get_total_price()

    tk.Label(

        window,

        text=f"Total Price: {total} EGP",

        font=("Arial", 14, "bold"),

        bg=bg,

        fg=dark

    ).pack(pady=8)

    if total <= user_budget:

        text = "✓ Within your budget"

    else:

        text = "✗ Over your budget"

    tk.Label(

        window,

        text=text,

        bg=bg

    ).pack()

    tk.Label(

        window,

        text="Rate this Look:",

        font=("Arial", 12, "bold"),

        bg=bg

    ).pack(pady=8)

    for value in range(1, 6):

        tk.Button(

            window,

            text=f"⭐ {value}",

            command=lambda x=value: rate(look, x),

            width=8,

            bg=pink

        ).pack(side="left", padx=4)

    tk.Button(

        window,

        text="Back to Home",

        command=home,

        width=20

    ).pack(pady=25)

def rate(look, value):

    look.set_rating(value)

    home()

def rate_page():

    clear()

    tk.Label(

        window,

        text="⭐ Rate Latest Look",

        font=("Arial", 22, "bold"),

        bg=bg,

        fg=dark

    ).pack(pady=30)

    if not looks:

        tk.Label(

            window,

            text="No looks available.",

            bg=bg

        ).pack(pady=10)

    else:

        for value in range(1, 6):

            tk.Button(

                window,

                text=f"⭐ {value}",

                command=lambda x=value: rate(looks[-1], x),

                width=12,

                bg=pink

            ).pack(pady=3)

    tk.Button(

        window,

        text="Back",

        command=home,

        width=20

    ).pack(pady=15)

def view_looks():

    clear()

    tk.Label(

        window,

        text="👀 All Looks",

        font=("Arial", 22, "bold"),

        bg=bg,

        fg=dark

    ).pack(pady=20)

    if not looks:

        tk.Label(

            window,

            text="No looks yet.",

            bg=bg

        ).pack()

    else:

        for look in looks:

            text = (

                f"{look.get_occasion()} | "

                f"{look.get_style()} | "

                f"{look.get_color()} | "

                f"⭐ {look.get_rating()}/5 | "

                f"{look.get_total_price()} EGP"

            )

            tk.Label(

                window,

                text=text,

                bg=bg

            ).pack(pady=5)

    tk.Button(

        window,

        text="Back",

        command=home,

        width=20

    ).pack(pady=20)

def search_looks():

    clear()

    tk.Label(

        window,

        text="🔍 Search Looks",

        font=("Arial", 22, "bold"),

        bg=bg,

        fg=dark

    ).pack(pady=25)

    tk.Label(

        window,

        text="Search by Occasion",

        bg=bg

    ).pack()

    search_entry = tk.Entry(

        window,

        width=25

    )

    search_entry.pack(pady=8)

    def search():

        results = recommendation.search_looks(

            looks,

            search_entry.get()

        )

        for x in window.winfo_children():

            if isinstance(x, tk.Label):

                if x not in [title_label]:

                    x.destroy()

        if not results:

            tk.Label(

                window,

                text="No looks found.",

                bg=bg

            ).pack(pady=10)

        else:

            for look in results:

                tk.Label(

                    window,

                    text=f"{look.get_occasion()} | "

                         f"{look.get_style()} | "

                         f"⭐ {look.get_rating()}/5",

                    bg=bg

                ).pack(pady=5)

    title_label = window.winfo_children()[0]

    tk.Button(

        window,

        text="Search",

        command=search,

        width=20,

        bg=pink

    ).pack(pady=8)

    tk.Button(

        window,

        text="Back",

        command=home,

        width=20

    ).pack(pady=15)

def top_rated():

    clear()

    tk.Label(

        window,

        text="🏆 Top Rated Looks",

        font=("Arial", 22, "bold"),

        bg=bg,

        fg=dark

    ).pack(pady=25)

    top = recommendation.get_top_rated(looks)

    if not top:

        tk.Label(

            window,

            text="No rated looks yet.",

            bg=bg

        ).pack()

    else:

        for look in top:

            tk.Label(

                window,

                text=f"🏆 {look.get_occasion()} "

                     f"⭐ {look.get_rating()}/5",

                bg=bg

            ).pack(pady=5)

    tk.Button(

        window,

        text="Back",

        command=home,

        width=20

    ).pack(pady=20)

home()

window.mainloop()