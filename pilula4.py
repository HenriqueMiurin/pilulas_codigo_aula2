import statistics as st 
lote1= float(input('Produção do lotre 1:'))
lote2= float(input('Produção do lotre 2:'))
lote3= float(input('Produção do lotre 3:'))

media = st.mean ((lote1,lote2,lote3))
desvio =  st.stdev(((lote1,lote2,lote3)))

print(f'Média {media:.2f}')
print(f"Desvio padrâo {desvio:.2f}")