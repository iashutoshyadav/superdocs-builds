from app.guide_generator import generate_getting_started_guide
from app.superdocs_client import FakeSuperDocsClient


def test_generates_a_numbered_guide_from_a_feature_description():
    client = FakeSuperDocsClient()

    guide = generate_getting_started_guide(
        client,
        "Sign up for an account. Create an API key in Settings. Install the SDK with pip install widgets-sdk. "
        "Call client.create_widget to make your first widget.",
        session_id="guide-1",
    )

    assert "1." in guide
    assert "Sign up for an account" in guide
    assert "Call client.create_widget" in guide


def test_each_sentence_becomes_its_own_numbered_step():
    client = FakeSuperDocsClient()

    guide = generate_getting_started_guide(
        client, "Step one happens. Step two happens. Step three happens.", session_id="guide-2",
    )

    assert "1. Step one happens." in guide
    assert "2. Step two happens." in guide
    assert "3. Step three happens." in guide
