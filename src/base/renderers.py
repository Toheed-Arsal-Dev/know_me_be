from rest_framework.renderers import JSONRenderer


class CustomJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = renderer_context.get("response")

        # Don't wrap errors again (already handled in custom_exception_handler)
        if response is not None and response.status_code not in range(200, 300):
            return super().render(data, accepted_media_type, renderer_context)

        # Success response wrapping
        response_data = {
            "success": True,
            "message": "Success",
            "data": data,
            "errors": None,
        }
        return super().render(response_data, accepted_media_type, renderer_context)
