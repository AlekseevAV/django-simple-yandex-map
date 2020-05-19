from .fields import YmapCoord
from .widgets import YmapCoordFieldWidget


class YmapAdmin(object):
    def formfield_for_dbfield(self, db_field, **kwargs):
        if isinstance(db_field, YmapCoord):
            kwargs['widget'] = YmapCoordFieldWidget

        field = super(YmapAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        return field
