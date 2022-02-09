-------------------------------------------------------------------------------------------- %

                                ------- HPC 1 --------

    Nesse repositório, resolvemos a equação de laplace aplicando condições de contorno 
    sob duas circunferência que possui um corte de um arco por um certo ângulo que 
    pode ser escolhido de acordo com o usuario.

    Caso deseje utilizar outros números para fazer a simulação, basta muda-los
    no codigo eletric-potential.c, na parte de "Declarações e Constantes".

------------------------------------------------------------------------------------------- %

    ! INSTRUÇÕES DE USO CONVENCIONAIS !

        Para compilar o programa, utilizamos o MAKEFILE, portanto basta 
        utilizar os seguintes comandos para compilar e rodar o programa:

        >> make
        >> time ./laplace.x

        O comando "time" irá captar o tempo de execução do programa.

    ! INSTRUÇÕES DE USO EXCEPCIONAIS !

        Caso disponha das bibliotecas numpy, matplotlib e pandas em seu computador,
        poderá rodar o programa e plotar a saída de dados, resultando em uma figura PNG. 
        Nesse caso, basta utilizar os comandos:

        >> make
        >> chmod +x script.sh
        >> time ./script.sh

------------------------------------------------------------------------------------------- %

    Caso deseje limpar os arquivos de output anteriores e rodar novamente
    basta utilizar o comando clean do makefile:

    >> make clean

------------------------------------------------------------------------------------------- %

    Nesse projeto temos duas versões do mesmo cálculo, uma utilizando o método de diferenças
    finitas de forma serial, resolvendo o problema de forma convencional. A outra versão se
    trata do cálculo do mesmo problema utilizando multithreading, com os artifícios da API 
    OpenMP.

------------------------------------------------------------------------------------------- %