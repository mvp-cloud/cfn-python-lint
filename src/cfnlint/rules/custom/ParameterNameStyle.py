"""
Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
"""
import re
from cfnlint.rules import CloudFormationLintRule
from cfnlint.rules import RuleMatch


class ParameterNameStyle(CloudFormationLintRule):
    """Check if Parameters follow style guide"""
    id = 'E9100'
    shortdesc = 'Parameter names follow proper structure'
    description = 'Parameters begin with a lowercase \'p\' and are in pCamelCase'
    source_url = ''
    tags = ['parameters']

    def match(self, cfn):
        """Check CloudFormation Parameters"""

        matches = []
        pattern = re.compile("^([p][A-Z_0-9]+[a-zA-Z0-9]*)+$")
        parameters = cfn.template.get('Parameters', {})
        if parameters:
            for paramname, val in parameters.items():
                if not pattern.match(paramname):
                    message = 'Parameters {0} should begin with a lowercase \'p\' and follow pCamelCase'
                    matches.append(RuleMatch(
                        ['Parameters', paramname],
                        message.format(paramname)
                    ))
        return matches
