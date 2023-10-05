import configuration
import requests
import data

def get_logistics():
    return requests.get(configuration.URL)
response = get_logistics()
print(response.status_code)
print(response.headers)

def post_authorization(user_body):
    return requests.post(configuration.URL_POST,
                         json=user_body,
                         headers=data.headers)
response = post_authorization(data.user_body)
print(response.status_code)
print(response.json())

def post_comment(comment_body):
    return requests.post(configuration.URL_POST_COMMENT,
                         json=comment_body,
                         headers=data.headers)
response = post_comment(data.comment_body)
print(response.status_code)
print(response.text)

def put_comment(comment_body_put):
    return requests.post(configuration.URL_POST_COMMENT,
                         json=comment_body_put,
                         headers=data.headers)
response = put_comment(data.comment_body_put)
print(response.status_code)
print(response.text)

def delete_product():
    return requests.delete(configuration.URL_DELETE_PRODUCT,
                         headers=data.headers)
response = delete_product()
print(response.status_code)
print(response.text)


def post_save_in_draft(product_body):
    return requests.post(configuration.URL_POST_DRAFT,
                         json=product_body,
                         headers=data.headers)

response = post_save_in_draft(data.product_body)
print(response.status_code)
print(response.text)