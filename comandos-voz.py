import pyttsx3, speech_recognition as sr

engine = pyttsx3.init()

voices = engine.getProperty("voices") 
engine.setProperty('voice', voices[0].id) #brasil
engine.setProperty('volume', 1)
engine.setProperty("rate", 155)

#Processa as modificações feitas até o momento
engine.runAndWait() 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Ouve o usuario.
def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n  Ouvindo...\n")
        speak('ouvindo')
        r.adjust_for_ambient_noise = 1.25
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("  Reconhecendo...\n")
        speak('Um momento, estou analisando sua solicitação.')
        query = r.recognize_google(audio, language='pt')
        #print(query)
    except:
        return "©empty_^_^_queryª"
    return query

speak("Olá. Meu nome é Sophie assistente virtual da ZeniTI, como posso te ajudar?")
if __name__ == "__main__":
    while True:

        print("opção: 1 Problema a ser resolvido ")
        print("opção: 2 Acionar um Alerta")
        print("opção: 3 Dicas para cuidar do meio ambiente")
        print("opção: 4 Sobre a empresa")
        print("Sair")
        speak('Escolha umas das opções acima:')


        query = command().lower()
        if '1' in query or 'um' in query:
            print("opção: 1 Problema a ser resolvido ")
            speak("você escolheu a opção numero 1")
            speak('Atualmente a poluição nas praias de São Paulo está aumentando drasticamente, ' +
             'principalmente depois de feriados e férias prolongadas. ' + 
             'Segundo Instituto Polis, em média, Caraguatatuba, Ilhabela, ' +
             'São Sebastião e Ubatuba gastam cerca de 10% do orçamento anual com lixo, ' +
             'uma porcentagem mais alta do que a da capital paulista, que é de 2%. ' +
             'Analisando esta situação, chegamos a conclusão que resolver esse problema '+
             'referente ao lixo nas praias poder trazer muitos benefícios para a sociedade como um todo.')

        elif '2' in query or 'dois' in query:
            print("opção: 2 Qual é o nosso objetivo")
            speak('você escolheu a opção numero 2')
            speak('De formar a resolver o problema apresentado, '+
            'temos como objetivo realizar a criação de um aplicativo mobile, ' + 
            'que terá como funcionalidade permitir que nossos usuários se informem ' + 
            'sobre a qualidade das praias do litoral paulista, e possam fazer denúncias ' + 
            'referentes a lixo e outros tipos de poluentes que estejam descartados nas mesmas, ' +
            'denúncias estas que serão atendidas por ONGs que também estarão cadastradas em nossa aplicação.')

        elif '3' in query  or 'três' in query:
            print("opção: 3 Dicas para cuidar do meio ambiente")
            speak("você escolheu a opção numero 3")
            speak("Faça uma lista de tudo que você está levando" + 
            " e certifique-se de trazer tudo de volta para casa," +
            " inclusive embalagens, sacos e garrafas plásticas." +
            " Tudo que é jogado na areia termina, invariavelmente," +  
            " no mar, e pode causar a morte de animais e sérios danos ao ecossistema marinho.")

        elif '4' in query  or 'quatro' in query:
            print("opção: 4 Sobre a empresa")
            speak("você escolheu a opção numero 4")
            speak("Nos somos a zeniTI e estamos juntos desde 2021 solucionando os problemas da vida real com o uso da tecnologia.")


            
        elif 'fim' in query or 'sair' in query : 
            print("Sair")
            speak("Ok, até mais!")
            break
  

        else:
            print("opção invalida")
            speak('não entendi o que você disse.')
            speak("Por favor, vamos tentar novamente. escolha uma opção válida.")
