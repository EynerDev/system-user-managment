from Utils.EventTool import authorizer, get_event_data
from Utils.Validation import Validation
from Classes.Function import Function


val = Validation()
function = Function()


@authorizer
def register_function(event, context):

    data = get_event_data(event)

    print(data)

    list_validations = [
        val.param_data(data, "name", str),
        val.param_data(data, "function_path", str),
        val.param_data(data, "function_method", str)
    ]

    val.validate(list_validations)

    result = function.register_function(data)

    return result


@authorizer
def get_functions(event, context):
    result = function.get_functions()

    return result


@authorizer
def update_fucntions(event, context):

    data = get_event_data(event)
    list_validations = [
        val.param_data(data, "function_id", int),
        val.param_data(data, "name", str),
        val.param_data(data, "path", str),
        val.param_data(data, "method", str)
    ]
    val.validate(list_validations)

    result = function.update_function(data)

    return result


@authorizer
def desactivate_function(event, context):
    data = get_event_data(event)

    list_validations = [
        val.param_data(data, "function_id", int)
    ]

    val.validate(list_validations)

    result = function.desactivate_function(data)

    return result
