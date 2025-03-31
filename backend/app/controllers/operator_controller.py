from flask import jsonify, request
from services.operator_service import OperatorService

operator_service = OperatorService()

def list_operators():
  results = operator_service.list_operators()
  if not results:
    return jsonify({"message": "Nenhum opereadora encontrada!"}), 404
  return jsonify(results)

def search_operators():
  search_term = request.args.get('q', '')
  if not search_term:
    return jsonify({"error": "O termo de pesquisa é obrigatório!"}), 400
  results = operator_service.search_operators(search_term)
  if not results:
    return jsonify({"message": "Nada consta com a busca!"}), 404
  return jsonify(results)