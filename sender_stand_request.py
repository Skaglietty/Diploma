import configuration
import requests
import data

def post_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                          json=order_body,
                         headers=data.headers)

response = post_order(data.order_body)

def get_order_info(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_INFO + str(track))