from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
from packaging import version

# !!important -> Here is where we can define current recommendation of instances:
target_instances = ["db.r5.large", "db.r6g.large"]


class RDSClusterInstanceUpgrade(BaseResourceCheck):
    def __init__(self):
        name = "Ensure RDS instances and Aurora clusters are running with db.r5.large or db.r6g.large to take advantage of more modern hardware and better cost/performance ratio."
        id = "CKV_IBT_008"
        supported_resources = ['aws_rds_cluster_instance',
                               'aws_rds_cluster', 'aws_db_instance', 'aws_db_instance']
        categories = [CheckCategories.CONVENTION]
        super().__init__(name=name, id=id, categories=categories,
                         supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        """
        Based on recommendation that we upgrade RDS instances and Aurora clusters from db.r3.large to db.r5.large or db.r6g.large
        Notes: Is it possible to periodically update the latest appropriate instance automatically rather than manually?

        reference:
        https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/db_instance
        https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/rds_cluster
        https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html
        https://aws.amazon.com/rds/postgresql/pricing/?pg=pr&loc=3
        https://aws.amazon.com/rds/aurora/pricing/

        checkov custom policy reference:
        https://www.checkov.io/3.Custom%20Policies/Python%20Custom%20Policies.html
        https://www.checkov.io/3.Custom%20Policies/Examples.html
        """

        if 'instance_class' in conf.keys():
            instance_class = conf['instance_class'][0]
            if instance_class not in target_instances:
                return CheckResult.FAILED

        if 'db_cluster_instance_class' in conf.keys():
            instance_class = conf['db_cluster_instance_class'][0]
            if instance_class not in target_instances:
                return CheckResult.FAILED
        return CheckResult.PASSED


check = RDSClusterInstanceUpgrade()
