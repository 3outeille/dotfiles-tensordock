"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import s2clientprotocol.common_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _DebugGameState:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _DebugGameStateEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_DebugGameState.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    show_map: _DebugGameState.ValueType  # 1
    control_enemy: _DebugGameState.ValueType  # 2
    food: _DebugGameState.ValueType  # 3
    free: _DebugGameState.ValueType  # 4
    all_resources: _DebugGameState.ValueType  # 5
    god: _DebugGameState.ValueType  # 6
    minerals: _DebugGameState.ValueType  # 7
    gas: _DebugGameState.ValueType  # 8
    cooldown: _DebugGameState.ValueType  # 9
    tech_tree: _DebugGameState.ValueType  # 10
    upgrade: _DebugGameState.ValueType  # 11
    fast_build: _DebugGameState.ValueType  # 12

class DebugGameState(_DebugGameState, metaclass=_DebugGameStateEnumTypeWrapper): ...

show_map: DebugGameState.ValueType  # 1
control_enemy: DebugGameState.ValueType  # 2
food: DebugGameState.ValueType  # 3
free: DebugGameState.ValueType  # 4
all_resources: DebugGameState.ValueType  # 5
god: DebugGameState.ValueType  # 6
minerals: DebugGameState.ValueType  # 7
gas: DebugGameState.ValueType  # 8
cooldown: DebugGameState.ValueType  # 9
tech_tree: DebugGameState.ValueType  # 10
upgrade: DebugGameState.ValueType  # 11
fast_build: DebugGameState.ValueType  # 12
global___DebugGameState = DebugGameState

