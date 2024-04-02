from Classes.programs import Programs
from Utils.EventTool import authorizer, get_event_data
from Utils.Validation import Validation

programs = Programs()
val = Validation()


@authorizer
def register_program(event, context):
    data = get_event_data(event)

    list_validations = [
        val.param_data(data, "name_program", str)
    ]

    val.validate(list_validations)

    result = programs.register_program(data)

    return result


@authorizer
def get_programs(event, context):
    result = programs.get_programs()

    return result


@authorizer
def desactivate_program(event, context):

    data = get_event_data(event)
    list_validations = [
        val.param_data(data, "program_id", int)
    ]

    val.validate(list_validations)

    result = programs.desactivate_program(data)

    return result
