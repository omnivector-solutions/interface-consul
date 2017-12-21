from charms.reactive import hook
from charms.reactive import RelationBase
from charmhelpers.core.hookenv import unit_private_ip


class ConsulClient(RelationBase):

    @hook('{provides:consul}-relation-{joined,changed}')
    def changed(self):
        conv = self.conversation()
        conv.set_state('{relation_name}.connected')

    @hook('{provides:consul}-relation-{broken,departed}')
    def broken(self):
        conv = self.conversation()
        conv.remove_state('{relation_name}.connected')

    def provide_data(self, port):
        ''' Consumers will invoke this method to ship the extant unit the port
            and address.
        '''
        for conv in self.conversations():
            self.set_remote(scope=conv.scope, data={'port': port,
                                                    'address': unit_private_ip()})  # noqa
