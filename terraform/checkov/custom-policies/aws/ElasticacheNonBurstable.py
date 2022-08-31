from lib2to3.pgen2.pgen import DFAState
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
from checkov.common.models.enums import CheckResult, CheckCategories

latest_instances = ['cache.t3.micro', 'cache.t3.small', 'cache.t3.medium']


class ElasticacheNonBurstable(BaseResourceCheck):
    def __init__(self):
        name = "Ensure clusters are deployed using T3 instances or non-burstable instance types for production workloads"
        id = "CKV_IBT_002"
        supported_resources = [
            'aws_elasticache_replication_group', 'aws_elasticache_cluster']
        # Look at checkov/common/models/enums.py for options
        categories = [CheckCategories.BACKUP_AND_RECOVERY]
        super().__init__(name=name, id=id, categories=categories,
                         supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        """
 # Deploy clusters using T3 instances or non-burstable instance types for production workloads
# Notes: Confirm that these instances are the correct ones to avoid and there aren't others.  Also, can we define production workloads?

# reference:
# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/elasticache_cluster
# https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/CacheNodes.SupportedTypes.html

# checkov custom policy reference:
# https://www.checkov.io/3.Custom%20Policies/YAML%20Custom%20Policies.html
# https://www.checkov.io/3.Custom%20Policies/Examples.html

        """

        if self.entity_type == 'aws_elasticache_replication_group' or self.entity_type == 'aws_elasticache_cluster':
            if 'node_type' in conf.keys():
                node_type = conf['node_type'][0]
                if node_type in latest_instances:
                    return CheckResult.PASSED
                return CheckResult.FAILED


scanner = ElasticacheNonBurstable()
