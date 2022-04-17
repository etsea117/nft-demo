import pytest
from scripts.advanced_collectible.create_metadata import upload_to_ipfs


def test_upload_to_ipfs():
    pytest.skip()
    # Arrange
    image_path = "./img/" + breed.lower().replace("_", "-") + ".png"
    # Act
    image_uri = upload_to_ipfs(image_path)
    # Assert
