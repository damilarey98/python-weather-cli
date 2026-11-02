
import weather


def test_get_coordinates_returns_coordinates(monkeypatch):
    class FakeResponse:
        def raise_for_status(self):
            pass

        def json(self):
            return {
                "results": [
                    {
                        "latitude": 6.5244,
                        "longitude": 3.3792
                    }
                ]
            }

    def fake_get(*args, **kwargs):
        return FakeResponse()

    monkeypatch.setattr(weather.requests, "get", fake_get)

    result = weather.get_coordinates("Lagos")

    assert result == (6.5244, 3.3792)



def test_get_coordinates_returns_none_for_unknown_city(monkeypatch):
    class FakeResponse:
        def raise_for_status(self):
            pass

        def json(self):
            return {"results": []}

    def fake_get(*args, **kwargs):
        return FakeResponse()

    monkeypatch.setattr(weather.requests, "get", fake_get)

    result = weather.get_coordinates("UnknownCity")

    assert result is None


def test_get_coordinates_handles_api_failure(monkeypatch):
    def fake_get(*args, **kwargs):
        raise weather.requests.exceptions.ConnectionError(
            "API unavailable"
        )

    monkeypatch.setattr(weather.requests, "get", fake_get)

    import pytest

    with pytest.raises(weather.requests.exceptions.ConnectionError):
        weather.get_coordinates("Lagos")


def test_get_weather_returns_current_weather(monkeypatch):
    class FakeResponse:
        def raise_for_status(self):
            pass

        def json(self):
            return {
                "current": {
                    "temperature_2m": 30.5,
                    "wind_speed_10m": 12.4
                }
            }

    def fake_get(*args, **kwargs):
        return FakeResponse()

    monkeypatch.setattr(weather.requests, "get", fake_get)

    result = weather.get_weather(6.5244, 3.3792)

    assert result["temperature_2m"] == 30.5
    assert result["wind_speed_10m"] == 12.4
