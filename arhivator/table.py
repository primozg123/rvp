from arhivator.models import Person
from table import Table
from table.columns import Column

class OsebaTable(Table):
    id = Column(field='id')
    ime = Column(field='ime')
    class Meta:
        model = Oseba
