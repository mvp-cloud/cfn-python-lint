"""
Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
"""
from cfnlint.rules import CloudFormationLintRule
from cfnlint.rules import RuleMatch


class ParameterDescription(CloudFormationLintRule):
    """Check if Parameters contain a Description"""
    id = 'E9101'
    shortdesc = 'Parameters contain a Description'
    description = 'Check if each Parameter contains an informative Description attribute'
    source_url = ''
    tags = ['parameters']

    def match(self, cfn):
        """Check CloudFormation Parameters"""

        matches = []
        parameters = cfn.template.get('Parameters', {})
        if parameters:
            for paramname, paramvalue in cfn.get_parameters().items():
                description_value = paramvalue.get('Description')
                if description_value is not None:
                    if len(description_value) < 15:
                        message = 'Parameter {0} Description is < 15 chars'
                        matches.append(RuleMatch(
                            ['Parameters', paramname],
                            message.format(paramname)
                        ))                    
                else:
                    message = 'Parameter {0} has no Description'
                    matches.append(RuleMatch(
                        ['Parameters', paramname],
                        message.format(paramname)
                    ))
        return matches
