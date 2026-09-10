from flask import Blueprint, jsonify


health_bp = Blueprint('health', __name__)


@health_bp.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'version': '0.4.0'
    })