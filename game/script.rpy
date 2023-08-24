# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define srBelmond = Character("sr. Belmond")
define samuel = Character("Samuel")
define oliverHarte = Character("Oliver Harte")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # 1st Board
    # 1st Scene
    srBelmond "Essa cidade já foi um lugar bom para morar, saudades daquela época..."

    samuel "Senhor Belmond... Oliver Harte deixou uma entrega destinada ao senhor, Gostaria que deixasse na sua mesa?"

    srBelmond "Deixe e saia."

    # 2nd Scene
    srBelmond "Esse detetive zomba de mim, mandou esse fotografo me entregar o serviço."
    srBelmond "Imprestável."

    # 3rd Scene
    srBelmond "Eu costumava ser feliz com minha família... e agora tenho que lidar com esses políticos e gangsters de merda..."
    srBelmond "Só espero estar errado."
    srBelmond "Traidora!!!! Aquela vadia vai me pagar por isso."

    # 3rd Board
    # 1st Scene
    oliverHarte "Um merecido descanso para um bom cidadão..."
    oliverHarte "Nada mais que o merecido... Afinal de contas."

    # 2nd Scene
    oliverHarte "Não é todo dia que descobrimos que a maior figura da cidade é o maior corno também."
    oliverHarte "Sinto muito Sr Belmond mas a infidelidade de sua esposa é minha alegria."
    
    # 3rd Scene
    oliverHarte "Cadê o dinheiro que estava aqui ?... Bolso de merda continue me dando dinheiro."
    oliverHarte "Tem muito dinheiro aqui."
    oliverHarte "Ninguém vai se importar se eu..."

    # This ends the game.

    return
