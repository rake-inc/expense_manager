from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Expense
		fields = ['category','price','description','user_id']