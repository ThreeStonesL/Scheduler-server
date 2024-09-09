import datetime
import pytest

from src.models.folder import add_folder_info


@pytest.mark.usefixtures("app_ctx")
def test_folder():
    add_folder_info(
        id=1,
        name="test",
        modifiedTime=datetime.datetime.now(),
        userId=5,
        order=1,
        icon="😀",
        color="223355",
    )
