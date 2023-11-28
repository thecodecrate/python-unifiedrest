from typing import Any

from ..action.action_interface import ActionInterface

ActionsClasses = list[type[ActionInterface[Any, Any]]]
