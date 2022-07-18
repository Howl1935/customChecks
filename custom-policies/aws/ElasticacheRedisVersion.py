from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
from packaging import version

# !!important -> Here is where we can define current version of redis:
latest_redis_version = "4.3.4"

class ElasticacheRedisVersion(BaseResourceCheck):
    def __init__(self):
        name = "Ensure Redis version is up to date to leverage a more modern feature set"
        id = "CKV_IBT_003"
        supported_resources = ['aws_elasticache_cluster']
        categories = [CheckCategories.CONVENTION]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        """
        Confirm that redis version is up to date to leverage a more modern feature set
        Notes: Is it possible to periodically update latest_redis_version automatically rather than manually?

        reference:
        https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/elasticache_cluster
        https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/supported-engine-versions.html

        checkov custom policy reference:
        https://www.checkov.io/3.Custom%20Policies/Python%20Custom%20Policies.html
        https://www.checkov.io/3.Custom%20Policies/Examples.html
        """
        if 'engine' in conf.keys():
            engine_type = conf['engine'][0]
            if engine_type == 'redis':
                if 'engine_version' in conf.keys():
                    engine_version = conf['engine_version'][0]
                    if version.parse(engine_version) < version.parse(latest_redis_version): 
                        return CheckResult.FAILED
        return CheckResult.PASSED


check = ElasticacheRedisVersion()