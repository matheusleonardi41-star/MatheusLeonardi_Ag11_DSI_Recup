from colorama import init, Fore, Style

# Inicializa o Colorama para exibir cores no terminal.
init(autoreset=True)

# Lista com as situações possíveis do reservatório, do nível mais baixo ao mais alto.
niveis_agua = [
    {"nivel": 1, "situacao": "Muito baixo (crítico)", "cor": Fore.RED},
    {"nivel": 2, "situacao": "Baixo", "cor": Fore.YELLOW},
    {"nivel": 3, "situacao": "Médio", "cor": Fore.GREEN},
    {"nivel": 4, "situacao": "Alto", "cor": Fore.CYAN},
    {"nivel": 5, "situacao": "Muito alto (alerta)", "cor": Fore.BLUE},
]


def exibir_alerta(nivel):
    """Exibe a situação do reservatório com a cor correspondente ao nível."""
    for item in niveis_agua:
        if item["nivel"] == nivel:
            print(
                item["cor"]
                + f"Nível {item['nivel']}: {item['situacao']}"
                + Style.RESET_ALL
            )
            return

    print(Fore.WHITE + f"Nível {nivel} inválido. Informe um nível de 1 a 5." + Style.RESET_ALL)


# Simulação: níveis registrados no reservatório.
niveis_simulados = [1, 2, 3, 4, 5]

print("=== MONITORAMENTO DO RESERVATÓRIO DE ÁGUA ===")
for nivel_atual in niveis_simulados:
    exibir_alerta(nivel_atual)
