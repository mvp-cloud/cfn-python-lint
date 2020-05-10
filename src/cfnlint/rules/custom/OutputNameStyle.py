"""
Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
"""
import re
from cfnlint.rules import CloudFormationLintRule
from cfnlint.rules import RuleMatch


class OutputNameStyle(CloudFormationLintRule):
    """Check if Outputs follow style guide"""
    id = 'E9500'
    shortdesc = 'Output names follow proper structure'
    description = 'Outputs begin with a lowercase \'o\' and are in oCamelCase'
    source_url = ''
    tags = ['outputs']

    def match(self, cfn):
        """Check CloudFormation Outputs"""

        matches = []
        pattern = re.compile("^([o][A-Z_0-9]+[a-zA-Z0-9]*)+$")
        outputs = cfn.template.get('Outputs', {})
        if outputs:
            for outputname, val in outputs.items():
                if not pattern.match(outputname):
                    message = 'Output {0} should begin with a lowercase \'o\' and follow oCamelCase'
                    matches.append(RuleMatch(
                        ['Outputs', outputname],
                        message.format(outputname)
                    ))
        return matches
