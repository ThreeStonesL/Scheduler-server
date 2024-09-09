from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import VARCHAR, ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column, DeclarativeBase
from typing import List

from .annotations import (
    snowflake_id_pk,
    str_not_null,
    color,
    datetime_not_null,
    str_unique_not_null,
    bytes_not_null,
    int_not_null,
    user_id,
)


class Base(DeclarativeBase):
    pass


DB = SQLAlchemy(model_class=Base)


class User(DB.Model):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True, nullable=False
    )
    email: Mapped[str_unique_not_null]
    username: Mapped[str_not_null]
    password: Mapped[bytes_not_null]

    folders: Mapped[List["Folder"]] = relationship(back_populates="user")
    checklists: Mapped[List["Checklist"]] = relationship(back_populates="user")
    groups: Mapped[List["Group"]] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return (
            f"{{User: id={self.id}, email={self.email},"
            f"username={self.username}, password={self.password}}}"
        )


class Folder(DB.Model):
    __tablename__ = "folder"

    id: Mapped[snowflake_id_pk]
    name: Mapped[str_not_null]
    icon: Mapped[str]
    color: Mapped[color]
    order: Mapped[int_not_null]
    modifiedTime: Mapped[datetime_not_null]
    userId: Mapped[user_id]

    user: Mapped[User] = relationship(back_populates="folders")
    checklists: Mapped[List["Checklist"]] = relationship(
        back_populates="folder"
    )

    def __repr__(self) -> str:
        return (
            f"{{Folder: id={self.id}, name={self.name}, icon={self.icon}, "
            f"color=#{self.color}, modifiedTime={self.modifiedTime}, userId={self.userId}}}"
        )


class Checklist(DB.Model):
    __tablename__ = "checklist"

    id: Mapped[snowflake_id_pk]
    name: Mapped[str_not_null]
    icon: Mapped[str]
    color: Mapped[color]
    order: Mapped[int_not_null]
    modifiedTime: Mapped[datetime_not_null]
    viewMode: Mapped[str] = mapped_column(VARCHAR(6))
    userId: Mapped[user_id]
    folderId: Mapped[int] = mapped_column(
        ForeignKey("folder.id"),
        nullable=False,
    )

    user: Mapped[User] = relationship(back_populates="checklists")
    folder: Mapped[Folder] = relationship(back_populates="checklists")
    groups: Mapped[List["Group"]] = relationship(back_populates="checklist")


class Group(DB.Model):
    __tablename__ = "group"

    id: Mapped[snowflake_id_pk]
    name: Mapped[str_not_null]
    icon: Mapped[str]
    color: Mapped[color]
    order: Mapped[int_not_null]
    modifiedTime: Mapped[datetime_not_null]
    userId: Mapped[user_id]
    checklistId: Mapped[int] = mapped_column(
        ForeignKey("checklist.id"), nullable=False
    )

    user: Mapped[User] = relationship(back_populates="groups")
    checklist: Mapped[Checklist] = relationship(back_populates="groups")
