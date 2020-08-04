from utils.const import CLASSNAMES
from dsl.function_table import FUNCTION_TABLE


def self_map(self):
    return self


def obj_processor(textX_object):
    '''
      Obj. processors can also introduce changes in the objects they process.
    Here we set "evaluate" function based on the object they refer to.
    '''
    if hasattr(textX_object, '_tx_fqn'):
        textX_object.evaluate = FUNCTION_TABLE.get(textX_object._tx_fqn, self_map)

    return textX_object


# Object processors are registered by defining a map between a rule name
# and the callable that will process the instances of that rule/class.
OBJ_PROCESSORS = {
    className: obj_processor for className in CLASSNAMES
    }

# This map/dict is registered on a meta-model by the "register_obj_processors"
# call.