"""
Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
"""
import re
from cfnlint.rules import CloudFormationLintRule
from cfnlint.rules import RuleMatch


class ResourceNameStyle(CloudFormationLintRule):
    """Check if Resources follow style guide"""
    id = 'E9400'
    shortdesc = 'Resource names follow proper structure'
    description = 'Resources begin with a lowercase \'r\' and are in rCamelCase'
    source_url = ''
    tags = ['resources']

    def match(self, cfn):
        """Check CloudFormation Resources"""

        matches = []
        pattern = re.compile("^([r][A-Z_0-9]+[a-zA-Z0-9]*)+$")
        resources = cfn.template.get('Resources', {})
        if resources:
            for resourcename, val  in resources.items():
                if not pattern.match(resourcename):
                    message = 'Resource {0} should begin with a lowercase \'r\' and follow rCamelCase'
                    matches.append(RuleMatch(
                        ['Resources', resourcename],
                        message.format(resourcename)
                    ))
        return matches
