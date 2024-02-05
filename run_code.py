import functions as f

top = 30
# video_id = 'd0Y4J0Opkds'  # primer dia
# video_id = '7JVkPLLUtbU'  # segundo dia
# video_id = '6dZPSq5kxkU'  # tercer dia


# # De a 1 dia
# data = f.get_data(video_id)
# data = f.filterDataEsp(data)
# print(data)
# f.graf_1(data, top, 'Conteo Palabras Congreso Dia 1').show()
# f.graf_2(data)


# Los 3 videos juntos
primer_dia = f.get_data('d0Y4J0Opkds')
segundo_dia = f.get_data('7JVkPLLUtbU')
tercer_dia = f.get_data('6dZPSq5kxkU')

# concateno los 3 y sumo los duplicados
primer_dia = primer_dia.add(segundo_dia, fill_value=0)
primer_dia = primer_dia.add(tercer_dia, fill_value=0)

# filtro palabras comunes
primer_dia = f.filterDataEsp(primer_dia)
primer_dia.sort_values(by='count', ascending=False, inplace=True)  # ordeno por cantidad de palabras

# grafico
f.graf_1(primer_dia, 30, titulo='Conteo Palabras Congreso Total').show()
f.graf_2(primer_dia, 30, titulo='Congreso Total Cloud').show()

