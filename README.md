# Equação de Laplace

    Nesse repositório, resolvemos a equação de laplace aplicando condições de contorno 
    sob duas circunferência que possui um corte de um arco por um certo ângulo que 
    pode ser escolhido de acordo com o usuario.

    Caso deseje utilizar outros números para fazer a simulação, basta muda-los
    no codigo eletric-potential.c, na parte de "Declarações e Constantes".

    Juntamente do projeto, há um relatório contendo toda a metodologia utilizada, além de uma
    discussão a respeito da utilizando de multithreading no programa.

------------------------------------------------------------------------------------------- %

# INSTRUÇÕES DE USO CONVENCIONAIS 

        Para compilar o programa, utilizamos o MAKEFILE, portanto basta 
        utilizar os seguintes comandos para compilar e rodar o programa:

        >> make
        >> time ./laplace.x

        Caso deseje rodar o programa com multithreading, deverá passar o número de threads
        que deseja utilizar juntamente do executavel do programa:

        >> time ./laplace.x 8                                                  (8 threads)

        O comando "time" irá captar o tempo de execução do programa.

------------------------------------------------------------------------------------------- %

    Caso deseje limpar os arquivos de output anteriores e rodar novamente
    basta utilizar o comando clean do makefile:

    >> make clean

------------------------------------------------------------------------------------------- %

    Nesse projeto temos duas versões do mesmo cálculo, uma utilizando o método de diferenças
    finitas de forma serial e inicial, resolvendo o problema de forma convencional. A outra 
    versão se trata do cálculo do mesmo problema utilizando multithreading, com os artifícios da API 
    OpenMP.

------------------------------------------------------------------------------------------- %
