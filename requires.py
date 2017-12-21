from charms.reactive import hook
from charms.reactive import RelationBase
from charms.reactive import scopes


class ConsulClient(RelationBase):
    scope = scopes.UNIT
    auto_accessors = ['address', 'port']

    @hook('{requires:consul}-relation-{joined,changed}')
    def changed(self):
        conv = self.conversation()

        conv.set_state('{relation_name}.connected')
        if conv.get_remote('port'):
            self.set_state('{relation_name}.available')

    @hook('{requires:consul}-relation-{broken,departed}')
    def broken(self):
        conv = self.conversation()
        conv.remove_state('{relation_name}.available')

    def list_unit_data(self):
        '''
        Iterate through all the consul conversations and return the data
        for each cached conversation. This allows us to build a cluster string
        directly from the relation data. eg:

        for unit in consul.list_unit_data():
            print(unit['port'])
        '''
        for conv in self.conversations():
            yield {'address': conv.get_remote('address'),
                   'port': conv.get_remote('port')}
