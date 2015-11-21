from django.dispatch import Signal

mask_on = Signal(providing_args=['mask_username', 'request'])

mask_off = Signal(providing_args=['mask_username', 'request'])
