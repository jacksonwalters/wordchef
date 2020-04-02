from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Optional

class RecipeForm(FlaskForm):
	word1 = StringField('word1', render_kw={"placeholder": "flour"}, validators=[DataRequired(message="Where's the flour?")])
	amount1 = FloatField('amount1', render_kw={"placeholder": "1"}, validators=[Optional(),NumberRange(min=-100.0,max=100.0,message="That's a little spicy, pal.")])
	word2 = StringField('word2', render_kw={"placeholder": "egg"}, validators=[DataRequired(message="Put an egg in there.")])
	amount2 = FloatField('amount2', render_kw={"placeholder": "2.5"}, validators=[Optional(),NumberRange(min=-100.0,max=100.0,message="Easy with the olive oil, friend.")])
	submit = SubmitField('Cook!')
