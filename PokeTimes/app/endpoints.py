from flask import Flask, request, jsonify
from app.data import Squad
import requests
import json

app = Flask(__name__)  # Cria uma instância da aplicação Flask

coaching_teams = {}  # Dicionário para armazenar os times

def retrieve_Pokemon_information(pokemon_name):
    # Função para obter dados de um Pokémon a partir do nome
    # Faz uma solicitação à pokeapi.co para obter os dados do Pokémon
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/"
    response = requests.get(url)  # Faz uma solicitação GET à API

    if response.status_code != 200:
        return None  # Pokemon não encontrado

    data = response.json()  # Converte a resposta em JSON
    pokemon_id = data.get("id")  # Obtém o ID do Pokémon
    height = data.get("height")  # Obtém a altura do Pokémon
    weight = data.get("weight")  # Obtém o peso do Pokémon

    return {
        "id": pokemon_id,
        "height": height,
        "weight": weight
    }

@app.route('/api/teams', methods=['GET'])
def retrieve_teams():
    # Rota para obter informações sobre todas as equipes
    fetch_teams = [team.to_dict() for team in coaching_teams.values()]  # Serializa todas as equipes em formato de lista
    return jsonify(fetch_teams)  # Converte a lista em uma resposta JSON

@app.route('/api/teams/<int:team_id>', methods=['GET'])
def retrieve_team(team_id):
    # Rota para obter informações sobre uma equipe específica com base em seu ID
    fetch_team = coaching_teams.get(team_id)  # Obtém a equipe com o ID fornecido
    if not fetch_team:
        return jsonify({"error": "Equipe nao encontrada, pesquise por outro id valido"}), 404  # Retorna um erro 404 se a equipe não existir
    return jsonify(fetch_team.to_dict())  # Converte a equipe em uma resposta JSON usando o método to_dict()

@app.route('/api/teams', methods=['POST'])
def generate_team():
    # Rota para criar uma nova equipe
    data = request.get_json()  # Obtém os dados da solicitação em formato JSON
    user = data.get('user')  # Obtém o nome do usuário da solicitação
    team_data = data.get('team')  # Obtém a lista de Pokémon da solicitação

    if not user or not team_data:
        return jsonify({"error": "Erro ao inserir informações, por favor insira informações validas"}), 400  # Retorna um erro 400 se a entrada for inválida

    # Verifica se o user já existe em algum time
    for team_id, existing_team in coaching_teams.items():
        if existing_team.owner == user:
            return jsonify({"error": f"O usuario {user} já existe para a equipe {team_id}"}), 400  # Retorna um erro se o usuário já existir

    pokemons = []
    for pokemon_name in team_data:
        # Valida e obtém os dados do Pokémon
        pokemon_data = retrieve_Pokemon_information(pokemon_name)

        if pokemon_data is None:
            return jsonify({"error": f"Pokemon {pokemon_name} Inexistente"}), 400  # Retorna um erro se o Pokémon não existir

        pokemons.append({
            "id": pokemon_data["id"],
            "name": pokemon_name,
            "weight": pokemon_data["weight"],
            "height": pokemon_data["height"]
        })

    new_team = Squad(owner=user, pokemons=pokemons)  # Cria uma nova equipe com os dados fornecidos
    team_id = len(coaching_teams) + 1  # Gera um novo ID para a equipe
    coaching_teams[team_id] = new_team  # Adiciona a nova equipe ao dicionário de equipes

    # Retorna uma mensagem personalizada ao usuário
    return jsonify({"message": f"Equipe criada com sucesso. Use a ID {team_id} para pesquisar"})

if __name__ == '__main__':
    app.run(debug=True)  # Inicia o servidor da aplicação Flask em modo de depuração se o script for executado como um programa independente