@typing_extensions.final
class DebugCommand(google.protobuf.message.Message):
    """Issue various useful commands to the game engine."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DRAW_FIELD_NUMBER: builtins.int
    GAME_STATE_FIELD_NUMBER: builtins.int
    CREATE_UNIT_FIELD_NUMBER: builtins.int
    KILL_UNIT_FIELD_NUMBER: builtins.int
    TEST_PROCESS_FIELD_NUMBER: builtins.int
    SCORE_FIELD_NUMBER: builtins.int
    END_GAME_FIELD_NUMBER: builtins.int
    UNIT_VALUE_FIELD_NUMBER: builtins.int
    @property
    def draw(self) -> global___DebugDraw: ...
    game_state: global___DebugGameState.ValueType
    @property
    def create_unit(self) -> global___DebugCreateUnit: ...
    @property
    def kill_unit(self) -> global___DebugKillUnit: ...
    @property
    def test_process(self) -> global___DebugTestProcess: ...
    @property
    def score(self) -> global___DebugSetScore:
        """Useful only for single-player "curriculum" maps."""
    @property
    def end_game(self) -> global___DebugEndGame: ...
    @property
    def unit_value(self) -> global___DebugSetUnitValue: ...
    def __init__(
        self,
        *,
        draw: global___DebugDraw | None = ...,
        game_state: global___DebugGameState.ValueType | None = ...,
        create_unit: global___DebugCreateUnit | None = ...,
        kill_unit: global___DebugKillUnit | None = ...,
        test_process: global___DebugTestProcess | None = ...,
        score: global___DebugSetScore | None = ...,
        end_game: global___DebugEndGame | None = ...,
        unit_value: global___DebugSetUnitValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["command", b"command", "create_unit", b"create_unit", "draw", b"draw", "end_game", b"end_game", "game_state", b"game_state", "kill_unit", b"kill_unit", "score", b"score", "test_process", b"test_process", "unit_value", b"unit_value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["command", b"command", "create_unit", b"create_unit", "draw", b"draw", "end_game", b"end_game", "game_state", b"game_state", "kill_unit", b"kill_unit", "score", b"score", "test_process", b"test_process", "unit_value", b"unit_value"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["command", b"command"]) -> typing_extensions.Literal["draw", "game_state", "create_unit", "kill_unit", "test_process", "score", "end_game", "unit_value"] | None: ...

global___DebugCommand = DebugCommand

@typing_extensions.final
class DebugDraw(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TEXT_FIELD_NUMBER: builtins.int
    LINES_FIELD_NUMBER: builtins.int
    BOXES_FIELD_NUMBER: builtins.int
    SPHERES_FIELD_NUMBER: builtins.int
    @property
    def text(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DebugText]: ...
    @property
    def lines(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DebugLine]: ...
    @property
    def boxes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DebugBox]: ...
    @property
    def spheres(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DebugSphere]: ...
    def __init__(
        self,
        *,
        text: collections.abc.Iterable[global___DebugText] | None = ...,
        lines: collections.abc.Iterable[global___DebugLine] | None = ...,
        boxes: collections.abc.Iterable[global___DebugBox] | None = ...,
        spheres: collections.abc.Iterable[global___DebugSphere] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["boxes", b"boxes", "lines", b"lines", "spheres", b"spheres", "text", b"text"]) -> None: ...

global___DebugDraw = DebugDraw

@typing_extensions.final
class Line(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    P0_FIELD_NUMBER: builtins.int
    P1_FIELD_NUMBER: builtins.int
    @property
    def p0(self) -> s2clientprotocol.common_pb2.Point: ...
    @property
    def p1(self) -> s2clientprotocol.common_pb2.Point: ...
    def __init__(
        self,
        *,
        p0: s2clientprotocol.common_pb2.Point | None = ...,
        p1: s2clientprotocol.common_pb2.Point | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["p0", b"p0", "p1", b"p1"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["p0", b"p0", "p1", b"p1"]) -> None: ...

global___Line = Line

@typing_extensions.final
class Color(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    R_FIELD_NUMBER: builtins.int
    G_FIELD_NUMBER: builtins.int
    B_FIELD_NUMBER: builtins.int
    r: builtins.int
    g: builtins.int
    b: builtins.int
    def __init__(
        self,
        *,
        r: builtins.int | None = ...,
        g: builtins.int | None = ...,
        b: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["b", b"b", "g", b"g", "r", b"r"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["b", b"b", "g", b"g", "r", b"r"]) -> None: ...

global___Color = Color

@typing_extensions.final
class DebugText(google.protobuf.message.Message):
    """Display debug text on screen."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COLOR_FIELD_NUMBER: builtins.int
    TEXT_FIELD_NUMBER: builtins.int
    VIRTUAL_POS_FIELD_NUMBER: builtins.int
    WORLD_POS_FIELD_NUMBER: builtins.int
    SIZE_FIELD_NUMBER: builtins.int
    @property
    def color(self) -> global___Color: ...
    text: builtins.str
    """Text to display."""
    @property
    def virtual_pos(self) -> s2clientprotocol.common_pb2.Point:
        """Virtualized position in 2D (the screen is 0..1, 0..1 for any resolution)."""
    @property
    def world_pos(self) -> s2clientprotocol.common_pb2.Point:
        """Position in the world."""
    size: builtins.int
    """Pixel height of the text. Defaults to 8px."""
    def __init__(
        self,
        *,
        color: global___Color | None = ...,
        text: builtins.str | None = ...,
        virtual_pos: s2clientprotocol.common_pb2.Point | None = ...,
        world_pos: s2clientprotocol.common_pb2.Point | None = ...,
        size: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["color", b"color", "size", b"size", "text", b"text", "virtual_pos", b"virtual_pos", "world_pos", b"world_pos"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["color", b"color", "size", b"size", "text", b"text", "virtual_pos", b"virtual_pos", "world_pos", b"world_pos"]) -> None: ...

global___DebugText = DebugText

@typing_extensions.final
class DebugLine(google.protobuf.message.Message):
    """Display debug lines on screen."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COLOR_FIELD_NUMBER: builtins.int
    LINE_FIELD_NUMBER: builtins.int
    @property
    def color(self) -> global___Color: ...
    @property
    def line(self) -> global___Line:
        """World space line."""
    def __init__(
        self,
        *,
        color: global___Color | None = ...,
        line: global___Line | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["color", b"color", "line", b"line"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["color", b"color", "line", b"line"]) -> None: ...

global___DebugLine = DebugLine

@typing_extensions.final
class DebugBox(google.protobuf.message.Message):
    """Display debug boxes on screen."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COLOR_FIELD_NUMBER: builtins.int
    MIN_FIELD_NUMBER: builtins.int
    MAX_FIELD_NUMBER: builtins.int
    @property
    def color(self) -> global___Color: ...
    @property
    def min(self) -> s2clientprotocol.common_pb2.Point: ...
    @property
    def max(self) -> s2clientprotocol.common_pb2.Point: ...
    def __init__(
        self,
        *,
        color: global___Color | None = ...,
        min: s2clientprotocol.common_pb2.Point | None = ...,
        max: s2clientprotocol.common_pb2.Point | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["color", b"color", "max", b"max", "min", b"min"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["color", b"color", "max", b"max", "min", b"min"]) -> None: ...

global___DebugBox = DebugBox

@typing_extensions.final
class DebugSphere(google.protobuf.message.Message):
    """Display debug spheres on screen."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COLOR_FIELD_NUMBER: builtins.int
    P_FIELD_NUMBER: builtins.int
    R_FIELD_NUMBER: builtins.int
    @property
    def color(self) -> global___Color: ...
    @property
    def p(self) -> s2clientprotocol.common_pb2.Point: ...
    r: builtins.float
    def __init__(
        self,
        *,
        color: global___Color | None = ...,
        p: s2clientprotocol.common_pb2.Point | None = ...,
        r: builtins.float | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["color", b"color", "p", b"p", "r", b"r"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["color", b"color", "p", b"p", "r", b"r"]) -> None: ...

global___DebugSphere = DebugSphere

@typing_extensions.final
class DebugCreateUnit(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    UNIT_TYPE_FIELD_NUMBER: builtins.int
    OWNER_FIELD_NUMBER: builtins.int
    POS_FIELD_NUMBER: builtins.int
    QUANTITY_FIELD_NUMBER: builtins.int
    unit_type: builtins.int
    owner: builtins.int
    @property
    def pos(self) -> s2clientprotocol.common_pb2.Point2D: ...
    quantity: builtins.int
    def __init__(
        self,
        *,
        unit_type: builtins.int | None = ...,
        owner: builtins.int | None = ...,
        pos: s2clientprotocol.common_pb2.Point2D | None = ...,
        quantity: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["owner", b"owner", "pos", b"pos", "quantity", b"quantity", "unit_type", b"unit_type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["owner", b"owner", "pos", b"pos", "quantity", b"quantity", "unit_type", b"unit_type"]) -> None: ...

global___DebugCreateUnit = DebugCreateUnit

@typing_extensions.final
class DebugKillUnit(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TAG_FIELD_NUMBER: builtins.int
    @property
    def tag(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(
        self,
        *,
        tag: collections.abc.Iterable[builtins.int] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["tag", b"tag"]) -> None: ...

global___DebugKillUnit = DebugKillUnit

@typing_extensions.final
class DebugTestProcess(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Test:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _TestEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[DebugTestProcess._Test.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        hang: DebugTestProcess._Test.ValueType  # 1
        crash: DebugTestProcess._Test.ValueType  # 2
        exit: DebugTestProcess._Test.ValueType  # 3

    class Test(_Test, metaclass=_TestEnumTypeWrapper): ...
    hang: DebugTestProcess.Test.ValueType  # 1
    crash: DebugTestProcess.Test.ValueType  # 2
    exit: DebugTestProcess.Test.ValueType  # 3

    TEST_FIELD_NUMBER: builtins.int
    DELAY_MS_FIELD_NUMBER: builtins.int
    test: global___DebugTestProcess.Test.ValueType
    delay_ms: builtins.int
    def __init__(
        self,
        *,
        test: global___DebugTestProcess.Test.ValueType | None = ...,
        delay_ms: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["delay_ms", b"delay_ms", "test", b"test"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["delay_ms", b"delay_ms", "test", b"test"]) -> None: ...

global___DebugTestProcess = DebugTestProcess

@typing_extensions.final
class DebugSetScore(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SCORE_FIELD_NUMBER: builtins.int
    score: builtins.float
    def __init__(
        self,
        *,
        score: builtins.float | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["score", b"score"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["score", b"score"]) -> None: ...

global___DebugSetScore = DebugSetScore

@typing_extensions.final
class DebugEndGame(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _EndResult:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _EndResultEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[DebugEndGame._EndResult.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        Surrender: DebugEndGame._EndResult.ValueType  # 1
        """Default if nothing is set. The current player admits defeat."""
        DeclareVictory: DebugEndGame._EndResult.ValueType  # 2

    class EndResult(_EndResult, metaclass=_EndResultEnumTypeWrapper): ...
    Surrender: DebugEndGame.EndResult.ValueType  # 1
    """Default if nothing is set. The current player admits defeat."""
    DeclareVictory: DebugEndGame.EndResult.ValueType  # 2

    END_RESULT_FIELD_NUMBER: builtins.int
    end_result: global___DebugEndGame.EndResult.ValueType
    def __init__(
        self,
        *,
        end_result: global___DebugEndGame.EndResult.ValueType | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["end_result", b"end_result"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["end_result", b"end_result"]) -> None: ...

global___DebugEndGame = DebugEndGame

@typing_extensions.final
class DebugSetUnitValue(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _UnitValue:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _UnitValueEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[DebugSetUnitValue._UnitValue.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        Energy: DebugSetUnitValue._UnitValue.ValueType  # 1
        Life: DebugSetUnitValue._UnitValue.ValueType  # 2
        Shields: DebugSetUnitValue._UnitValue.ValueType  # 3

    class UnitValue(_UnitValue, metaclass=_UnitValueEnumTypeWrapper): ...
    Energy: DebugSetUnitValue.UnitValue.ValueType  # 1
    Life: DebugSetUnitValue.UnitValue.ValueType  # 2
    Shields: DebugSetUnitValue.UnitValue.ValueType  # 3

    UNIT_VALUE_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    UNIT_TAG_FIELD_NUMBER: builtins.int
    unit_value: global___DebugSetUnitValue.UnitValue.ValueType
    value: builtins.float
    unit_tag: builtins.int
    def __init__(
        self,
        *,
        unit_value: global___DebugSetUnitValue.UnitValue.ValueType | None = ...,
        value: builtins.float | None = ...,
        unit_tag: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["unit_tag", b"unit_tag", "unit_value", b"unit_value", "value", b"value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["unit_tag", b"unit_tag", "unit_value", b"unit_value", "value", b"value"]) -> None: ...

global___DebugSetUnitValue = DebugSetUnitValue
