from Utils.Validation import Validation
from Utils.EventTool import authorizer, get_event_data
from Classes.UserRoles import UserRoles

val = Validation()
user_role = UserRoles()


@authorizer
def register_user_role(event, context):

    data = get_event_data(event)

    list_validation = [
        val.param_data(data, "role_name", str)
    ]

    val.validate(list_validation)

    result = user_role.register_user_role(data)

    return result


@authorizer
def get_user_roles(event, context):

    data = get_event_data(event)

    result = user_role.get_user_roles(data)

    return result


@authorizer
def update_user_role(event, context):

    data = get_event_data(event)

    list_validation = [
        val.param_data(data, "user_role_id", int),
        val.param_data(data, "role_name", str)
    ]

    val.validate(list_validation)

    result = user_role.update_user_role(data)

    return result


@authorizer
def desactivate_user_role(event, context):

    data = get_event_data(event)

    list_validation = [
        val.param_data(data, "user_role_id", int)
    ]

    val.validate(list_validation)

    result = user_role.desactivate_user_role(data)

    return result
