from datetime import datetime
from typing import Annotated
from sqlalchemy import VARCHAR, BigInteger, DateTime, ForeignKey, String
from sqlalchemy.orm import mapped_column


str_not_null = Annotated[str, mapped_column(String, nullable=False)]
str_unique_not_null = Annotated[
    str, mapped_column(String, nullable=False, unique=True)
]

bytes_not_null = Annotated[bytes, mapped_column(nullable=False)]

int_not_null = Annotated[int, mapped_column(nullable=False)]

snowflake_id_pk = Annotated[
    int, mapped_column(BigInteger, nullable=False, primary_key=True)
]
snowflake_id = Annotated[int, mapped_column(BigInteger, nullable=False)]

color = Annotated[str, mapped_column(VARCHAR(6))]

datetime_not_null = Annotated[
    datetime, mapped_column(DateTime, nullable=False)
]

user_id = Annotated[int, mapped_column(ForeignKey("user.id"))]
