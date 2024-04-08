from Utils.Validation import Validation
from Utils.EventTool import lamda_response, get_event_data, authorizer
from Classes.Users import User

val = Validation()
user = User()


@authorizer
def create_new_user(event, context):

    data = get_event_data(event)

    list_validation = [
        val.param_data(data, "type_doc", int),
        val.param_data(data, "document", int),
        val.param_data(data, "first_name", str,),
        val.param_data(data, "last_name", str),
        val.param_data(data, "email", str),
        val.param_data(data, "number", int),
        val.param_data(data, "user_role_id", int),
        val.param_data(data, "user_name", str),
        val.param_data(data, "password", str)
    ]

    val.validate(list_validation)

    result = user.create_new_user(data)

    return result


@authorizer
def massive_user_insertion(event, context):
    data = get_event_data(event)

    list_validation = [
        val.param_data(data, "file_content_base64", str),]

    val.validate(list_validation)

    result = user.massive_user_insertion(data)

    return result


@lamda_response
def auth_user(event, context):

    data = get_event_data(event)

    list_validation = [
        val.param_data(data, "user_name", str),
        val.param_data(data, "password", str, True, 16, 8)
    ]

    val.validate(list_validation)

    result = user.auth_user(data)

    return result


@authorizer
def user_permission_assign(event, context):

    data = get_event_data(event)

    list_validation = [
        val.param_data(data, "user_id", int),
        val.param_data(data, "functions", list)
    ]

    val.validate(list_validation)

    result = user.user_permission_assign(data)

    return result


@authorizer
def desactivate_user(event, context):
    data = get_event_data(event)

    list_validations = [
        val.param_data(data, "user_name", str)
    ]

    val.validate(list_validations)

    result = user.desactivate_user(data)
    return result


@authorizer
def update_user(event, context):
    data = get_event_data(event)

    list_validations = [
        val.param_data(data, "user_name", str),
        val.param_data(data, "password", str)
    ]

    val.validate(list_validations)
    result = user.update_User(data)

    return result


@authorizer
def get_users(event, data):
    result = user.get_users()
    return result
