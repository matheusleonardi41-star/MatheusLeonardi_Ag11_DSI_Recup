# Controle de Níveis de Água — DSI

## Objetivo
Simular o monitoramento do nível de água de um reservatório, exibindo uma mensagem colorida para cada situação.

## Tecnologias utilizadas
- Python 3
- Biblioteca `colorama`

## Níveis e cores
- Nível 1 — Muito baixo (crítico): vermelho
- Nível 2 — Baixo: amarelo
- Nível 3 — Médio: verde
- Nível 4 — Alto: ciano
- Nível 5 — Muito alto (alerta): azul

## Como o programa funciona
O programa armazena os cinco níveis em uma lista de dicionários. A função `exibir_alerta()` recebe um nível, localiza sua situação e imprime a mensagem com a cor correspondente. Ao final da mensagem, `Style.RESET_ALL` restaura o estilo padrão do terminal.

A lista `niveis_simulados` contém os valores usados na demonstração. Não é necessário digitar informações durante a execução.

## Como executar
1. Instale Python 3, caso ainda não esteja instalado.
2. No terminal, instale a dependência:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute:
   ```bash
   python main.py
   ```

## Estrutura do projeto
- `main.py`: código principal.
- `requirements.txt`: biblioteca necessária para executar o programa.
- `README.md`: explicação do projeto.
