from flask import Blueprint, request, jsonify
from services import calculate_metrics

metric_routes = Blueprint('metrics', __name__, url_prefix='/api/v1')
    
@metric_routes.route('/metrics', methods=['POST'])
def calc():
    data = request.get_json()
    history = data['data']
    results = calculate_metrics.main(history,initial_investment=8000)

    response = jsonify({
        "message":"Calculation successful",
        "results": results
    })
    return response, 200