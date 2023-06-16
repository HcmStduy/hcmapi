import uuid

from django.forms.widgets import Input,TextInput


class SendEmailButton(Input):
    input_type = 'text'
    template_name = "sent_email_widget.html"

    def __init__(self, attrs=None):
        if attrs is not None:
            attrs = attrs.copy()
            self.input_type = attrs.pop("type", self.input_type)
        super().__init__(attrs)

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context["widget"]["type"] = self.input_type
        return context


class IDwidget(TextInput):
    def get_context(self, name, value, attrs):
        #新增用户时
        if not value:
            value = uuid.uuid4().hex

        return super(IDwidget, self).get_context(name, value, attrs)

class ImgWidget(TextInput):
    template_name = ''