import akinator

aki = akinator.Akinator()

try:
    q = aki.start_game("pl")
except (akinator.AkiServerDown, akinator.AkiTechnicalError):
    try:
        q = aki.start_game("en2")
    except (akinator.AkiServerDown, akinator.AkiTechnicalError):
        q = aki.start_game("en3")

while aki.progression <= 100:
    a = input(q + "\n\t")
    if a == "b":
        try:
            q = aki.back()
        except akinator.CantGoBackAnyFurther:
            pass
    else:
        q = aki.answer(a)
        print(aki.progression)
aki.win()

correct = input(f"It's {aki.name} ({aki.description})! Was I correct?\n{aki.picture}\n\t")
if correct.lower() == "yes" or correct.lower() == "y":
    print("Yay\n")
else:
    print("Oof\n")
