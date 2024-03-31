from Classes.programs import 
from Utils.EventTool import authorizer, get_event_data
from Utils.Validation import Validation

fichas = P()
val = Validation()


@authorizer
def register_ficha(event, context):
    data = get_event_data(event)

    list_validations = [
        val.param_data(data, "program_id", int),
        val.param_data(data, "number_ficha", int),
        val.param_data(data, "alias", str),
        val.param_data(data, "status_id", int)
    ]

    val.validate(list_validations)

    result = fichas.register_ficha(data)

    return result


@authorizer
def get_fichas(event, context):
    result = fichas.get_fichas()

    return result