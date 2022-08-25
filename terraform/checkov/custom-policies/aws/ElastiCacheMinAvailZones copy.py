from lib2to3.pgen2.pgen import DFAState
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
from checkov.common.models.enums import CheckResult, CheckCategories


class ElastiCacheMinAvailZones(BaseResourceCheck):
    def __init__(self):
        name = "Ensure ElastiCache clusters are configured with at least 3 AZs.\nhttps://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/elasticache_replication_group"
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
        # first make sure that it is a redis cluster with cluster mode enabled
        # then make sure that multi-az is enabled
        if self.entity_type == 'aws_elasticache_replication_group':
            if 'parameter_group_name' in conf.keys():
                param_data = conf['parameter_group_name'][0].split('.')
                #check to make sure that this is an instance where cluster mode is enabled.
                if param_data[len(param_data) - 2] == 'cluster' and param_data[len(param_data) - 1] == 'on':
                    if 'cluster_mode' in conf.keys():
                        # still have to figure out how to make it count AZs
                        if 'preferred_cache_cluster_azs' in conf.keys():
                            if 'automatic_failover_enabled' in conf.keys() and conf['automatic_failover_enabled'][0]:
                                if 'multi_az_enabled' in conf.keys() and conf['multi_az_enabled'][0]:
                                    if 'num_cache_clusters' in conf.keys() and conf['num_cache_clusters'][0] >= 2:
                                        return CheckResult.PASSED
                                    self.name = "ElasticCache cluster mode is enabled, please make sure num_cache_clusters attribute is >= 2 and that 3 AZs are defined."
                                    return CheckResult.FAILED 
                                self.name = "ElasticCache cluster mode is enabled, please add \'multi_az_enabled\' attribute.\nhttps://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/elasticache_replication_group#multi_az_enabled" 
                                return CheckResult.FAILED 
                            self.name = "ElasticCache cluster mode is enabled, however \'automatic_failover_cluster_azs\' must be set to true."    
                            return CheckResult.FAILED
                        self.name = "ElasticCache cluster mode is enabled, however multi-azs using \'preferred_cache_cluster_azs\' attribute is necessary.\nhttps://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/elasticache_replication_group#preferred_cache_cluster_azs"
                        return CheckResult.FAILED
                    self.name = "ElastiCache cluster mode is enabled, however \'cluster_mode\' is deprecated.  Please update resource per terraform documentation:\nhttps://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/elasticache_replication_group#cluster_mode"
                    return CheckResult.FAILED
                return CheckResult.PASSED

scanner = ElastiCacheMinAvailZones()