from rest_framework.exceptions import APIException


class DuplicateReviewException(APIException):
    status_code = 400 
    default_detail = {"code": status_code, 
                      "message": "You sent review for this movie before."}
