from Utils.EventTool import authorizer, get_event_data
from Utils.Validation import Validation
from Classes.Instructor import Instructor

val = Validation()
instructor = Instructor()


@authorizer
def register_instructor(event, context):

    data = get_event_data(event)

    print(data)

    list_validations = [
        val.param_data(data, "user_id", int)
    ]

    val.validate(list_validations)

    result = instructor.register_instructor(data)

    return result


@authorizer
def get_instructor(event, context):
    result = instructor.get_instructor()

    return result


@authorizer
def desactivate_instructor(event, context):

    data = get_event_data(event)
    list_validations = [
        val.param_data(data, "instructor_id", int),

    ]
    val.validate(list_validations)

    result = instructor.desactivate_instructor(data)

    return result


@authorizer
def get_fichas_asigned_instructor(event, context):

    data = get_event_data(event)

    list_validation = [
        val.param_data(data, "instructor_id", int),

    ]

    val.validate(list_validation)

    result = instructor.get_fichas_asigned_instructor(data)

    return result


@authorizer
def assign_ficha(event, context):

    data = get_event_data(event)

    list_validation = [
        val.param_data(data, "instructor_id", int),
        val.param_data(data, "ficha_id", int),

    ]

    val.validate(list_validation)

    result = instructor.assign_ficha(data)

    return result
