country = {
    "Acre":                 { "adjacency": ["Amazonas", "Rondônia"], "color": None },
    "Amazonas":             { "adjacency": ["Acre", "Roraima", "Pará", "Mato Grosso", "Rondônia"], "color": None },
    "Roraima":              { "adjacency": ["Amazonas", "Pará"], "color": None },
    "Pará":                 { "adjacency": ["Amazonas", "Roraima", "Amapá", "Maranhão", "Tocantins", "Mato Grosso"], "color": None },
    "Amapá":                { "adjacency": ["Pará"], "color": None },
    "Rondônia":             { "adjacency": ["Acre", "Amazonas", "Mato Grosso"], "color": None },
    "Mato Grosso":          { "adjacency": ["Rondônia", "Amazonas", "Pará", "Tocantins", "Goiás", "Mato Grosso do Sul"], "color": None },
    "Maranhão":             { "adjacency": ["Pará", "Piauí", "Tocantins"], "color": None },
    "Tocantins":            { "adjacency": ["Mato Grosso", "Pará", "Maranhão", "Bahia", "Goiás"], "color": None },
    "Goiás":                { "adjacency": ["Mato Grosso do Sul","Mato Grosso", "Tocantins", "Bahia", "Minas Gerais"], "color": None },
    "Mato Grosso do Sul":   { "adjacency": ["Mato Grosso", "Goiás", "Minas Gerais", "São Paulo", "Paraná"], "color": None },
    "Paraná":               { "adjacency": ["Mato Grosso do Sul", "São Paulo", "Santa Catarina"], "color": None },
    "Santa Catarina":       { "adjacency": ["Paraná", "Rio Grande do Sul"], "color": None },
    "Rio Grande do Sul":    { "adjacency": ["Santa Catarina"], "color": None },
    "São Paulo":            { "adjacency": ["Paraná", "Mato Grosso do Sul", "Minas Gerais", "Rio de Janeiro"], "color": None },
    "Minas Gerais":         { "adjacency": ["São Paulo", "Mato Grosso do Sul", "Goiás", "Bahia", "Espírito Santo", "Rio de Janeiro"], "color": None },
    "Rio de Janeiro":       { "adjacency": ["São Paulo", "Minas Gerais", "Espírito Santo"], "color": None },
    "Espírito Santo":       { "adjacency": ["Minas Gerais", "Rio de Janeiro", "Bahia"], "color": None },
    "Bahia":                { "adjacency": ["Espírito Santo", "Minas Gerais", "Goiás", "Tocantins", "Piauí","Pernambuco", "Alagoas", "Sergipe"], "color": None },
    "Piauí":                { "adjacency": ["Bahia", "Maranhão", "Ceará", "Pernambuco"], "color": None },
    "Ceará":                { "adjacency": ["Piauí", "Pernambuco", "Paraíba", "Rio Grande do Norte"], "color": None },
    "Rio Grande do Norte":  { "adjacency": ["Ceará", "Paraíba"], "color": None },
    "Paraíba":              { "adjacency": ["Rio Grande do Norte", "Ceará", "Pernambuco"], "color": None },
    "Pernambuco":           { "adjacency": ["Paraíba", "Ceará", "Piauí", "Bahia", "Alagoas"], "color": None },
    "Alagoas":              { "adjacency": ["Pernambuco", "Bahia", "Sergipe"], "color": None },
    "Sergipe":              { "adjacency": ["Alagoas", "Bahia"], "color": None },
}


# retorna True se for um grafo não direcionado.
def isGraphUndirected():
    for state in country:
        for adj in country[state]["adjacency"]:
            if(state not in country[adj]["adjacency"]):
                return False
    return True;


# retorna o nome do estado com mais estados adjacentes com cor.
def getHighestColoredAdjState():
    highestAdjCount = -1;
    highestAdjState = None;

    for state in country:
        if(country[state]["color"] != None):
            continue;
        coloredCount = 0;
        for adj in country[state]["adjacency"]:
            if(country[adj]["color"] != None):
                coloredCount += 1;
        
        if coloredCount > highestAdjCount:
            highestAdjState = state;
            highestAdjCount = coloredCount;
    return(highestAdjState)


# Pega a cor atribuída aos estados, agrupando estados com a mesma cor.
def getCountryColorDict():
    colorDict = {};
    for state in country:
        color = country[state]["color"];
        if color not in colorDict:
            colorDict.update({color: []})
        colorDict[color].append(state);

    return colorDict;


# Atribui um cor para cada estado, utilizando o teorema das 4 cores.BaseException
def fourColorTheorem():
    while True:
        st = getHighestColoredAdjState();
        if st == None:
            break;

        # pega a lista de cores de cada vértice adjacente
        adjColors = list();
        for adj in country[st]["adjacency"]:
            color = country[adj]["color"];
            if(color != None):
                adjColors.append(color);

        # escolhe uma nova cor
        newColor = None;
        if len(adjColors) != 0:
            # caso adjColors for, por exemplo {1, 2, 4},
            # newColor será 3.
            for i in range(len(adjColors) + 1):
                if(i not in adjColors):
                    newColor = i;
                    break;
        else:
            newColor = 1;

        country[st]["color"] = newColor;



# main
# Verifica se o gráfico é aceitavel.
if not isGraphUndirected():
    print("Grafo inválido");
    exit(0);

# Calcula a cor para cada estado.
fourColorTheorem();

# Mostra os resultados.
colorDict = getCountryColorDict();
for color in colorDict:
    print(f"Cor {color}:")
    for state in colorDict[color]:
        print(f"\t{state}");
