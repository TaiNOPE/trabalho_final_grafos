// Classe para representar um vértice
class Vertice {
    constructor(id) {
      this.id = id; // Identificador do vértice
      this.adjacentes = []; // Lista de vértices adjacentes
      this.distancia = Infinity; // Distância inicialmente definida como infinito
      this.anterior = null; // Vértice anterior no caminho mais curto
    }
  
    // Método para adicionar um vértice adjacente juntamente com o peso da aresta
    adicionarAdjacente(vertice, peso) {
      this.adjacentes.push({ vertice, peso });
    }
  }
  
  // Função para encontrar o menor caminho usando o algoritmo de Dijkstra
  function dijkstra(grafo, idVerticeInicio, idVerticeFim) {
    const verticeInicio = grafo[idVerticeInicio]; // Vértice inicial
    const verticeFim = grafo[idVerticeFim]; // Vértice final
  
    // Define a distância do vértice inicial como 0
    verticeInicio.distancia = 0;
  
    const verticesNaoVisitados = new Set(Object.keys(grafo)); // Conjunto de vértices não visitados
  
    while (verticesNaoVisitados.size > 0) {
      // Encontra o vértice com a menor distância entre os não visitados
      let idVerticeAtual = null;
      let menorDistancia = Infinity;
  
      for (const idVertice of verticesNaoVisitados) {
        const vertice = grafo[idVertice];
        if (vertice.distancia < menorDistancia) {
          menorDistancia = vertice.distancia;
          idVerticeAtual = idVertice;
        }
      }
  
      if (idVerticeAtual === null) {
        break;
      }
  
      const verticeAtual = grafo[idVerticeAtual];
      verticesNaoVisitados.delete(idVerticeAtual);
  
      // Atualiza as distâncias dos vértices adjacentes
      for (const { vertice, peso } of verticeAtual.adjacentes) {
        const distancia = verticeAtual.distancia + peso;
  
        if (distancia < vertice.distancia) {
          vertice.distancia = distancia;
          vertice.anterior = verticeAtual;
        }
      }
    }
  
    // Constrói o caminho a partir do vértice final
    const caminho = [];
    let verticeAtual = verticeFim;
    let distanciaTotal = 0;
  
    while (verticeAtual !== null) {
      caminho.unshift(verticeAtual);
      if (verticeAtual.anterior) {
        const { vertice, peso } = verticeAtual.anterior.adjacentes.find(adj => adj.vertice === verticeAtual);
        distanciaTotal += peso;
      }
      verticeAtual = verticeAtual.anterior;
    }
  
    return { caminho, distanciaTotal };
  }
  
  // Criação do grafo
  const grafo = {};
  
  // Função para adicionar arestas ao grafo
  function adicionarAresta(origem, destino, peso) {
    if (!grafo[origem]) {
      grafo[origem] = new Vertice(origem);
    }
  
    if (!grafo[destino]) {
      grafo[destino] = new Vertice(destino);
    }
  
    grafo[origem].adicionarAdjacente(grafo[destino], peso);
  }
  
  // Adiciona as arestas ao grafo
  adicionarAresta(1, 2, 0.85);
  adicionarAresta(1, 4, 0.7);
  adicionarAresta(1, 7, 3.25);
  adicionarAresta(2, 3, 1.4);
  adicionarAresta(3, 5, 0.68);
  adicionarAresta(4, 5, 1.5);
  adicionarAresta(4, 8, 0.9);
  adicionarAresta(5, 6, 1.95);
  adicionarAresta(6, 12, 1.65);
  adicionarAresta(7, 8, 0.6);
  adicionarAresta(8, 9, 1.1);
  adicionarAresta(9, 10, 0.9);
  adicionarAresta(10, 11, 0.38);
  adicionarAresta(11, 12, 0.68);
  adicionarAresta(12, 13, 0.68);
  adicionarAresta(13, 14, 0.55);
  
  // Executa o algoritmo de Dijkstra para encontrar o menor caminho entre dois vértices
  const idVerticeInicio = 1;
  const idVerticeFim = 14;
  const { caminho, distanciaTotal } = dijkstra(grafo, idVerticeInicio, idVerticeFim);
  
  // Exibe o caminho encontrado
  if (caminho.length > 0) {
    const idsCaminho = caminho.map(vertice => vertice.id).join(' -> ');
    console.log(`O menor caminho de ${idVerticeInicio} a ${idVerticeFim} é: ${idsCaminho}`);
    console.log(`Distância total do caminho: ${distanciaTotal.toFixed(2)}`);
  } else {
    console.log(`Não há caminho possível entre ${idVerticeInicio} e ${idVerticeFim}`);
  }
  