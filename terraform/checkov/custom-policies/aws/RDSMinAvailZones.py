from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
from checkov.common.models.enums import CheckResult, CheckCategories


class RDSMinAvailZones(BaseResourceCheck):
    def __init__(self):
        name = "Ensure RDS instances are configured for at least 3 AZs.  Please add at least one reader node for Aurora clusters.  See: https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/rds_cluster"
        id = "CKV_IBT_007"
        supported_resources = ['aws_rds_cluster']
        # Look at checkov/common/models/enums.py for options
        categories = [CheckCategories.BACKUP_AND_RECOVERY]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        """
            Ensure that RDS instances are configured with multi-az and add at least one reader node.
            To create a Multi-AZ RDS cluster, you must additionally specify the engine, storage_type, allocated_storage, iops and db_cluster_instance_class attributes.
            https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/rds_cluster
            https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html
        """
        if self.entity_type == 'aws_rds_cluster':
            if 'engine' in conf.keys() and 'storage_type' in conf.keys() and 'allocated_storage' in conf.keys() and 'iops' in conf.keys() and 'db_cluster_instance_class' in conf.keys():
                if "availability_zones" in conf.keys():
                    # still have to figure out exactly to confirm that the listed AZ's are valid.
                    return CheckResult.PASSED
            return CheckResult.FAILED

        # Below is checking the subnet groups to make sure they are in 3 AZs above is going by terraform doc recommendations.
        # if self.entity_type == 'aws_elasticache_subnet_group':
        #     if 'subnet_ids' in conf.keys():
        #         self.name = 'Elasticache has a subnet_id.  Please ensure that ' + conf['subnet_ids'] + ' has 3 AZs.'
        #         return CheckResult.PASSED
        #     return CheckResult.FAILED


scanner = RDSMinAvailZones()