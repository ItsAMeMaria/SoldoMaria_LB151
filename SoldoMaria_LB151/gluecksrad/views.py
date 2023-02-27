from django.shortcuts import redirect, render, get_object_or_404
from .models import Player, Word, Category
import random
# Create your views here.
def index(request):
    return render(request, "index.html")

def game(request):
    return render(request, "game.html")

def admin(request):
    return render(request, "admin.html")

def add_player(request):
    if request.method == 'POST':
        name = request.POST['name']
        player = Player.objects.create(name=name)
        player.save()
        print(f"Created a new player with name {name}")
        return redirect("game")
    else:
        return render(request, "index.html")

def random_word(request):
    word = random.choice(Word.objects.all()).word.upper()
    letters = list(word)
    request.session['word'] = letters
    request.session['letters'] = ['_' if letter != ' ' else ' ' for letter in letters]
    request.session['guessed_letters'] = []
    return render(request, 'game.html', {'letters': request.session['letters']})

def play_game(request):
    if request.method == "POST":
        guess = request.POST.get('letter')
        letters = request.session.get('letters', [])
        if guess and guess not in letters:
            word = request.session.get('word')
            if guess in word:
                for i, letter in enumerate(word):
                    if letter == guess:
                        letters[i] = guess
                request.session['letters'] = letters
                guessed_letters = [letter if letter in letters else " " for letter in word]
                return render(request, "game.html", {'letters': letters, 'guessed_letters': guessed_letters, 'message': 'Correct guess!'})
            else:
                request.session['letters'] = letters
                guessed_letters = [letter if letter in letters else " " for letter in word]
                return render(request, "game.html", {'letters': letters, 'guessed_letters': guessed_letters, 'message': 'Wrong guess!'})
        else:
            guessed_letters = [letter if letter in letters else " " for letter in word]
            return render(request, "game.html", {'letters': letters, 'guessed_letters': guessed_letters, 'message': 'Please enter a valid letter!'})
    else:
        return redirect('random_word')


