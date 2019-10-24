from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'username')


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        # 원래 field값에 email도 추가해주자.
        fields = UserCreationForm.Meta.fields + ('email',)