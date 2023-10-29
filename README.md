# PokeTimes - API Pokémon
Bem-vindo à documentação da API Pokémon, uma ferramenta que permite criar e listar equipes de Pokémons. 
Aqui você encontrará informações sobre como configurar o projeto com Docker, usar a API localmente e no Docker Compose, além de detalhes sobre cada rota com exemplos.

## Configuração com Docker
Caso você não tenha o Docker instalado, siga as instruções em Docker Installation Guide para instalar a plataforma em seu sistema.

### Configuração com Docker Compose
1. Clone o repositório do projeto:

git clone https://github.com/EstudanteWS/PokeTimes.git
cd PokeTimes

Dentro do diretório do projeto, execute o seguinte comando para iniciar a aplicação com Docker Compose:

docker-compose up

Isso iniciará a API, que estará disponível em http://localhost:5000.

#### Uso Local
#### Para utilizar a API localmente, siga estas etapas:

2. Clone o repositório do projeto:

git clone https://github.com/EstudanteWS/PokeTimes.git
cd PokeTimes

Inicie a aplicação localmente utilizando o docker:

docker build -t pokemon-python . (para criar imagem do dockerfile)

docker run -it -p 5000:5000 pokemon-python (para rodar conteiner da imagem do dockerfile na porta 5000:5000)

python main.py

A API estará disponível em http://localhost:5000.

#### Rotas da API
#### Para testar esta API, recomendamos o uso da ferramenta Postman.

Aqui estão alguns exemplos de uso das rotas da API:

#### Listar Todas as Equipes (GET /api/teams)
Descrição: Retorna uma lista de todas as equipes registradas.

Exemplo de Requisição:

GET http://localhost:5000/api/teams

Exemplo de Resposta:

[
	{
		"owner": "sleao",
		"pokemons": [
			{
				"height": 16,
				"id": 9,
				"name": "blastoise",
				"weight": 855
			},
			{
				"height": 4,
				"id": 25,
				"name": "pikachu",
				"weight": 60
			},
			{
				"height": 17,
				"id": 6,
				"name": "charizard",
				"weight": 905
			},
			{
				"height": 20,
				"id": 3,
				"name": "venusaur",
				"weight": 1000
			},
			{
				"height": 25,
				"id": 131,
				"name": "lapras",
				"weight": 2200
			},
			{
				"height": 17,
				"id": 6,
				"name": "charizard",
				"weight": 905
			}
		]
	},
	{
		"owner": "maka",
		"pokemons": [
			{
				"height": 16,
				"id": 9,
				"name": "blastoise",
				"weight": 855
			},
			{
				"height": 4,
				"id": 25,
				"name": "pikachu",
				"weight": 60
			},
			{
				"height": 17,
				"id": 6,
				"name": "charizard",
				"weight": 905
			}
		]
	}
]

#### Buscar Equipe por ID (GET /api/teams/{id})
Descrição: Retorna uma equipe registrada com base em sua ID única.

Exemplo de Requisição:

GET http://localhost:5000/api/teams/1

Exemplo de Resposta em caso id esteja correto:

{
	"owner": "sleao",
	"pokemons": [
		{
			"height": 16,
			"id": 9,
			"name": "blastoise",
			"weight": 855
		},
		{
			"height": 4,
			"id": 25,
			"name": "pikachu",
			"weight": 60
		},
		{
			"height": 17,
			"id": 6,
			"name": "charizard",
			"weight": 905
		},
		{
			"height": 20,
			"id": 3,
			"name": "venusaur",
			"weight": 1000
		},
		{
			"height": 25,
			"id": 131,
			"name": "lapras",
			"weight": 2200
		},
		{
			"height": 17,
			"id": 6,
			"name": "charizard",
			"weight": 905
		}
	]
}

Caso Id seja inserido incorretamente: 
{
	"error": "Equipe nao encontrada, pesquise por outro id valido"
	}

#### Criar Equipe (POST /api/teams)
Descrição: Crie uma nova equipe com base em uma lista de Pokémons e um nome de usuário.

Exemplo de Requisição:

POST http://localhost:5000/api/teams '{
  "user": "sleao",
  "team": ["blastoise", "pikachu", "charizard", "venusaur", "lapras", "charizard"]
}' 

Exemplo de Resposta caso seja inserida informações invalidas:

{
	"error": "Erro ao inserir informações, por favor insira informações validas"
	}

Exemplo de resposta caso usuario ja esteja em outro time:

{
	"error": f"O usuario {user} já existe para a equipe {team_id}"
	}

Exemplo de resposta caso os dados do pokemon seja inserido de forma invalido:

{
	"error": f"Pokemon {pokemon_name} Inexistente"
	}

Exemplo de Resposta caso seja inserido usuario e id pela primeira vez:

{
	"message": "Equipe criada com sucesso. Use a ID 1 para pesquisar."
}

Esta API foi criada para o desafio de infraestrutura da Triágil.