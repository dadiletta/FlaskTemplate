from flask_mail import Mail
from flask_moment import Moment
from flask_wtf.csrf import CSRFProtect
 
mail = Mail()
moment = Moment()
csrf = CSRFProtect()