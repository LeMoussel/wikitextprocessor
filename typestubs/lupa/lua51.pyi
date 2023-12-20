from typing import (
    Any,
    Callable,
    NoReturn,
    Optional,
    Union,
)

LuaNumber = Union[int, float]

LUA_MAXINTEGER: LuaNumber
LUA_MININTEGER: LuaNumber
LUA_VERSION: LuaNumber

class LuaError(Exception): ...
class LuaSyntaxError(LuaError): ...
class LuaMemoryError(LuaError, MemoryError): ...
class _PyProtocolWrapper(object): ...

class _LuaObject(object):
    def __init__(self) -> None: ...
    def __dealloc__(self) -> None: ...
    def __call__(self, *args: Any) -> Any: ...
    def __len__(self) -> int: ...
    def __nonzero__(self) -> bool:
        return True
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def __iter__(self) -> Union[NoReturn, _LuaIter]: ...
    def __next__(self) -> Any: ...
    def __getattr__(self, name: str) -> Any: ...
    def __getitem__(self, name: Any) -> Any: ...

class _LuaIter(_LuaObject):
    def __init__(self, kind: LuaNumber) -> None: ...
    def __dealloc__(self) -> None: ...
    def __repr__(self) -> str: ...
    def __iter__(self) -> _LuaIter: ...
    def __next__(self) -> Any: ...

class _LuaTable(_LuaObject):
    def __iter__(self) -> _LuaIter: ...
    def keys(self) -> _LuaIter: ...
    def values(self) -> _LuaIter: ...
    def items(self) -> _LuaIter: ...
    def __setattr__(self, name: str, value: Any) -> None: ...
    def __setitem__(self, name: Any, value: Any) -> None: ...
    def __delattr__(self, name: str) -> None: ...
    def __delitem__(self, name: Any) -> None: ...

def as_attrgetter(obj: Any) -> _PyProtocolWrapper: ...
def as_itemgetter(obj: Any) -> _PyProtocolWrapper: ...
def lua_type(obj: Any) -> Optional[str]: ...
def unpacks_lua_table(func: Callable[..., Any]) -> Callable[..., Any]: ...
def unpacks_lua_table_method(
    meth: Callable[..., Any],
) -> Callable[..., Any]: ...

class LuaRuntime(object):
    encoding: str = "UTF-8"
    source_encoding: Optional[str] = None
    attribute_filter: Optional[Callable] = None
    attribute_handlers: Optional[Callable] = None
    register_eval: bool = True
    unpack_returned_tuples: bool = False
    register_builtins: bool = True
    overflow_handler: Optional[Callable] = None
    max_memory: Optional[LuaNumber] = None

    def __init__(
        self,
        encoding: str = "UTF-8",
        source_encoding: Optional[str] = None,
        attribute_filter: Optional[Callable] = None,
        attribute_handlers: Optional[Callable] = None,
        register_eval: bool = True,
        unpack_returned_tuples: bool = False,
        register_builtins: bool = True,
        overflow_handler: Optional[Callable] = None,
        max_memory: Optional[LuaNumber] = None,
    ): ...
    def get_max_memory(self, total: bool = False) -> Optional[LuaNumber]: ...
    def get_memory_used(self, total: bool = False) -> Optional[LuaNumber]: ...
    @property
    def lua_version(self) -> LuaNumber: ...
    @property
    def lua_implementation(self) -> str: ...
    def eval(self, lua_code: str, *args: Any) -> Any: ...
    def execute(self, lua_code: str, *args: Any) -> Any: ...
    def compile(self, lua_code: str) -> Callable[..., Any]: ...
    def require(self, modulename: str) -> None: ...
    def globals(self) -> Optional[_LuaTable]: ...
    def table(self, *args: Any, **kwargs: Any) -> _LuaTable: ...
    def table_from(self, *args: Any) -> _LuaTable: ...
    def set_max_memory(
        self, max_memory: LuaNumber, total: bool = False
    ) -> None: ...
    def set_overflow_handler(self, overflow_handler: Callable) -> None: ...

# Names in __all__ with no definition:
#   LUA_MAXINTEGER
#   LUA_MININTEGER
#   LUA_VERSION
#   LuaError
#   LuaMemoryError
#   LuaRuntime
#   LuaSyntaxError
#   as_attrgetter
#   as_itemgetter
#   lua_type
#   unpacks_lua_table
#   unpacks_lua_table_method
