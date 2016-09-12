def laspeyre(somatorioMesAnterior, somatorioMesAtual, pesoAtual, pesoAnterior):
    return somatorioMesAnterior*(pesoAtual*(somatorioMesAtual/somatorioMesAnterior))/(somatorioMesAnterior*pesoAnterior)