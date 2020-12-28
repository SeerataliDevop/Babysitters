from django.contrib import admin

from Babysitters.models import Available, AvailableMultan, AvailableIslamabad, AvailableGujranwala, AvailableKarachi, \
    AvailableSialkot, AvailablePeshawar, AvailableGujrat

admin.site.register(Available)
admin.site.register(AvailableMultan)
admin.site.register(AvailableIslamabad)
admin.site.register(AvailableGujranwala)
admin.site.register(AvailableKarachi)
admin.site.register(AvailableSialkot)
admin.site.register(AvailablePeshawar)
admin.site.register(AvailableGujrat)




admin.site.site_header='Blooming Buds'