# Atividade de Recuperação — Agenda 11 DSI
## Controle de Níveis de Água

**Aluno:** Matheus Leonardi  
**Curso:** Desenvolvimento de Sistemas  
**Turma:** ____________________  
**Data:** ____/____/________

## 1. Objetivo
Desenvolver uma simulação em Python para monitorar os níveis de água de um reservatório. O programa apresenta uma mensagem colorida no terminal para cada nível, facilitando a identificação da situação.

## 2. Recursos utilizados
- Lista: armazena os cinco níveis, suas situações e as cores.
- Função: `exibir_alerta(nivel)` identifica a mensagem e a cor do nível informado.
- Biblioteca Colorama: fornece as cores usadas nas mensagens do terminal.
- Estrutura de repetição: percorre os níveis simulados e exibe os alertas.

## 3. Funcionamento
O programa possui cinco níveis: muito baixo (crítico), baixo, médio, alto e muito alto (alerta). Cada nível recebe a cor solicitada no enunciado: vermelho, amarelo, verde, ciano e azul, respectivamente.

A função recebe o número do nível, procura esse nível na lista e exibe a situação com a cor correspondente. Caso o número não exista entre 1 e 5, o programa apresenta uma mensagem de nível inválido. O comando `Style.RESET_ALL` restaura o estilo padrão do terminal após a mensagem.

## 4. Testes realizados na simulação
A lista de simulação utiliza os níveis 1, 2, 3, 4 e 5. Dessa forma, é possível verificar a exibição de todas as situações previstas na atividade.

## 5. Conclusão
A atividade permitiu praticar listas, funções, repetição e utilização de biblioteca externa em Python. O uso de cores torna os alertas mais fáceis de identificar e a restauração do estilo evita que a cor de uma mensagem afete as seguintes.

## 6. Repositório GitHub
**Link do repositório:** inserir aqui o link do repositório criado no GitHub.
