from django.forms import widgets
from django.utils.html import format_html
from django.forms.utils import flatatt


class GhCheckboxInput(widgets.CheckboxInput):
    template_wrapper = (
        '<div class="onoffswitch">'
        '{input}'
        '<label class="onoffswitch-label" for="{id}">'
        '<span class="onoffswitch-inner"></span>'
        '<span class="onoffswitch-switch"></span>'
        '</label>'
        '</div>'
    )
    def render(self, name, value, attrs=None):
        final_attrs = self.build_attrs(attrs, type='checkbox', name=name)
        if self.check_test(value):
            final_attrs['checked'] = 'checked'
        if not (value is True or value is False or value is None or value == ''):
            # Only add the 'value' attribute if a value is non-empty.
            final_attrs['value'] = force_text(value)
        if 'class' in final_attrs:
            final_attrs['class'] = ' '.join([final_attrs['class'], 'onoffswitch-checkbox'])
        else:
            final_attrs['class'] = 'onoffswitch-checkbox'

        return self.template_wrapper.format(input=format_html('<input{} />', flatatt(final_attrs)), id=final_attrs['id'])