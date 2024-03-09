from Classes.FunctionGroup import FunctionGroup
from Utils.EventTool import authorizer, get_event_data
from Utils.Validation import Validation

val = Validation()
functionGroup = FunctionGroup()


@authorizer
def register_group_function(event, context):
    data = get_event_data(event)

    list_validations = [
        val.param_data(data, "name", str)
    ]

    val.validate(list_validations)

    result = functionGroup.register_function_group(data)

    return result


@authorizer
def get_function_group(event, context):

    result = functionGroup.get_function_group()

    return result


@authorizer
def update_function_group(event, context):

    data = get_event_data(event)

    list_validations = [
        val.param_data(data, "function_group_id")
    ]

    val.validate(list_validations)

    result = functionGroup.update_function_group(data)

    return result


@authorizer
def desactivate_function_group(event, context):

    data = get_event_data(event)

    list_validations = [
        val.param_data(data, "function_group_id")
    ]

    val.validate(list_validations)

    result = functionGroup.desactivate_function_group(data)

    return result


@authorizer
def register_function_relation(event, context):

    data = get_event_data(event)

    list_validations = [
        val.param_data(data, "function_group_id", int),
        val.param_data(data, "functions", list),
    ]

    val.validate(list_validations)

    result = functionGroup.register_function_relation(data)

    return result


@authorizer
def get_function_relation(event, context):

    data = get_event_data(event)

    list_validations = [
        val.param_data(data, "function_group_id", int),
        val.param_data(data, "functions", list, False),
    ]

    val.validate(list_validations)

    result = function_group.get_function_relation(data)

    return result


@authorizer
def insert_function_group_auth(event, context):

    data = get_event_data(event)

    list_validations = [
        val.param_data(data, "function_group_id", int),
        val.param_data(data, "user_roles", list)
    ]

    val.validate(list_validations)

    result = function_group.insert_function_group_auth(data)

    return result

