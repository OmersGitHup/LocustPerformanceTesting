class Data:

    @classmethod
    def pet_create_payload(cls):

        payload = {
            "id": 3432,
            "category": {"id": 234,
                         "name": "string"
                         },
            "name": "Cevdet",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "string"}
            ],
            "status": "available"
        }
        return payload

    @classmethod
    def pet_update_payload(cls):

        payload={
            "id": 3432,
            "category": {
                "id": 0,
                "name": "string"
            },
            "name": "Yakup",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "string"
                }
            ],
            "status": "available"
        }
        return payload