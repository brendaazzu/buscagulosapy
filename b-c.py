def busca_gulosa_conversao(conversoes, taxas):
    melhor_opcao = min(conversoes, key=lambda moeda: conversoes[moeda] + taxas[f'taxa{moeda}'])
    moeda_barata = melhor_opcao
    taxa_barata = taxas[f'taxa{moeda_barata}']
    return moeda_barata, taxa_barata


conversoes = {
    'dolar': 4.98,
    'euro': 5.44,
    'libra': 6.33
}

taxas = {
    'taxadolar': ((5 * 4.98) / 100),
    'taxaeuro': ((10 * 5.44) / 100),
    'taxalibra': ((15 * 6.33) / 100),
}

moeda_barata, taxa_barata = busca_gulosa_conversao(conversoes, taxas)
melhor_opcao = (conversoes[moeda_barata] + taxas[f'taxa{moeda_barata}'])  
nome_melhor_opcao = moeda_barata.capitalize()  
print(f"A moeda mais barata é {moeda_barata}.")
print(f"A taxa mais barata é a taxa do {moeda_barata} com {taxa_barata:.2f} em relação ao real.")
print(f"A melhor opção é a moeda {nome_melhor_opcao}.")
