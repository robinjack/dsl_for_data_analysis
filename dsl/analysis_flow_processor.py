from utils.const import CLASSNAMES
from dsl.function_table import FUNCTION_TABLE




def obj_processor(textX_object):
  '''
  Obj. processors can also introduce changes in the objects they process.
  Here we set "evaluate" function based on the object they refer to.
  '''
  textX_object.evaluate = FUNCTION_TABLE[textX_object._tx_fqn]


# Object processors are registered by defining a map between a rule name
# and the callable that will process the instances of that rule/class.
OBJ_PROCESSORS = {
    className: obj_processor for className in CLASSNAMES
    }

# This map/dict is registered on a meta-model by the "register_obj_processors"
# call.