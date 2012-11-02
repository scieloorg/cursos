=====================
Lista de exercícios 1
=====================


1. Para que servem as *funções* em Python?

#. Por que utilizaríamos *testes automatizados*? Cite as
   principais bibliotecas de testes automatizados disponíveis em Python.

#. Há um *bug* na função *autores_doctest.py*[1]_ quando tentamos normalizar
   nomes de autores com mais de 2 partes. Exemplo: **'Stevie Ray Vaughan'** é
   normalizado para **'VAUGHAN, Ray, Stevie'**, quando deveria ser
   **'VAUGHAN, Stevie Ray'**. Corrija este bug.

#. Implemente uma função que imprime **apenas as vogais** de uma *string*
   passada como argumento.

   Exemplo::

       >>> vogais('pirulito')
       i
       u
       i
       o

#. Implemente uma função que recebe uma *string* no formato *csv*
   como argumento e produz a saída conforme o exemplo abaixo::

       >>> csv_para_humanos('Gustavo Fonseca,Engenheiro de Software,28')
       Nome: Gustavo Fonseca
       Atividade: Engenheiro de Software
       Idade: 28


.. [1] http://git.io/dBUqag
