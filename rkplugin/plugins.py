# pylint: disable=maybe-no-member
from inspect import isabstract
from typing import List
import wx
import abc
from dataclasses import dataclass
from enum import Enum
from .api import Node


@dataclass
class PluginMetadata:
    name: str
    author: str
    version: str
    short_desc: str
    long_desc: str


class PluginType(Enum):
    NULL = 0
    COMMAND = 1
    WINDOWED = 2


class Plugin:
    metadata: PluginMetadata
    ptype: PluginType

    def __init__(self, metadata: PluginMetadata, ptype: PluginType):
        self.metadata = metadata
        self.ptype = ptype

    def on_did_add_node(self, node: Node):
        pass

    def on_moving_node(self, node: Node):
        # TODO not implemented
        pass

    def on_did_move_node(self, node: Node):
        # TODO not implemented
        pass

    def on_will_paint(self, gc: wx.GraphicsContext):
        # TODO not implemented
        pass

    def on_selection_did_change(self, node_indices: List[int], reaction_indices: List[int]):
        pass

    
class CommandPlugin(Plugin, abc.ABC):
    def __init__(self, metadata: PluginMetadata):
        super().__init__(metadata, PluginType.COMMAND)

    @abc.abstractmethod
    def run(self):
        pass


class WindowedPlugin(Plugin, abc.ABC):
    def __init__(self, metadata: PluginMetadata):
        super().__init__(metadata, PluginType.WINDOWED)

    @abc.abstractmethod
    def create_window(self, parent: wx.Window) -> wx.Window:
        pass

    def on_will_close_window(self, evt):
        evt.Skip()

    def on_did_focus(self):
        pass

    def on_did_unfocus(self):
        pass
