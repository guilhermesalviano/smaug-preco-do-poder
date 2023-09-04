# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define srBelmond = Character("", kind=bubble, image="sylvie")
define samuel = Character("Samuel")
define oliverHarte = Character("Oliver Harte")
define newspaperDelivery = Character("Entregador de Jornal")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # 1st Board
    # 1st Scene
    # show sylvie green surprised
    scene story board_01
    with fade
    srBelmond "Essa cidade já foi um lugar bom para morar, saudades daquela época..."
    samuel "Senhor Belmond... Oliver Harte deixou uma entrega destinada ao senhor, Gostaria que deixasse na sua mesa?"
    # hide sylvie green surprised

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
    scene story board_03
    with fade
    oliverHarte "Um merecido descanso para um bom cidadão..."
    oliverHarte "Nada mais que o merecido... Afinal de contas."

    # 2nd Scene
    oliverHarte "Não é todo dia que descobrimos que a maior figura da cidade é o maior corno também."
    oliverHarte "Sinto muito Sr Belmond mas a infidelidade de sua esposa é minha alegria."
    
    # 3rd Scene
    oliverHarte "Cadê o dinheiro que estava aqui ?... Bolso de merda continue me dando dinheiro."
    oliverHarte "Tem muito dinheiro aqui."
    oliverHarte "Ninguém vai se importar se eu..."

    # 4rd Board
    # 1st Scene
    scene story board_04
    with fade
    oliverHarte "(........................)"
    oliverHarte "(........................)"
    oliverHarte "Maldito seja quem quer que tenha ligado a luz?"

    # 2nd Scene
    oliverHarte "Ah, é você sol! A quanto tempo."
    oliverHarte "Que dor, minha cabeça está querendo cair do lugar."
    oliverHarte "Tentarei me livrar dela assim que encontrar qualquer um que pareça precisar de um cérebro novo."
    oliverHarte "E claro, se aceita-lo de ressaca."

    # 3rd Scene
    oliverHarte "Que bagunça é essa?"
    oliverHarte "Pessoas sendo pessoas, o que diabos estão tentando pegar ali."
    oliverHarte "Parece papel, deve ser o “Eco” de hoje."
    oliverHarte "Tão cedo,... Aliás, que horas são?"
    oliverHarte "Preciso comer."
    oliverHarte "Cadê todo meu dinheiro... FUI ROUBADO!!! Ou será que não?"
    oliverHarte "Não me lembro, mas esse bolso deveria estar cheio de dinheiro, meu aluguel iria ser pago com ele."
    oliverHarte "Passarei no jornal para pegar o restante e poder voltar para casa sem aquele senhorio idiota para me encher."

    # 4rd Scene
    newspaperDelivery "Extra!!!! Belmond Preso..."
    oliverHarte "Como é senhores... Me de isso aqui..."
    oliverHarte "Gordo idiota, se te pego quem vai para manchete sou eu."

    # This ends the game.

    return
