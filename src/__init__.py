"""
This file registers the model with the Python SDK.
"""

from viam.services.vision import Vision
from viam.resource.registry import Registry, ResourceCreatorRegistration

from .chatgpt import chatgpt

Registry.register_resource_creator(Vision.SUBTYPE, chatgpt.MODEL, ResourceCreatorRegistration(chatgpt.new, chatgpt.validate))
