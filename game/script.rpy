init python:
    comemoration = False
    whichOne = False
    whatTheyWanted = False
    talkAboutGoodThings = False

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define srBelmond = Character("", kind=bubble, image="sylvie")
define noOne = Character("")
define samuel = Character("Samuel")
define oliverHarte = Character("Oliver Harte")
define mike = Character("Mike")
define newspaperDelivery = Character("Entregador de Jornal")

# The game starts here.
label start:
    play sound "background-music.mp3" loop
    label prologue:
        scene black_background
        with fade
        show text "{size=75}{color=#ffffff}Prólogo{/size}" at truecenter
        with dissolve
        pause 2.0
        hide text
        with dissolve

    label scenario1:
        #show eileen happy
        # {size=50} {b} {color=#ffffff} {space=75} {fast} {p} 
        scene story board_01 with fade
        # srBelmond "{font=Not-my-Type.otf}teste de fonte: ã,õ,á,é,ó,í,â,ô,ç{/font}"
        show text "Cidade de Helden" at top with dissolve
        pause 1.5
        hide text with dissolve
        srBelmond "Essa cidade já foi um lugar bom para morar, saudades daquela época..."
        samuel "Senhor Belmond... Oliver Harte deixou uma entrega destinada ao senhor, Gostaria que deixasse na sua mesa?"
        # hide sylvie green surprised

        srBelmond "Deixe e saia."

        srBelmond "Esse detetive zomba de mim, mandou esse fotografo me entregar o serviço."
        srBelmond "Imprestável."

        scene story board_01-02 with fade
        noOne "Eu costumava ser feliz com minha família... e agora tenho que lidar com esses políticos e gangsters de merda..."
        noOne "Só espero estar errado."
        
        srBelmond "Traidora!{w=0.5}!{w=0.5}!{w=0.8} A{w=0.05}q{w=0.05}u{w=0.05}e{w=0.05}l{w=0.05}a {w=0.05}v{w=0.05}a{w=0.05}d{w=0.05}i{w=0.05}a{w=0.05} {w=0.05}v{w=0.05}a{w=0.05}i {w=0.05}m{w=0.05}e {w=0.05}p{w=0.05}a{w=0.05}g{w=0.05}a{w=0.05}r {w=0.05}p{w=0.05}o{w=0.05}r {w=0.05}i{w=0.05}s{w=0.05}s{w=0.05}o{w=0.05}."

    label scenario2:
        scene story board_02 with fade
        oliverHarte "Boa noite meu querido Mike."

        scene story board_03 with fade
        mike "Se fosse querido teria me pago suas dividas, detetive."
        mike "O que vai querer?"
        oliverHarte "O de sempre, e adicione um pouco de animo na sua cara."

        scene story board_04 with fade
        pause 2.0
        
        scene story board_05 with fade
        
        menu:
            "Vamos comemorar hoje.":
                $comemoration = True
            "Muito movimento hoje?":
                $comemoration = False
        
        if comemoration == True:
            mike "Comemoraremos o quê mesmo?"
        else:
            mike "Nem tanto, os malditos Marlones vieram aqui mais cedo."
            menu:
                "Qual deles?":
                    $whichOne = True
                    mike "O mais novo, acho que seu nome é Raul."
                    oliverHarte "Oquê eles queriam?"
                    mike "Comprar o Bar, Aparentemente eles estão interessados por ser um local bem localizado."
                    oliverHarte "Ignore eles, vamos falar de coisa boa."
                "Oquê eles queriam?":
                    $whatTheyWanted = True
                    mike "Comprar o Bar, Aparentemente eles estão interessados por ser um local bem localizado."
                    oliverHarte "Ignore eles, vamos falar de coisa boa."
                "Ignore eles, vamos falar de coisa boa.":
                    $talkAboutGoodThings = True

        oliverHarte "Resolvi mais um caso, e vou receber uma grana preta amanhã. Vamos sair essa noite."

        mike "Sair? Você sabe que sou casado, e se não voltar para casa na hora, apareço no Eco na seção de homicídios."

        oliverHarte "Falando em Eco, descobri que a mulher do Belmond estava saindo com o Terry."

        mike "O açougueiro? Com aquele Terry?"

        oliverHarte "Uhum, um maldito açougueiro."

        oliverHarte "Uma pena que você não vir, mas vou indo nessa fica com o troco."

    label scenario3:
        scene story board_06 with fade
        oliverHarte "Um merecido descanso para um bom cidadão..."
        oliverHarte "Nada mais que o merecido... Afinal de contas."

        oliverHarte "Não é todo dia que descobrimos que a maior figura da cidade é o maior corno também."
        oliverHarte "Sinto muito Sr Belmond mas a infidelidade de sua esposa é minha alegria."

        oliverHarte "Cadê o dinheiro que estava aqui ?... Bolso de merda continue me dando dinheiro."
        oliverHarte "Tem muito dinheiro aqui."
        oliverHarte "Ninguém vai se importar se eu..."

    label scenario4:
        scene story board_07 with fade
        oliverHarte "{w=0.3}.{w=1}.{w=1}.{w=0.3}"

        scene story board_08 with fade
        oliverHarte "{w=0.3}.{w=1}.{w=1}.{w=0.3}"
        oliverHarte "Maldito seja quem quer que tenha ligado a luz?"
        oliverHarte "Ah, é você sol! A quanto tempo."
        oliverHarte "Que dor, minha cabeça está querendo cair do lugar."
        oliverHarte "Tentarei me livrar dela assim que encontrar qualquer um que pareça precisar de um cérebro novo."
        oliverHarte "E claro, se aceita-lo de ressaca."

        scene story board_09 with fade
        oliverHarte "Que bagunça é essa?"
        oliverHarte "Pessoas sendo pessoas, o que diabos estão tentando pegar ali."
        oliverHarte "Parece papel, deve ser o “Eco” de hoje."
        oliverHarte "Tão cedo,... Aliás, que horas são?"
        oliverHarte "Preciso comer."
        oliverHarte "Cadê todo meu dinheiro... FUI ROUBADO!!! Ou será que não?"
        oliverHarte "Não me lembro, mas esse bolso deveria estar cheio de dinheiro, meu aluguel iria ser pago com ele."
        oliverHarte "Passarei no jornal para pegar o restante e poder voltar para casa sem aquele senhorio idiota para me encher."

    label scenario5:
        scene story board_10 with fade
        newspaperDelivery "Extra!!!! Belmond Preso..."
        oliverHarte "Como é senhores... Me de isso aqui..."
        oliverHarte "Gordo idiota, se te pego quem vai para manchete sou eu."
    
    label scenario6:
        scene story board_11 with fade

return
# This ends the game.
