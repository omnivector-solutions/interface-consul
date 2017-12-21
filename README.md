# Consul interface

This interface has been designed as a drop in interface for clients wishing to
connect to the existing consul-charm in the juju charm store.


## States

### {relation-name}.connected
 When this state is raised, the unit has connected but might not have transmitted
 the information we need in order to complete our connection. Defer until 'available'
 has been raised.

### {relation-name}.available
This state is set when the unit has presented all the required information:

 - Address
 - Port

 Example Code:

 ```python
@when('consul.available')
def configure_consul(consul):
    connection_string = "consul://"
    for unit in consul.list_unit_data():
      host_string = "{}:{}".format(unit['address'], unit['port'])
      connection_string = "{}{},".format(connection_string, host_string)
    start_my_app(connection_string.rstrip(','))
 ```

# maintainers

- Charles Butler <charles.butler@canonical.com>
- Matt Bruzek <matt.bruzek@canonical.com>
