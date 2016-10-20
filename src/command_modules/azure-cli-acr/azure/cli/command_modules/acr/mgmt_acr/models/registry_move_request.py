#---------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#---------------------------------------------------------------------------------------------
#pylint: skip-file
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 0.16.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RegistryMoveRequest(Model):
    """RegistryMoveRequest

    :param target_resource_group:
    :type target_resource_group: str
    :param resources:
    :type resources: list of str
    """ 

    _attribute_map = {
        'target_resource_group': {'key': 'targetResourceGroup', 'type': 'str'},
        'resources': {'key': 'resources', 'type': '[str]'},
    }

    def __init__(self, target_resource_group=None, resources=None):
        self.target_resource_group = target_resource_group
        self.resources = resources