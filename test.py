# Мария Листова, 22-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request
import data

def test_get_order_by_track():
    response_order = sender_stand_request.post_order(data.order_body)
    track = response_order.json()["track"]
    response = sender_stand_request.get_order_info(track)
    assert response.status_code == 200