from .fixture import api_call_response


def test_name_is_carbon_credits(api_call_response):
    assert api_call_response.get("Name") == "Carbon credits"


def test_can_relist_is_true(api_call_response):
    assert api_call_response.get("CanRelist")


def test_gallery_description(api_call_response):
    promotion_list = api_call_response.get("Promotions")
    promotion_named_gallery = list(
        filter(lambda gallery: gallery["Name"] == "Gallery", promotion_list)
    )
    assert promotion_named_gallery[0].get("Description").find("2x larger image") != -1
