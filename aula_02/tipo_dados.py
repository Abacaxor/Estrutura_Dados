# Modulo de Tipagem
produto = input('Nome do componente: ')
preco_base = float(input('Preco de custo: '))
quantidade = int(input('Quantidade em estoque: '))
disponivel = quantidade > 0

valor_total = preco_base * quantidade

print(f'Item: {produto} | Tipo: {type(produto)}')
print(f'Total em Estoque: R${valor_total:.2f} | Disponivel: {disponivel}')
