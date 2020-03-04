from flask import Blueprint, render_template

from models.user import User


general_bp = Blueprint('general_bp', __name__, template_folder='templates')


@general_bp.route('/')
@general_bp.route('/user/<user_id>')
def index(user_id=None):
    user = User.query.filter(User.id == user_id).first()
    return render_template('general/index.html', user=user)
