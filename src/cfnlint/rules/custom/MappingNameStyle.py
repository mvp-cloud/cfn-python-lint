"""
Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
"""
import re
from cfnlint.rules import CloudFormationLintRule
from cfnlint.rules import RuleMatch


class MappingNameStyle(CloudFormationLintRule):
    """Check if Mappings follow style guide"""
    id = 'E9200'
    shortdesc = 'Mapping names follow proper structure'
    description = 'Mappings begin with a lowercase \'m\' and are in mCamelCase'
    source_url = ''
    tags = ['mappings']

    def match(self, cfn):
        """Check CloudFormation Mappings"""

        matches = []
        pattern = re.compile("^([m][A-Z_0-9]+[a-zA-Z0-9]*)+$")
        mappings = cfn.template.get('Mappings', {})
        if mappings:
            for mappingname, val  in mappings.items():
                if pattern.match(mappingname):
                    message = 'Mapping {0} should begin with a lowercase \'m\' and follow mCamelCase'
                    matches.append(RuleMatch(
                        ['Mappings', mappingname],
                        message.format(mappingname)
                    ))
        return matches
