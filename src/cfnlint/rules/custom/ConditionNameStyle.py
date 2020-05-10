"""
Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
"""
import re
from cfnlint.rules import CloudFormationLintRule
from cfnlint.rules import RuleMatch


class ConditionNameStyle(CloudFormationLintRule):
    """Check if Conditions follow style guide"""
    id = 'W9300'
    shortdesc = 'Condition names follow proper structure'
    description = 'Conditions begin with a lowercase \'c\' and are in cCamelCase'
    source_url = ''
    tags = ['conditions']

    def match(self, cfn):
        """Check CloudFormation Conditions"""

        matches = []
        pattern = re.compile("^([c][A-Z_0-9]+[a-zA-Z0-9]*)+$")
        conditions = cfn.template.get('Conditions', {})
        if conditions:
            for condname, val in conditions.items():
                if not pattern.match(condname):
                    message = 'Condition {0} has improper naming scheme'
                    matches.append(RuleMatch(
                        ['Conditions', condname],
                        message.format(condname)
                    ))
        return matches
