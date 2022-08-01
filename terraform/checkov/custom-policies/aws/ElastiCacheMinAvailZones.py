from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
from checkov.common.models.enums import CheckResult, CheckCategories


class ElastiCacheMinAvailZones(BaseResourceCheck):
    def __init__(self):
        name = "Ensure ElastiCache clusters are configured with at least 3 AZs."
        id = "CKV_IBT_004"
        supported_resources = ['aws_elasticache_replication_group']
        # Look at checkov/common/models/enums.py for options
        categories = [CheckCategories.BACKUP_AND_RECOVERY]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        """
            For this suggestion, we need to deploy clusters using cluster mode in at least 3 AZs.  Cluster mode is defined by the aws_elasticache_replication_group.  
            Cluster mode is enabled when the resource has num_node_groups and replicas_per_node_group.  availabilty_zones is deprecated; we use preferred_cache_cluster_azs instead.
            
            https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/elasticache_replication_group
        """
        if self.entity_type == 'aws_elasticache_replication_group':
            if 'cluster_mode' in conf.keys() or 'replicas_per_node_group' in conf.keys() and 'num_node_groups' in conf.keys():
                if "subnet_group_name" in conf.keys():
                    self.name = 'ElastiCache clusters have cluster mode enabled, and have a subnet_group_name'
                    return CheckResult.PASSED
            return CheckResult.FAILED

        if self.entity_type == 'aws_elasticache_subnet_group':
            if 'subnet_ids' in conf.keys():
                self.name = 'Elasticache has a subnet_id.  Please ensure that ' + conf['subnet_ids'] + ' has 3 AZs.'
                return CheckResult.PASSED
            return CheckResult.FAILED


scanner = ElastiCacheMinAvailZones()