Para criar um arquivo executavel (.exe) é só fazer os seguintes passos:
    . Crie uma pasta e insira o temporarizador.py nessa pasta.
    . Acesse esta pasta e na barra do caminho escreva CMD.
    . Com o pyinstaller já instalado você irá rodar o seguinte comando no CMD:
        - pyinstaller --onefile --windowed temporizador.py

Com esses passos feitos irá aparecer duas novas pastas dentro dessa pasta antes criada (build e dist).
O programa executavel estará dentro da pasta 'build'. Mova para onde desejar e pode apagar o restante.

OBS.: Esse passo a passo só será possivel se ja tiver com o python instalado na maquina e a biblioteca pyinstaller.
