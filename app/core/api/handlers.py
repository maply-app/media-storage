from core.api.base import APIResponse
from core.api.errors import Errors


async def handle_custom_error(request, response, exception, params, ws=None):
    await APIResponse.Error(exception).response(response)


async def handle_custom_404_error(request, response, exception, params, ws=None):
    await APIResponse.Error(Errors.RouteNotFound).response(response)


async def handle_custom_500_error(request, response, exception, params, ws=None):
    await APIResponse.Error(Errors.InternalServerError).response(response)